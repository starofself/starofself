# 공시/IR 자동 분석기

기업명을 입력하면 DART 우선으로 PDF를 가져오고, 실패 시 웹 검색 기반으로 PDF를 탐색한 뒤 Gemini로 분석하는 Streamlit 앱입니다.

## 1) 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) 키 설정

`.env.example`을 복사해 `.env` 생성 후 API 키를 넣으세요.

```bash
cp .env.example .env
```

필수 값:
- `DART_API_KEY`
- `GOOGLE_API_KEY`

## 3) 실행

```bash
streamlit run app.py
```

## 4) 동작 개요

1. `ir_downloader.py`
   - DART 기반 PDF 다운로드 시도
   - 실패 시 웹 검색 기반 PDF 다운로드 fallback
2. `dart_fetcher.py`
   - 최신 공시에서 핵심 섹션 텍스트 보조 추출
3. `ai_analyzer.py`
   - Gemini File API 업로드 + 시스템 프롬프트 분석
4. `app.py`
   - Streamlit UI + 진행 상태 + 수동 PDF 업로드 fallback + 결과 저장

## 5) 장애 대응 (다운로드 실패)

- 자동 다운로드 실패 시 앱에서 에러 메시지를 확인하세요.
- 같은 화면의 **수동 PDF 업로드**에 IR 자료 PDF를 올리면 분석을 계속할 수 있습니다.
- DART 키 미설정/오류일 경우 웹 fallback이 자동 시도됩니다.

## 6) 최소 검증

외부 API 호출 없이 모듈 import 및 인터페이스를 확인하려면:

```bash
python scripts/check_imports.py
pytest -q
```
