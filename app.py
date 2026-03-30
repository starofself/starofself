from __future__ import annotations

import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from ai_analyzer import analyze_pdf_with_gemini, build_gemini_web_prompt
from dart_fetcher import fetch_report_sections
from ir_downloader import download_ir_pdf


load_dotenv()

st.set_page_config(page_title="IR Homepage Analyzer", page_icon="📊", layout="wide")

st.markdown(
    """
<style>
.block-container {max-width: 1050px;}
.hero {padding: 1.2rem 1rem; border-radius: 16px; background: linear-gradient(135deg,#102a43,#243b53); color: #fff; margin-bottom: 1rem;}
.card {padding: 1rem; border-radius: 12px; border: 1px solid #dfe6ee; background: #f8fbff;}
.small {font-size: 0.9rem; color: #5b6b7a;}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <h2>📊 공시/IR 홈페이지형 분석기</h2>
  <p>기업명만 입력하면 자동으로 자료 수집을 시작하고, Gemini 웹 로그인 기반 분석을 진행합니다.</p>
</div>
""",
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1])
with left:
    company_name = st.text_input("기업명 입력", placeholder="예: 삼성전자", key="company_name")
    st.caption("입력 즉시 자동 수집 프로세스가 시작됩니다.")
with right:
    manual_file = st.file_uploader("수동 PDF 업로드", type=["pdf"])

if "last_company" not in st.session_state:
    st.session_state.last_company = ""
if "analysis_markdown" not in st.session_state:
    st.session_state.analysis_markdown = ""
if "download_result" not in st.session_state:
    st.session_state.download_result = None

should_run = bool(company_name.strip()) and company_name.strip() != st.session_state.last_company

if should_run:
    st.session_state.last_company = company_name.strip()
    dart_key = os.getenv("DART_API_KEY", "")

    with st.status("자동 수집 진행 중...", expanded=True) as status:
        dl_result = download_ir_pdf(company_name.strip(), dart_api_key=dart_key)
        st.session_state.download_result = dl_result
        st.write({"download": dl_result})
        status.update(label="자료 수집 단계 완료", state="complete")

    pdf_path: Path | None = None
    if dl_result.get("status") == "success":
        pdf_path = Path(dl_result["file_path"])
    elif manual_file is not None:
        uploads_dir = Path("uploads")
        uploads_dir.mkdir(exist_ok=True)
        pdf_path = uploads_dir / manual_file.name
        pdf_path.write_bytes(manual_file.read())
        st.info("자동 수집 실패로 수동 업로드 PDF를 사용합니다.")

    sections = {}
    if dart_key:
        with st.status("보조 텍스트 추출 중...", expanded=False):
            sections = fetch_report_sections(company_name.strip(), dart_key)

    st.markdown("### Gemini 웹 로그인 분석")
    st.markdown("API 없이 사용하려면 아래 절차를 따르세요.")
    web_prompt = build_gemini_web_prompt(company_name.strip(), sections)

    c1, c2 = st.columns([1, 1])
    with c1:
        st.link_button("1) Gemini 열기 (로그인)", "https://gemini.google.com/app")
        if pdf_path and pdf_path.exists():
            st.success(f"PDF 준비됨: {pdf_path}")
        else:
            st.warning("자동 PDF가 없으면 왼쪽 수동 업로드를 먼저 진행하세요.")
    with c2:
        st.download_button(
            "2) 프롬프트 txt 다운로드",
            data=web_prompt,
            file_name=f"{company_name.strip()}_gemini_prompt.txt",
            mime="text/plain",
        )

    st.text_area("Gemini에 붙여넣을 프롬프트", value=web_prompt, height=240)
    st.info("Gemini 웹에서 PDF 업로드 + 위 프롬프트 실행 후, 결과를 아래 칸에 붙여넣으세요.")

analysis_input = st.text_area("Gemini 결과 붙여넣기", value=st.session_state.analysis_markdown, height=260)
if analysis_input:
    st.session_state.analysis_markdown = analysis_input
    st.markdown("## 분석 결과")
    st.markdown(analysis_input)

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    save_name = (st.session_state.last_company or "company") + "_analysis.md"
    out_file = out_dir / save_name
    out_file.write_text(analysis_input, encoding="utf-8")
    st.success(f"결과 저장 완료: {out_file}")

st.markdown("---")
st.markdown(
    '<div class="card"><b>참고</b><div class="small">'
    "브라우저 로그인 세션(개인 Gemini 계정)은 Streamlit 서버 코드에서 직접 제어할 수 없습니다. "
    "따라서 본 앱은 로그인 기반 워크플로를 안전하게 지원하기 위해 '자동 수집 + 웹 프롬프트 생성 + 결과 붙여넣기' 형태로 제공합니다."
    "</div></div>",
    unsafe_allow_html=True,
)
