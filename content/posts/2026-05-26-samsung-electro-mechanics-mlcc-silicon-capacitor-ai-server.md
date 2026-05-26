---
title: "삼성전기 MLCC·실리콘캐패시터: AI 서버 전기를 ‘덜 먹게’ 만드는 진짜 이유"
date: 2026-05-26T15:45:00+09:00
draft: false
tags: ["삼성전기", "MLCC", "실리콘캐패시터", "AI서버", "데이터센터", "반도체패키징"]
categories: ["stock-research"]
slug: "samsung-electro-mechanics-mlcc-silicon-capacitor-ai-server"
description: "삼성전기 MLCC와 실리콘캐패시터가 AI 서버·데이터센터 전력효율에 유리한 이유를 그림과 함께 정리합니다."
summary: "캐패시터가 직접 전기를 아끼는 것이 아니라, ESR/ESL·전압마진·전원노이즈를 줄여 AI 서버의 성능/Watt를 개선합니다."
author: "Hermes / MasterClaw"
---

> 리서치 관점의 정리입니다. 투자 조언이 아닙니다.

## 한 줄 결론

삼성전기의 기존 **MLCC**는 AI 서버 보드·전원부·GPU/HBM 주변에서 계속 필요한 전원 안정화 기본 부품이고, **실리콘캐패시터**는 MLCC보다 비싸지만 GPU/HBM 패키지 내부처럼 아주 가까운 위치에서 초고주파 전원 흔들림을 잡는 고부가 보완재입니다.

“전기를 덜 먹는다”는 말은 엄밀히는 이렇게 바꿔야 합니다.

> 캐패시터가 직접 전기를 아끼는 게 아니라, ESR/ESL/누설/유전손실·전압마진·전원노이즈를 줄여서 시스템 전체의 손실·발열·오류·전압 여유분을 낮춘다.

---

## 1. 캐패시터는 전기를 먹는 부품이 아니라, 전기를 안정화하는 부품

이상적인 캐패시터는 전기를 소비하지 않습니다. 전기장을 통해 에너지를 저장했다가 다시 내보냅니다.

```text
저장 에너지 E = 1/2 · C · V²
```

하지만 실제 캐패시터는 완벽하지 않기 때문에 열과 손실이 생깁니다.

<div style="border:1px solid #e5e7eb;border-radius:18px;padding:18px;margin:24px 0;background:#fafafa;overflow-x:auto">
<svg width="860" height="360" viewBox="0 0 860 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="캐패시터 손실 구조 인포그래픽">
  <defs>
    <linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="#2563eb"/><stop offset="1" stop-color="#06b6d4"/></linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#0f172a" flood-opacity="0.16"/></filter>
  </defs>
  <rect x="30" y="45" width="800" height="270" rx="24" fill="white" filter="url(#shadow)"/>
  <text x="430" y="86" text-anchor="middle" font-size="25" font-weight="800" fill="#0f172a">왜 어떤 캐패시터가 ‘전기를 덜 먹는 것처럼’ 보일까?</text>
  <text x="430" y="116" text-anchor="middle" font-size="15" fill="#475569">핵심은 저장이 아니라 손실·노이즈·전압마진 감소</text>

  <rect x="75" y="155" width="140" height="86" rx="18" fill="#eff6ff" stroke="#93c5fd"/>
  <text x="145" y="187" text-anchor="middle" font-size="18" font-weight="700" fill="#1d4ed8">ESR</text>
  <text x="145" y="214" text-anchor="middle" font-size="13" fill="#334155">리플전류 I²R</text>
  <text x="145" y="233" text-anchor="middle" font-size="13" fill="#334155">발열 손실</text>

  <rect x="260" y="155" width="140" height="86" rx="18" fill="#ecfeff" stroke="#67e8f9"/>
  <text x="330" y="187" text-anchor="middle" font-size="18" font-weight="700" fill="#0e7490">ESL</text>
  <text x="330" y="214" text-anchor="middle" font-size="13" fill="#334155">고주파 전류</text>
  <text x="330" y="233" text-anchor="middle" font-size="13" fill="#334155">공급 방해</text>

  <rect x="445" y="155" width="140" height="86" rx="18" fill="#fefce8" stroke="#fde047"/>
  <text x="515" y="187" text-anchor="middle" font-size="18" font-weight="700" fill="#a16207">누설전류</text>
  <text x="515" y="214" text-anchor="middle" font-size="13" fill="#334155">DC 전압에서</text>
  <text x="515" y="233" text-anchor="middle" font-size="13" fill="#334155">새는 전류</text>

  <rect x="630" y="155" width="140" height="86" rx="18" fill="#fdf2f8" stroke="#f9a8d4"/>
  <text x="700" y="187" text-anchor="middle" font-size="18" font-weight="700" fill="#be185d">유전손실</text>
  <text x="700" y="214" text-anchor="middle" font-size="13" fill="#334155">tanδ</text>
  <text x="700" y="233" text-anchor="middle" font-size="13" fill="#334155">AC 열손실</text>

  <path d="M145 255 C240 305, 620 305, 700 255" fill="none" stroke="url(#g1)" stroke-width="6" stroke-linecap="round"/>
  <text x="430" y="298" text-anchor="middle" font-size="18" font-weight="800" fill="#0f172a">손실이 작을수록 발열↓ · 전압노이즈↓ · 전압마진↓</text>
