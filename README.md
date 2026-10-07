# coupang link (PWA)

가족·지인 전용 쇼핑 링크입니다. 앱 설치 없이 **브라우저에서 홈 화면에 추가**만 하면 됩니다.
설치형 앱이 아니므로 Play 프로텍트·은행 앱 보안 경고 대상이 아닙니다.

## 사용법
1. 아래 주소를 휴대폰 브라우저에서 연다
2. 브라우저 메뉴(⋮ 또는 공유) → **홈 화면에 추가**
3. 아이콘이 생기면 눌러서 사용 (쿠팡으로 이동)

## 주소
- https://lifeporterlab.github.io/coupang-link/

## 대가성 표기
이 링크는 쿠팡 파트너스 활동의 일환으로, 이를 통한 구매 시 일정액의 수수료를 받을 수 있습니다.

## 파일
- `index.html` — 화면 (쿠팡으로 이동하는 버튼)
- `manifest.webmanifest` — PWA 설정 (이름·아이콘·standalone)
- `sw.js` — 오프라인 셸 캐시
- `icon-192.png` · `icon-512.png` · `icon-maskable-512.png` · `icon-180.png`

## 링크 변경
`index.html` 의 `URL_TARGET` 한 줄만 바꾸면 됩니다.
