from inspect import signature

from ai_analyzer import analyze_pdf_with_gemini
from dart_fetcher import fetch_report_sections
from ir_downloader import download_ir_pdf


def test_download_interface():
    params = signature(download_ir_pdf).parameters
    assert "company_name" in params


def test_fetch_interface():
    params = signature(fetch_report_sections).parameters
    assert "dart_api_key" in params


def test_analyzer_interface():
    params = signature(analyze_pdf_with_gemini).parameters
    assert "google_api_key" in params
