# RhythmTag🕺
태그를 포함하여 노래를 추천하고 공유하는 음악블로그

---

## 1️⃣ 프로젝트 개요
RhythmTag는 YouTube 링크를 기반으로 사용자가 노래를 추천하고,  
태그와 함께 공유하며, 다른 사용자의 추천곡을 탐색할 수 있는  
인스타그램형 음악 블로그 커뮤니티입니다.

주요 기능:
- YouTube 링크를 통한 노래 공유
- 태그 기반 곡 분류 및 탐색
- 댓글, 좋아요 기능
- 모바일 반응형 UI

---

## 2️⃣ 기술 스택
- **Frontend:** HTML, CSS, JavaScript (Vanilla / Bootstrap)
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Etc:** GitHub, Figma, YouTube API

---

## 3️⃣ 프로젝트 실행 방법
# 가상환경 실행
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
python manage.py runserver

--- 

## 4️⃣ 기능 구성
* 회원가입 / 로그인 / 로그아웃
* 게시글 작성 / 수정 / 삭제 (YouTube 링크 포함)
* 태그 등록 / 검색
* 댓글 작성 / 삭제
* 좋아요
* 메인 피드 (최신 추천곡 리스트)
* 태그별 피드
* 팔로잉 / 팔로워 / 팔로잉삭제

---

# 5️⃣ ERD

---

# 6️⃣ URL 구성

---

# 7️⃣ WireFrame

---

# 8️⃣ 일정표 (WBS)
```mermaid
gantt
    title RhythmTag 프로젝트 일정 (2025-07-02 ~ 2025-07-09)
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d

    section 요구사항 및 설계
    프로젝트 개요 정의      :a1, 2025-07-02, 1d
    ERD/Wireframe 설계      :a2, 2025-07-02, 1d

    section 백엔드 개발 (Django / PostgreSQL / Python)
    Django 프로젝트 생성   :b1, 2025-07-03, 0.5d
    회원가입/로그인 구현    :b2, 2025-07-03, 0.5d
    게시글 CRUD            :b3, 2025-07-04, 1d
    댓글/좋아요/태그        :b4, 2025-07-05, 1d
    API / URL 구성          :b5, 2025-07-06, 0.5d

    section 프론트엔드 개발 (HTML / CSS / JS)
    기본 레이아웃 + 메인피드 :c1, 2025-07-03, 0.5d
    글 작성 / 상세 페이지   :c2, 2025-07-04, 1d
    댓글 / 태그 UI         :c3, 2025-07-05, 0.5d
    반응형/디자인 다듬기   :c4, 2025-07-06, 0.5d

    section 테스트 / 배포 / 회고
    통합 테스트            :d1, 2025-07-07, 0.5d
    배포                   :d2, 2025-07-07, 0.5d
    트러블슈팅 기록        :d3, 2025-07-08, 0.5d
    프로젝트 회고 작성     :d4, 2025-07-09, 0.5d
```

---

# 9️⃣ 시연 내용

---

# 🔟 트러블슈팅

---

# 1️⃣1️⃣ 프로젝트 진행하며 느낀 점