</svg>
</div>

실제 손실은 대략 이렇게 볼 수 있습니다.

```text
Ptotal ≈ Irms² · ESR + Vdc · Ileak + Pac,dielectric
```

따라서 “전기를 덜 먹는 캐패시터”라는 표현은 정확히는 **동일 조건에서 전력손실·발열·전원노이즈가 작은 캐패시터**라는 뜻입니다.

---

## 2. MLCC가 AI 서버에서 중요한 이유

MLCC는 Multi-Layer Ceramic Capacitor, 적층세라믹캐패시터입니다. 세라믹 유전체와 내부전극을 여러 층 쌓아 작은 부피에 큰 정전용량을 만듭니다.

MLCC의 장점은 분명합니다.

- ESR이 낮습니다.
- ESL이 낮습니다.
- 고주파 디커플링에 강합니다.
- 누설전류가 낮은 편입니다.
- 작은 사이즈로 많이 배치할 수 있습니다.
- 서버·스마트폰·전장·산업기기 어디에나 들어갑니다.

GPU나 CPU가 순간적으로 전류를 확 당기면 전압이 푹 꺼질 수 있습니다. 이걸 voltage droop라고 합니다. MLCC는 칩 근처에서 순간 전류를 공급해서 전압 흔들림을 막습니다.

```text
전압노이즈 ≈ L · di/dt
```

여기서 `L`은 루프 인덕턴스입니다. 부품이 칩에서 멀수록, 배선이 길수록 커집니다. 그래서 작고 가까이 붙일 수 있는 MLCC가 강합니다.

다만 MLCC에도 약점이 있습니다. 특히 X5R/X7R 같은 Class II MLCC는 DC 전압이 걸리면 실제 용량이 줄어듭니다. 명목 10µF여도 실제 동작 전압에서는 3~5µF처럼 동작할 수 있습니다. 따라서 설계자는 정격 용량이 아니라 **동작 전압에서의 유효 용량**을 봐야 합니다.

---

## 3. 실리콘캐패시터는 왜 비싼데 쓰나

실리콘캐패시터는 실리콘 웨이퍼 기반으로 만든 캐패시터입니다. MOS/MIM/trench 구조 등을 이용해 실리콘 안에 정밀한 캐패시터를 만듭니다.

삼성전기 공식 제품 페이지 기준으로 실리콘캐패시터는:

- 실리콘 위에 유전체와 내부전극을 쌓아 캐패시터를 형성합니다.
- wafer grinding으로 **100µm 이하 두께**까지 얇게 만들 수 있습니다.
- 패키지 내부 적용이 가능합니다.
- **Low ESL**이 전원 안정성에 유리합니다.

핵심은 “가까움”입니다. 이걸 가장 쉽게 보면 **MLCC는 보드 위에 붙고, 실리콘캐패시터는 패키지 안으로 들어갈 수 있다**는 차이입니다.

### 보드 위 MLCC와 패키지 안 실리콘캐패시터의 차이

AI 가속기 보드를 위에서 본다고 생각해봅시다.

- 기존 MLCC: GPU 패키지 주변의 **PCB 보드 위**에 붙습니다.
- 실리콘캐패시터: GPU/HBM 패키지의 **기판 안, 인터포저 근처, 칩 바로 아래/옆**까지 들어갈 수 있습니다.

즉 MLCC는 “집 밖 마당에 있는 비상 배터리”에 가깝고, 실리콘캐패시터는 “방 안 책상 옆에 붙여둔 비상 배터리”에 가깝습니다. 둘 다 전기를 도와주지만, 순간적으로 필요할 때는 가까운 쪽이 훨씬 빠릅니다.

