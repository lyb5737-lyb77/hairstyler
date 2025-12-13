# GitHub Pages 배포 가이드

이 문서는 **AI 헤어 스타일러** 프로젝트를 GitHub Pages를 통해 무료로 배포하는 방법을 설명합니다.

> [!WARNING]
> **보안 주의사항**: 현재 코드(`index.html`)에 **Google Gemini API 키가 포함**되어 있습니다.
> GitHub에 코드를 올리면 **API 키가 전 세계에 공개**됩니다.
> 악의적인 사용자가 키를 도용하여 요금이 부과되거나 쿼리 한도가 소진될 수 있습니다.
>
> **권장 조치**:
> 1. 배포 후 테스트가 끝나면 즉시 API 키를 삭제하거나 재생성하세요.
> 2. 또는 Google Cloud Console에서 해당 API 키에 **HTTP 리퍼러 제한(HTTP Referrer restriction)**을 걸어, 본인의 GitHub Pages 주소(예: `https://your-id.github.io/*`)에서만 작동하도록 설정하세요.

---

## 1단계: GitHub 저장소 생성
1. [GitHub](https://github.com)에 로그인합니다.
2. 우측 상단의 `+` 아이콘을 누르고 **New repository**를 선택합니다.
3. **Repository name**에 `hairstyler` (또는 원하는 이름)를 입력합니다.
4. **Public** (공개)을 선택합니다.
5. **Create repository** 버튼을 클릭합니다.

## 2단계: 코드 업로드 (터미널 명령어)
VS Code의 터미널(Ctrl + `)을 열고 아래 명령어들을 순서대로 입력하세요.
(`YOUR_GITHUB_USERNAME` 부분을 본인의 깃허브 아이디로 바꿔야 합니다.)

```bash
# 1. 깃 초기화
git init

# 2. 모든 파일 스테이징
git add .

# 3. 커밋 (저장)
git commit -m "Initial commit: AI Hairstyler App"

# 4. 브랜치 이름 변경 (main)
git branch -M main

# 5. 원격 저장소 연결 (본인의 저장소 주소로 변경 필수!)
# 예: git remote add origin https://github.com/홍길동/hairstyler.git
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/hairstyler.git

# 6. 깃허브로 푸시 (업로드)
git push -u origin main
```

## 3단계: GitHub Pages 활성화
1. 방금 생성한 GitHub 저장소 페이지로 이동합니다.
2. 상단 메뉴의 **Settings** (설정) 탭을 클릭합니다.
3. 왼쪽 사이드바에서 **Pages** 메뉴를 클릭합니다.
4. **Build and deployment** 섹션의 **Branch** 항목에서:
   - `None`을 `main`으로 변경합니다.
   - 폴더는 `/(root)` 그대로 둡니다.
   - **Save** 버튼을 클릭합니다.

## 4단계: 배포 확인
1. 설정 저장 후 약 1~3분 정도 기다립니다.
2. 페이지 상단에 **"Your site is live at..."** 라는 메시지와 함께 링크가 나타납니다.
3. 해당 링크(예: `https://your-id.github.io/hairstyler/`)를 클릭하여 앱이 정상적으로 작동하는지 확인합니다.

---

### 문제 해결
- **이미지가 안 나와요**: 파일명 대소문자(`man.png` vs `Man.png`)가 정확한지 확인하세요. GitHub(리눅스 기반)는 대소문자를 엄격하게 구분합니다.
- **404 에러**: 배포가 완료될 때까지 시간이 조금 걸릴 수 있습니다. 5분 뒤에 다시 접속해보세요.
