"""Helpers for Gemini analysis flows.

This module supports two modes:
1) API mode (optional): uses Gemini API key.
2) Web-login mode (no API): builds prompt/content for gemini.google.com manual run.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

DEFAULT_SYSTEM_PROMPT = """
당신은 한국 상장사 공시/IR 문서를 분석하는 애널리스트입니다.
다음을 제공하세요:
1) 핵심 사업/성장 포인트
2) 실적/재무 핵심 요약
3) 리스크 요인
4) 투자자 관점 체크포인트
5) 5줄 요약
표/불릿 중심으로 간결하게 작성하세요.
""".strip()


def build_gemini_web_prompt(company_name: str, extracted_sections: Optional[dict] = None) -> str:
    """Return a ready-to-paste prompt for Gemini web (login-based usage)."""
    sections_text = ""
    if extracted_sections:
        lines = []
        for k, v in extracted_sections.items():
            lines.append(f"## {k}\n{v}")
        sections_text = "\n\n".join(lines)

    return (
        f"[기업명] {company_name}\n\n"
        f"[시스템 지시]\n{DEFAULT_SYSTEM_PROMPT}\n\n"
        "[요청]\n첨부한 PDF와 아래 텍스트를 함께 참고해 분석해 주세요.\n"
        "결과는 '핵심 포인트/재무요약/리스크/체크포인트/5줄 요약' 순서로 작성하세요.\n\n"
        f"[보조 텍스트]\n{sections_text if sections_text else '(없음)'}"
    )


def analyze_pdf_with_gemini(
    pdf_path: str,
    google_api_key: str,
    user_prompt: Optional[str] = None,
    model_name: str = "gemini-1.5-pro",
) -> str:
    """Upload PDF via Gemini File API and run analysis with system prompt.

    Note: kept for optional API mode compatibility.
    """
    import google.generativeai as genai

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel(model_name=model_name, system_instruction=DEFAULT_SYSTEM_PROMPT)

    uploaded = genai.upload_file(path=str(path), mime_type="application/pdf")
    prompt = user_prompt or "문서를 분석해 핵심 인사이트를 정리해 주세요."
    response = model.generate_content([uploaded, prompt])
    return getattr(response, "text", "") or "분석 결과를 생성하지 못했습니다."