<div style="border:1px solid #e5e7eb;border-radius:18px;padding:18px;margin:24px 0;background:#f8fafc;overflow-x:auto">
<svg width="920" height="500" viewBox="0 0 920 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="보드 위 MLCC와 패키지 안 실리콘캐패시터 실장 위치 비교">
  <defs>
    <marker id="arrowNear" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#0f766e"/></marker>
    <marker id="arrowFar" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#dc2626"/></marker>
  </defs>

  <text x="460" y="42" text-anchor="middle" font-size="27" font-weight="900" fill="#0f172a">왜 실리콘캐패시터가 더 가까울 수 있나?</text>
  <text x="460" y="72" text-anchor="middle" font-size="15" fill="#475569">MLCC는 PCB 보드 위, 실리콘캐패시터는 패키지 안쪽까지 들어갈 수 있다</text>

  <rect x="55" y="130" width="810" height="250" rx="28" fill="#dbeafe" stroke="#60a5fa" stroke-width="3"/>
  <text x="92" y="162" font-size="18" font-weight="900" fill="#1e3a8a">PCB 보드</text>

  <rect x="295" y="165" width="330" height="170" rx="22" fill="#e2e8f0" stroke="#64748b" stroke-width="3"/>
  <text x="460" y="192" text-anchor="middle" font-size="18" font-weight="900" fill="#334155">GPU/HBM 패키지 기판</text>

  <rect x="352" y="215" width="95" height="68" rx="12" fill="#fee2e2" stroke="#ef4444" stroke-width="3"/>
  <text x="399" y="244" text-anchor="middle" font-size="18" font-weight="900" fill="#991b1b">GPU</text>
  <text x="399" y="266" text-anchor="middle" font-size="12" fill="#7f1d1d">전류 급변</text>

  <rect x="478" y="215" width="95" height="68" rx="12" fill="#fef3c7" stroke="#f59e0b" stroke-width="3"/>
  <text x="525" y="244" text-anchor="middle" font-size="18" font-weight="900" fill="#92400e">HBM</text>
  <text x="525" y="266" text-anchor="middle" font-size="12" fill="#78350f">초고속 메모리</text>

  <rect x="335" y="305" width="250" height="18" rx="9" fill="#94a3b8"/>
  <text x="460" y="354" text-anchor="middle" font-size="13" fill="#475569">패키지 내부 배선/인터포저/기판</text>

  <rect x="170" y="198" width="62" height="36" rx="8" fill="#fef9c3" stroke="#ca8a04" stroke-width="3"/>
  <text x="201" y="221" text-anchor="middle" font-size="14" font-weight="900" fill="#854d0e">MLCC</text>
  <rect x="700" y="198" width="62" height="36" rx="8" fill="#fef9c3" stroke="#ca8a04" stroke-width="3"/>
  <text x="731" y="221" text-anchor="middle" font-size="14" font-weight="900" fill="#854d0e">MLCC</text>

  <rect x="416" y="290" width="88" height="32" rx="8" fill="#fae8ff" stroke="#a855f7" stroke-width="3"/>
  <text x="460" y="311" text-anchor="middle" font-size="13" font-weight="900" fill="#6b21a8">실리콘C</text>

  <path d="M201 216 C260 205, 305 210, 352 236" fill="none" stroke="#dc2626" stroke-width="5" stroke-dasharray="10 8" marker-end="url(#arrowFar)"/>
  <text x="255" y="185" text-anchor="middle" font-size="14" font-weight="800" fill="#b91c1c">보드 배선 경유</text>
  <text x="255" y="250" text-anchor="middle" font-size="13" fill="#991b1b">길다 → 루프 인덕턴스↑</text>

  <path d="M460 290 C448 278, 432 265, 410 250" fill="none" stroke="#0f766e" stroke-width="6" marker-end="url(#arrowNear)"/>
  <text x="575" y="305" font-size="14" font-weight="900" fill="#0f766e">패키지 안에서 바로 공급</text>
  <text x="575" y="327" font-size="13" fill="#115e59">짧다 → ESL/노이즈↓</text>

  <rect x="100" y="405" width="330" height="58" rx="16" fill="white" stroke="#fecaca" stroke-width="2"/>
  <text x="265" y="429" text-anchor="middle" font-size="15" font-weight="900" fill="#991b1b">MLCC 경로</text>
  <text x="265" y="451" text-anchor="middle" font-size="13" fill="#475569">보드 패턴 + 비아 + 패키지 기판을 거쳐 칩까지 간다</text>

  <rect x="490" y="405" width="330" height="58" rx="16" fill="white" stroke="#99f6e4" stroke-width="2"/>
  <text x="655" y="429" text-anchor="middle" font-size="15" font-weight="900" fill="#0f766e">실리콘캐패시터 경로</text>
  <text x="655" y="451" text-anchor="middle" font-size="13" fill="#475569">패키지 내부에서 칩 근처에 붙어 순간 전류를 준다</text>
</svg>
</div>

위 그림이 “위에서 본 배치”라면, 아래는 **옆에서 자른 단면도**입니다. 이 그림이 핵심입니다. MLCC는 PCB 표면에 납땜되어 있고, GPU까지 가려면 보드 배선과 비아, 패키지 범프를 거칩니다. 반면 실리콘캐패시터는 패키지 기판 안쪽이나 칩 바로 아래쪽에 붙을 수 있어 전류 루프가 훨씬 짧습니다.

