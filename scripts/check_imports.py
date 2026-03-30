"""Static interface check without external API calls."""
from __future__ import annotations

import sys
from inspect import signature
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import ai_analyzer
import dart_fetcher
import ir_downloader


def main() -> None:
    assert hasattr(ir_downloader, "download_ir_pdf")
    assert "company_name" in signature(ir_downloader.download_ir_pdf).parameters

    assert hasattr(dart_fetcher, "fetch_report_sections")
    assert "dart_api_key" in signature(dart_fetcher.fetch_report_sections).parameters

    assert hasattr(ai_analyzer, "analyze_pdf_with_gemini")
    assert "google_api_key" in signature(ai_analyzer.analyze_pdf_with_gemini).parameters

    assert hasattr(ai_analyzer, "build_gemini_web_prompt")
    assert "company_name" in signature(ai_analyzer.build_gemini_web_prompt).parameters

    print("OK: imports and interfaces are valid.")


if __name__ == "__main__":
    main()
