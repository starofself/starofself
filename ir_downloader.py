"""IR/PDF downloader with DART-first and web-search fallback."""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional
import re


class IRDownloadError(RuntimeError):
    """Raised when IR/PDF download fails in all strategies."""


@dataclass
class DownloadResult:
    status: str
    source: str
    file_path: Optional[str] = None
    message: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


def _safe_filename(name: str) -> str:
    cleaned = re.sub(r"[^0-9A-Za-z가-힣._-]+", "_", name).strip("_")
    return cleaned or "downloaded_ir"


def _download_file(url: str, target_path: Path, timeout: int = 20) -> Path:
    import requests

    response = requests.get(url, stream=True, timeout=timeout)
    response.raise_for_status()
    target_path.parent.mkdir(parents=True, exist_ok=True)
    with target_path.open("wb") as fp:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                fp.write(chunk)
    return target_path


def _try_dart_download(company_name: str, output_dir: Path, dart_api_key: str) -> Optional[Path]:
    """Try downloading a recent disclosure attachment from DART."""
    try:
        import OpenDartReader
    except Exception:
        return None

    reader = OpenDartReader(dart_api_key)
    reports = reader.list(company_name, kind="A", final=False)
    if reports is None or getattr(reports, "empty", True):
        return None

    latest = reports.iloc[0]
    rcept_no = str(latest.get("rcept_no", ""))
    report_nm = str(latest.get("report_nm", "dart_report"))
    if not rcept_no:
        return None

    candidate_urls = [
        f"https://dart.fss.or.kr/pdf/download/pdf.do?rcp_no={rcept_no}&dcm_no=0",
        f"https://dart.fss.or.kr/pdf/download/main.do?rcp_no={rcept_no}",
    ]
    for idx, url in enumerate(candidate_urls):
        try:
            out_file = output_dir / f"{_safe_filename(company_name)}_{_safe_filename(report_nm)}_{idx}.pdf"
            return _download_file(url, out_file)
        except Exception:
            continue
    return None


def _try_web_search_download(company_name: str, output_dir: Path) -> Optional[Path]:
    import requests
    from bs4 import BeautifulSoup

    query = f"{company_name} IR PDF"
    url = "https://duckduckgo.com/html/"
    response = requests.get(url, params={"q": query}, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a[href]")
    for link in links:
        href = link.get("href", "")
        if ".pdf" in href.lower():
            filename = _safe_filename(company_name) + "_web.pdf"
            try:
                return _download_file(href, output_dir / filename)
            except Exception:
                continue
    return None


def download_ir_pdf(company_name: str, output_dir: str = "downloads", dart_api_key: Optional[str] = None) -> dict:
    """Download IR-related PDF using DART first, then web-search fallback."""
    out_dir = Path(output_dir)

    if dart_api_key:
        try:
            dart_file = _try_dart_download(company_name, out_dir, dart_api_key)
            if dart_file:
                return DownloadResult(status="success", source="dart", file_path=str(dart_file)).to_dict()
        except Exception as exc:
            dart_error = str(exc)
        else:
            dart_error = "No matching DART file found."
    else:
        dart_error = "DART_API_KEY not set."

    try:
        web_file = _try_web_search_download(company_name, out_dir)
        if web_file:
            return DownloadResult(status="success", source="web", file_path=str(web_file)).to_dict()
    except Exception as exc:
        web_error = str(exc)
    else:
        web_error = "No PDF found in web search results."

    message = f"DART failed: {dart_error} / Web fallback failed: {web_error}"
    return DownloadResult(status="failed", source="none", message=message).to_dict()