<div style="border:1px solid #e5e7eb;border-radius:18px;padding:18px;margin:24px 0;background:#ffffff;overflow-x:auto">
<svg width="940" height="560" viewBox="0 0 940 560" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="PCB 보드 단면에서 MLCC와 실리콘캐패시터 실장 위치 비교">
  <defs>
    <marker id="redArrowCross" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#dc2626"/></marker>
    <marker id="greenArrowCross" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#059669"/></marker>
    <linearGradient id="pcbLayer" x1="0" x2="1"><stop offset="0" stop-color="#bfdbfe"/><stop offset="1" stop-color="#93c5fd"/></linearGradient>
    <linearGradient id="pkgLayer" x1="0" x2="1"><stop offset="0" stop-color="#e5e7eb"/><stop offset="1" stop-color="#cbd5e1"/></linearGradient>
  </defs>

  <text x="470" y="42" text-anchor="middle" font-size="27" font-weight="900" fill="#0f172a">PCB/패키지 단면 비교: 누가 GPU에 더 가까운가?</text>
  <text x="470" y="72" text-anchor="middle" font-size="15" fill="#475569">노란 MLCC는 보드 표면, 보라색 실리콘캐패시터는 패키지 내부/칩 아래쪽</text>

  <rect x="60" y="400" width="820" height="72" rx="12" fill="url(#pcbLayer)" stroke="#2563eb" stroke-width="3"/>
  <text x="92" y="443" font-size="18" font-weight="900" fill="#1e3a8a">PCB 보드</text>
  <line x1="220" y1="418" x2="840" y2="418" stroke="#1d4ed8" stroke-width="4" opacity="0.35"/>
  <line x1="220" y1="438" x2="840" y2="438" stroke="#1d4ed8" stroke-width="3" opacity="0.25"/>
  <line x1="220" y1="456" x2="840" y2="456" stroke="#1d4ed8" stroke-width="3" opacity="0.25"/>
  <text x="520" y="493" text-anchor="middle" font-size="13" fill="#475569">PCB 내부 구리 배선층: 전류가 돌아가는 길이 길수록 기생 인덕턴스가 커진다</text>

  <rect x="300" y="262" width="360" height="96" rx="14" fill="url(#pkgLayer)" stroke="#64748b" stroke-width="3"/>
  <text x="480" y="292" text-anchor="middle" font-size="18" font-weight="900" fill="#334155">패키지 기판 / 인터포저 영역</text>
  <line x1="330" y1="322" x2="630" y2="322" stroke="#64748b" stroke-width="4" opacity="0.4"/>
  <line x1="330" y1="342" x2="630" y2="342" stroke="#64748b" stroke-width="3" opacity="0.3"/>

  <rect x="365" y="136" width="112" height="74" rx="12" fill="#fee2e2" stroke="#ef4444" stroke-width="3"/>
  <text x="421" y="168" text-anchor="middle" font-size="20" font-weight="900" fill="#991b1b">GPU</text>
  <text x="421" y="192" text-anchor="middle" font-size="12" fill="#7f1d1d">전류 급변</text>

  <rect x="505" y="136" width="98" height="74" rx="12" fill="#fef3c7" stroke="#f59e0b" stroke-width="3"/>
  <text x="554" y="168" text-anchor="middle" font-size="20" font-weight="900" fill="#92400e">HBM</text>
  <text x="554" y="192" text-anchor="middle" font-size="12" fill="#78350f">메모리</text>

  <line x1="385" y1="210" x2="385" y2="262" stroke="#475569" stroke-width="5"/>
  <line x1="421" y1="210" x2="421" y2="262" stroke="#475569" stroke-width="5"/>
  <line x1="457" y1="210" x2="457" y2="262" stroke="#475569" stroke-width="5"/>
  <text x="278" y="244" font-size="13" fill="#475569">마이크로범프/접속부</text>

  <rect x="425" y="232" width="110" height="28" rx="7" fill="#fae8ff" stroke="#a855f7" stroke-width="3"/>
  <text x="480" y="251" text-anchor="middle" font-size="13" font-weight="900" fill="#6b21a8">실리콘캐패시터</text>
  <text x="480" y="224" text-anchor="middle" font-size="13" font-weight="800" fill="#6b21a8">패키지 안, 칩 바로 아래/옆</text>

  <rect x="135" y="356" width="82" height="38" rx="8" fill="#fef9c3" stroke="#ca8a04" stroke-width="3"/>
  <text x="176" y="380" text-anchor="middle" font-size="15" font-weight="900" fill="#854d0e">MLCC</text>
  <text x="176" y="338" text-anchor="middle" font-size="13" font-weight="800" fill="#854d0e">PCB 표면 실장</text>

  <circle cx="250" cy="400" r="7" fill="#1d4ed8"/>
  <circle cx="300" cy="400" r="7" fill="#1d4ed8"/>
  <circle cx="350" cy="400" r="7" fill="#1d4ed8"/>
  <circle cx="410" cy="358" r="6" fill="#64748b"/>
  <line x1="250" y1="400" x2="250" y2="358" stroke="#1d4ed8" stroke-width="4" stroke-dasharray="5 5"/>
  <line x1="300" y1="400" x2="300" y2="358" stroke="#1d4ed8" stroke-width="4" stroke-dasharray="5 5"/>
  <line x1="350" y1="400" x2="350" y2="358" stroke="#1d4ed8" stroke-width="4" stroke-dasharray="5 5"/>
  <text x="287" y="384" text-anchor="middle" font-size="12" fill="#1e40af">비아</text>

  <path d="M176 356 C210 330, 250 320, 300 340 C350 365, 365 300, 421 210" fill="none" stroke="#dc2626" stroke-width="6" stroke-dasharray="12 8" marker-end="url(#redArrowCross)"/>
  <text x="170" y="280" font-size="15" font-weight="900" fill="#b91c1c">MLCC 전류 경로</text>
  <text x="170" y="303" font-size="13" fill="#991b1b">보드 위 → PCB 배선/비아 → 패키지 → GPU</text>
  <text x="170" y="324" font-size="13" fill="#991b1b">길고 돌아간다 = 루프 인덕턴스↑</text>

  <path d="M480 232 C462 216, 445 202, 421 180" fill="none" stroke="#059669" stroke-width="7" marker-end="url(#greenArrowCross)"/>
  <text x="590" y="238" font-size="15" font-weight="900" fill="#047857">실리콘C 전류 경로</text>
  <text x="590" y="261" font-size="13" fill="#065f46">패키지 안 → GPU 바로 옆</text>
  <text x="590" y="282" font-size="13" fill="#065f46">짧고 작다 = ESL↓, droop↓</text>

  <rect x="80" y="94" width="255" height="78" rx="16" fill="#fff7ed" stroke="#fb923c" stroke-width="2"/>
  <text x="207" y="122" text-anchor="middle" font-size="15" font-weight="900" fill="#9a3412">비유</text>
  <text x="207" y="146" text-anchor="middle" font-size="13" fill="#7c2d12">MLCC = 집 밖 마당 비상배터리</text>
  <text x="207" y="164" text-anchor="middle" font-size="13" fill="#7c2d12">실리콘C = 책상 옆 비상배터리</text>

  <rect x="665" y="345" width="205" height="92" rx="16" fill="#ecfdf5" stroke="#34d399" stroke-width="2"/>
  <text x="767" y="373" text-anchor="middle" font-size="15" font-weight="900" fill="#047857">얻는 이점</text>
  <text x="767" y="397" text-anchor="middle" font-size="13" fill="#065f46">순간 전류 대응↑</text>
  <text x="767" y="416" text-anchor="middle" font-size="13" fill="#065f46">전압 흔들림↓</text>
  <text x="767" y="435" text-anchor="middle" font-size="13" fill="#065f46">전압 마진/발열↓</text>
