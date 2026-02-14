from __future__ import annotations

import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from ai_analyzer import analyze_pdf_with_gemini
from dart_fetcher import fetch_report_sections
from ir_downloader import download_ir_pdf


load_dotenv()

st.set_page_config(page_title="IR Analyzer", page_icon="📊", layout="wide")
st.title("📊 공시/IR 자동 분석기")

company_name = st.text_input("기업명", placeholder="예: 삼성전자")
auto_run = st.button("자동 수집+분석 실행", type="primary")

manual_file = st.file_uploader("수동 PDF 업로드 (fallback)", type=["pdf"])

if auto_run and not company_name:
    st.warning("기업명을 입력해 주세요.")

if auto_run and company_name:
    dart_key = os.getenv("DART_API_KEY", "")
    google_key = os.getenv("GOOGLE_API_KEY", "")

    with st.status("1) PDF 다운로드 중...", expanded=True) as status:
        dl_result = download_ir_pdf(company_name, dart_api_key=dart_key)
        st.write(dl_result)
        status.update(label="1) 다운로드 단계 완료", state="complete")

    pdf_path: Path | None = None
    if dl_result.get("status") == "success":
        pdf_path = Path(dl_result["file_path"])
    elif manual_file is not None:
        uploads_dir = Path("uploads")
        uploads_dir.mkdir(exist_ok=True)
        pdf_path = uploads_dir / manual_file.name
        pdf_path.write_bytes(manual_file.read())
        st.info("자동 다운로드 실패로 수동 업로드 파일을 사용합니다.")
    else:
        st.error("자동 다운로드 실패. 아래 수동 업로드를 이용해 주세요.")

    if pdf_path and pdf_path.exists():
        with st.status("2) DART 텍스트 보조 추출 중...", expanded=False):
            sections = fetch_report_sections(company_name, dart_key) if dart_key else {}
            if sections:
                st.success(f"핵심 섹션 {len(sections)}개 추출")
            else:
                st.caption("보조 텍스트 추출 없음 (PDF 분석은 계속 진행)")

        if not google_key:
            st.error("GOOGLE_API_KEY가 없어 AI 분석을 수행할 수 없습니다.")
        else:
            with st.status("3) Gemini 분석 중...", expanded=True):
                analysis = analyze_pdf_with_gemini(str(pdf_path), google_key)

            st.subheader("분석 결과")
            st.markdown(analysis)

            out_dir = Path("outputs")
            out_dir.mkdir(exist_ok=True)
            out_file = out_dir / f"{company_name}_analysis.md"
            out_file.write_text(analysis, encoding="utf-8")
            st.success(f"결과 저장 완료: {out_file}")
