"""Fetch core sections from DART business/quarterly/semiannual reports."""
from __future__ import annotations

from typing import Dict, List, Optional


DEFAULT_SECTION_KEYWORDS = [
    "사업의 내용",
    "재무에 관한 사항",
    "요약재무정보",
    "위험요소",
    "경영진단 및 분석",
]


def _extract_lines_with_keywords(text: str, keywords: List[str], window: int = 12) -> Dict[str, str]:
    lines = text.splitlines()
    result: Dict[str, str] = {}

    for i, line in enumerate(lines):
        for key in keywords:
            if key in line and key not in result:
                start = max(0, i)
                end = min(len(lines), i + window)
                result[key] = "\n".join(lines[start:end]).strip()
    return result


def fetch_report_sections(
    company_name: str,
    dart_api_key: str,
    section_keywords: Optional[List[str]] = None,
    report_types: Optional[List[str]] = None,
) -> Dict[str, str]:
    """Return text snippets for core report sections from latest filing.

    Notes:
    - Uses OpenDartReader API shape in a tolerant way.
    - Returns empty dict when nothing can be fetched.
    """
    import OpenDartReader

    keywords = section_keywords or DEFAULT_SECTION_KEYWORDS
    kinds = report_types or ["A", "F", "Q"]

    reader = OpenDartReader(dart_api_key)
    reports = reader.list(company_name, kind=" ".join(kinds), final=False)
    if reports is None or getattr(reports, "empty", True):
        return {}

    rcept_no = str(reports.iloc[0].get("rcept_no", ""))
    if not rcept_no:
        return {}

    doc_text = ""
    try:
        doc = reader.document(rcept_no)
        if isinstance(doc, bytes):
            doc_text = doc.decode("utf-8", errors="ignore")
        else:
            doc_text = str(doc)
    except Exception:
        # If API doesn't provide document text directly, return empty for caller fallback.
        return {}

    return _extract_lines_with_keywords(doc_text, keywords)