</svg>
</div>

이 단면도를 보면 “왜 비싼 실리콘캐패시터를 굳이 쓰는가”가 더 명확해집니다. AI GPU 입장에서는 **멀리 있는 큰 물탱크**보다 **바로 옆 작은 물통**이 순간 압력 저하를 더 빨리 막아줍니다. MLCC는 여전히 보드 전체를 받치는 주력이고, 실리콘캐패시터는 칩 바로 옆에서 마지막 순간 전압을 지키는 부품입니다.

여기서 중요한 것은 **거리 자체**보다, 그 거리 때문에 생기는 **기생 인덕턴스**입니다. 전류가 지나가는 길은 모두 아주 작은 코일처럼 행동합니다. 길이 길고, 비아를 많이 지나고, 루프 면적이 커질수록 인덕턴스가 커집니다.

```text
전압 흔들림 ≈ L · di/dt
```

AI GPU는 `di/dt`, 즉 “전류가 변하는 속도”가 매우 큽니다. 순간적으로 수십~수백 A가 왔다 갔다 합니다. 그래서 `L`이 조금만 커져도 전압이 흔들립니다.

실리콘캐패시터가 패키지 안으로 들어가면 얻는 이점은 단순합니다.

1. **전류 공급 경로가 짧아집니다.**  
   보드 위 MLCC에서 칩까지 가는 긴 길을 줄입니다.

2. **ESL, 즉 기생 인덕턴스가 낮아집니다.**  
   고주파 순간 전류에 더 빨리 반응합니다.

3. **전압 droop와 ripple이 줄어듭니다.**  
   GPU/HBM이 순간적으로 전류를 먹어도 전압이 덜 꺼집니다.

4. **전압 여유분을 줄일 수 있습니다.**  
   노이즈가 작으면 안정성을 위해 일부러 높게 주던 전압 마진을 낮출 수 있습니다.

5. **발열과 throttling 가능성이 낮아집니다.**  
   전압이 흔들려 성능을 낮추거나 오류가 나는 상황을 줄입니다.

