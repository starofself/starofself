# 공시/IR 홈페이지형 분석기

기업명을 입력하면 자동으로 DART 우선 PDF 수집을 시도하고, 실패 시 웹 검색 fallback을 수행한 뒤 **Gemini 웹 로그인 기반(비-API)** 분석을 진행하는 Streamlit 앱입니다.

## 1) 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) 키 설정

`.env.example`을 복사해 `.env` 생성 후 키를 넣으세요.

```bash
cp .env.example .env
```

- `DART_API_KEY`: 공시 보조 텍스트 추출/다운로드 정확도 향상용
- `GOOGLE_API_KEY`: **선택값** (API 모드 사용 시에만 필요)

## 3) 실행

```bash
streamlit run app.py
```

## 4) 기본 사용 흐름 (비-API, Gemini 로그인)

1. 기업명을 입력하면 자동 수집 시작
2. PDF 수집 결과 확인 (실패 시 수동 PDF 업로드)
3. 앱에서 생성한 프롬프트를 Gemini 웹(`https://gemini.google.com/app`)에 붙여넣기
4. Gemini 결과를 앱에 붙여넣고 저장

## 5) 왜 완전 자동 로그인이 아닌가?

- 개인 Gemini 웹 로그인 세션은 사용자 브라우저 컨텍스트에 묶여 있습니다.
- Streamlit 서버 코드가 해당 세션에 안전하게 직접 접근/제어할 수 없으므로, 본 앱은 현실적으로 안정적인 하이브리드 방식(자동 수집 + 수동 실행)을 제공합니다.

## 6) 최소 검증

```bash
python scripts/check_imports.py
pytest -q
```