6. **패키지/보드 설계 자유도가 커집니다.**  
   보드 위에 MLCC를 무한정 붙일 수 없기 때문에, 일부 기능을 패키지 안으로 가져가는 것이 고성능 AI 패키지에서는 유리합니다.

쉽게 말해 MLCC와 실리콘캐패시터는 경쟁이라기보다 역할 분담입니다.

- **MLCC**: 보드 전체와 중고주파 전원 안정화의 주력
- **실리콘캐패시터**: GPU/HBM 바로 옆 초고주파·초근접 전원 안정화의 특수부대

결론은 명확합니다.

> 실리콘캐패시터는 MLCC 전체를 대체하는 게 아니라, GPU/HBM/AI 패키지 주변의 초고성능 영역에서 MLCC를 보완하거나 일부 대체하는 고부가 부품입니다.

---

## 4. AI 서버 전원망을 그림으로 보면

AI 서버는 일반 서버보다 전력 밀도가 훨씬 높습니다. GPU, HBM, CPU, 고속 네트워크 ASIC, VRM, POL 전원부가 모두 빠르게 전류를 요구합니다.

<div style="border:1px solid #e5e7eb;border-radius:18px;padding:18px;margin:24px 0;background:#f8fafc;overflow-x:auto">
<svg width="900" height="420" viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AI 서버 전원망 계층도">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#334155"/></marker>
  </defs>
  <text x="450" y="42" text-anchor="middle" font-size="26" font-weight="900" fill="#0f172a">AI 서버 PDN: 캐패시터는 주파수별로 역할이 다르다</text>
  <text x="450" y="70" text-anchor="middle" font-size="15" fill="#475569">멀수록 저주파·대용량, 가까울수록 고주파·초저 ESL</text>

  <rect x="45" y="135" width="130" height="95" rx="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
  <text x="110" y="170" text-anchor="middle" font-size="17" font-weight="800" fill="#075985">48V/54V</text>
  <text x="110" y="196" text-anchor="middle" font-size="13" fill="#334155">랙 전원</text>

  <rect x="215" y="135" width="130" height="95" rx="18" fill="#dcfce7" stroke="#22c55e" stroke-width="2"/>
  <text x="280" y="170" text-anchor="middle" font-size="17" font-weight="800" fill="#166534">VRM/POL</text>
  <text x="280" y="196" text-anchor="middle" font-size="13" fill="#334155">전압 변환</text>

  <rect x="385" y="135" width="130" height="95" rx="18" fill="#fef9c3" stroke="#eab308" stroke-width="2"/>
  <text x="450" y="170" text-anchor="middle" font-size="17" font-weight="800" fill="#854d0e">MLCC</text>
  <text x="450" y="196" text-anchor="middle" font-size="13" fill="#334155">보드 근처</text>

  <rect x="555" y="135" width="150" height="95" rx="18" fill="#fae8ff" stroke="#c026d3" stroke-width="2"/>
  <text x="630" y="170" text-anchor="middle" font-size="17" font-weight="800" fill="#86198f">실리콘C</text>
  <text x="630" y="196" text-anchor="middle" font-size="13" fill="#334155">패키지 내부</text>

  <rect x="745" y="135" width="110" height="95" rx="18" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
  <text x="800" y="170" text-anchor="middle" font-size="17" font-weight="800" fill="#991b1b">GPU/HBM</text>
  <text x="800" y="196" text-anchor="middle" font-size="13" fill="#334155">초고속 부하</text>

  <line x1="175" y1="182" x2="215" y2="182" stroke="#334155" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="345" y1="182" x2="385" y2="182" stroke="#334155" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="515" y1="182" x2="555" y2="182" stroke="#334155" stroke-width="3" marker-end="url(#arrow)"/>
  <line x1="705" y1="182" x2="745" y2="182" stroke="#334155" stroke-width="3" marker-end="url(#arrow)"/>

  <rect x="80" y="285" width="220" height="62" rx="16" fill="white" stroke="#cbd5e1"/>
  <text x="190" y="310" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">저주파·대용량</text>
  <text x="190" y="333" text-anchor="middle" font-size="13" fill="#475569">Bulk capacitor / 전원 저장</text>

  <rect x="340" y="285" width="220" height="62" rx="16" fill="white" stroke="#cbd5e1"/>
  <text x="450" y="310" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">중고주파</text>
  <text x="450" y="333" text-anchor="middle" font-size="13" fill="#475569">MLCC / 보드 디커플링</text>

  <rect x="600" y="285" width="220" height="62" rx="16" fill="white" stroke="#cbd5e1"/>
  <text x="710" y="310" text-anchor="middle" font-size="15" font-weight="800" fill="#0f172a">초고주파·초근접</text>
  <text x="710" y="333" text-anchor="middle" font-size="13" fill="#475569">실리콘C / 패키지 디커플링</text>
</svg>
</div>

AI 서버 PDN의 핵심 목표는 넓은 주파수 범위에서 낮은 임피던스를 유지하는 것입니다.

```text
목표 임피던스 Ztarget ≈ 허용 전압 변동 / 부하 전류 변동
```

예를 들어 허용 droop가 20mV이고 transient가 100A면 목표 임피던스는 0.2mΩ 수준입니다. 매우 빡센 조건입니다.

---

## 5. 데이터센터에서 실제로 유리한 지점

### 전압 droop/ripple 감소

GPU/HBM은 전압이 순간적으로 흔들리면 오류, throttling, reset, ECC error, timing violation이 생길 수 있습니다. MLCC와 실리콘캐패시터는 이 흔들림을 줄입니다.

### 전압 마진 축소 가능

AI 칩은 안정성을 위해 실제 필요 전압보다 높게 공급하는 경우가 많습니다. 이 여유분을 guardband라고 보면 됩니다. PDN이 좋아지면 guardband를 줄일 수 있습니다.

동적전력은 대략 전압의 제곱에 비례합니다.

```text
Pdynamic ∝ C · V² · f
```

0.80V rail에서 전압을 낮출 때 계산 예시는 다음과 같습니다.

- 10mV 절감: 동적전력 약 2.48% 감소 여지
- 20mV 절감: 동적전력 약 4.94% 감소 여지
- 30mV 절감: 동적전력 약 7.36% 감소 여지
- 50mV 절감: 동적전력 약 12.11% 감소 여지

물론 실제 서버 전체 전력 절감률은 해당 rail의 전력 비중과 workload에 따라 달라집니다. 그래도 방향은 분명합니다.

> 캐패시터가 직접 전기를 아끼는 게 아니라, 더 낮은 전압에서도 안정 동작하게 만들어 전력을 줄일 수 있게 합니다.

### ESR 손실 감소

리플전류 손실은 간단합니다.

```text
P = Irms² · ESR
```

리플전류 10A일 때:

- ESR 100mΩ: 10W 손실
- ESR 10mΩ: 1W 손실
- ESR 1mΩ: 0.1W 손실

ESR이 낮을수록 캐패시터 자체 발열이 줄고, 주변 전원부 hotspot도 줄어듭니다.

### 보드 면적과 패키지 공간 절약

AI 서버 보드는 GPU, HBM, VRM, 커넥터, 냉각 구조 때문에 빽빽합니다. MLCC는 작아서 보드에 많이 배치 가능하고, 실리콘캐패시터는 패키지 내부로 들어갈 수 있습니다.

이건 단순 면적 절약이 아니라 액체냉각 설계 자유도, 전원 경로 단축, 서버 밀도 증가, 신호 무결성 개선으로 이어질 수 있습니다.

---

## 6. 삼성전기에서 제일 중요한 이벤트

삼성전기 공식 뉴스룸 기준으로 2026년 5월 20일에 다음 내용이 나왔습니다.

- **실리콘캐패시터 공급계약 약 1.5조원**
- 계약기간: **2027-01-01~2028-12-31**
- 단순 연평균: **약 7,500억원/년**
- 적용처: **AI 서버용 GPU, HBM 같은 고성능 반도체 패키지 내부**
- 역할: 전원 공급 안정성 향상
- 회사 설명: 기존 MLCC 대비 **ESL/ESR 저항이 100배 이상 낮아** 고성능 반도체의 signal loss를 최소화

이건 단순 “미래 기술 개발”이 아니라 **상업화·고객 인증·대형 공급망 진입**이 공식 확인된 이벤트입니다.

계약 1.5조원 / 2년 = 단순 연평균 7,500억원입니다.

삼성전기 연매출을 10~12조원대로 가정하면:

- 10조원 매출 대비: 7.5%
- 11조원 매출 대비: 6.82%
- 12조원 매출 대비: 6.25%

단일 신규 제품군 계약으로는 작지 않습니다. 다만 실제 매출 인식, 마진, 고객 집중도, 추가 수주 여부는 별도로 확인해야 합니다.

---

## 7. 투자 포인트를 그림으로 정리

<div style="border:1px solid #e5e7eb;border-radius:18px;padding:18px;margin:24px 0;background:#fff7ed;overflow-x:auto">
<svg width="900" height="420" viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="삼성전기 투자 포인트 맵">
  <text x="450" y="44" text-anchor="middle" font-size="26" font-weight="900" fill="#111827">삼성전기 리서치 포인트: MLCC에서 AI 패키지 부품으로</text>
  <circle cx="450" cy="205" r="78" fill="#1e293b"/>
  <text x="450" y="190" text-anchor="middle" font-size="20" font-weight="900" fill="white">삼성전기</text>
  <text x="450" y="218" text-anchor="middle" font-size="14" fill="#cbd5e1">수동부품 + 패키지 역량</text>

  <rect x="70" y="105" width="220" height="90" rx="20" fill="white" stroke="#f97316" stroke-width="3"/>
  <text x="180" y="138" text-anchor="middle" font-size="18" font-weight="900" fill="#9a3412">기존 MLCC</text>
  <text x="180" y="165" text-anchor="middle" font-size="13" fill="#334155">IT·전장·서버 보드</text>
  <text x="180" y="184" text-anchor="middle" font-size="13" fill="#334155">고부가 믹스 개선</text>

  <rect x="610" y="105" width="220" height="90" rx="20" fill="white" stroke="#7c3aed" stroke-width="3"/>
  <text x="720" y="138" text-anchor="middle" font-size="18" font-weight="900" fill="#5b21b6">실리콘캐패시터</text>
  <text x="720" y="165" text-anchor="middle" font-size="13" fill="#334155">GPU/HBM 패키지 내부</text>
  <text x="720" y="184" text-anchor="middle" font-size="13" fill="#334155">1.5조원 계약</text>

  <rect x="70" y="255" width="220" height="90" rx="20" fill="white" stroke="#0ea5e9" stroke-width="3"/>
  <text x="180" y="288" text-anchor="middle" font-size="18" font-weight="900" fill="#075985">AI 서버 수요</text>
  <text x="180" y="315" text-anchor="middle" font-size="13" fill="#334155">고전력·고속·고집적</text>
  <text x="180" y="334" text-anchor="middle" font-size="13" fill="#334155">전원 안정성 중요</text>

  <rect x="610" y="255" width="220" height="90" rx="20" fill="white" stroke="#ef4444" stroke-width="3"/>
  <text x="720" y="288" text-anchor="middle" font-size="18" font-weight="900" fill="#991b1b">확인 리스크</text>
  <text x="720" y="315" text-anchor="middle" font-size="13" fill="#334155">수율·마진·추가 고객</text>
  <text x="720" y="334" text-anchor="middle" font-size="13" fill="#334155">MLCC 사이클</text>

  <line x1="290" y1="150" x2="375" y2="185" stroke="#64748b" stroke-width="3"/>
  <line x1="610" y1="150" x2="525" y2="185" stroke="#64748b" stroke-width="3"/>
  <line x1="290" y1="300" x2="375" y2="225" stroke="#64748b" stroke-width="3"/>
  <line x1="610" y1="300" x2="525" y2="225" stroke="#64748b" stroke-width="3"/>
</svg>
</div>

삼성전기를 볼 때 이제 축은 세 개입니다.

1. 기존 MLCC 업황 회복
2. 전장·서버 고부가 MLCC 믹스 상승
3. 실리콘캐패시터의 AI 패키지 공급망 진입과 추가 수주

---

## 8. 조심할 점

좋은 이야기만 보면 안 됩니다.

- MLCC는 여전히 재고·가격 사이클 산업입니다.
- Murata, TDK 등 일본 업체의 기술·고객 기반이 강합니다.
- 중국·대만 업체의 범용품 가격 경쟁이 있습니다.
- 실리콘캐패시터는 MLCC 전체 대체재가 아니라 고성능 보완재입니다.
- 1.5조원 계약의 실제 마진·수율·고객 집중도는 추가 확인이 필요합니다.
- 매출 인식은 2027~2028년 중심이라 단기 실적보다 중장기 옵션 성격이 강합니다.

---

## 최종 판단

삼성전기 MLCC 스토리는 이제 “스마트폰 회복”만으로 보면 부족합니다. AI 서버는 고전력·고속·고집적 구조 때문에 전원 안정화 부품의 중요도를 끌어올립니다. MLCC는 보드 레벨의 핵심이고, 실리콘캐패시터는 패키지 내부 고부가 영역을 담당합니다.

가격이 비싸도 쓰는 이유는 단순합니다.

- 전압 흔들림을 줄입니다.
- 전압마진을 줄일 수 있습니다.
- 성능/Watt를 높입니다.
- 오류와 throttling을 줄입니다.
- 패키지/보드 공간을 아낍니다.
- AI 서버의 전력밀도 문제를 완화합니다.

삼성전기가 1.5조원 규모 실리콘캐패시터 계약을 따낸 것은 이 변화가 이미 상업화 단계에 들어갔다는 신호입니다. 다만 2027~2028년 매출 인식, 마진, 추가 고객, 수율, 경쟁사 대응을 계속 확인해야 합니다.

## 참고 출처

- Samsung Electro-Mechanics, MLCC product page
- Samsung Electro-Mechanics, Silicon Capacitor product page
- Samsung Electro-Mechanics Newsroom, 2026-05-20, “Samsung Electro-Mechanics Signs 1.5 Trillion KRW Silicon Capacitor Supply Contract with Global Large-Scale Company”
- Murata, Silicon Capacitors / IPDiA product resources
- TDK, MLCC decoupling and capacitor application resources
- JEDEC HBM standard overview
- NVIDIA/AMD data center accelerator public materials
