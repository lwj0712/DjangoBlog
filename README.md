# 목표

# WBS

```mermaid
gantt
    title Django 블로그 프로젝트 개발 일정
    dateFormat  YYYY-MM-DD

    section 기획
    WBS 작성 :2024-08-26, 1d
    아이디어 기획 :2024-08-26, 2d
    와이어 프레임 작성 :2024-08-26, 2d
    ERD 작성 :2024-08-27, 1d

    section 개발
    URL 패턴 정의 :2024-08-27, 1d
    모델 설계 :2024-08-27, 1d
    CBV 구현 :2024-08-27, 2d
    CRUD 구현 :2024-08-28, 2d
    사용자 인증 :2024-08-29, 2d
    추가 기능 구현 :2024-08-29, 2d
    테스트 및 배포:2024-08-30, 1d

    section 문서 작성
    README 작성 :2024-08-30, 2d

    section 발표 준비
    발표 준비 :2024-09-01, 1d
```


# ERD

```mermaid

erDiagram
    User ||--|| Profile : has
    User ||--o{ Post : writes
    User ||--o{ Comment : writes
    User ||--o{ Like : gives
    Post ||--o{ Comment : has
    Post ||--o{ Like : receives
    Post }o--o| Category : belongs_to
    Comment ||--o{ Comment : has_reply

    User {
        int id PK
        string username
        string password
        string email
        datetime date_joined
    }

    Profile {
        int id PK
        int user_id FK
        string display_name
        string name
        string email
        string bio
        string profile_image
    }

    Post {
        int id PK
        int user_id FK
        int category_id FK
        string title
        text content
        string image
        datetime created_at
        datetime updated_at
    }

    Category {
        int id PK
        string name
    }

    Comment {
        int id PK
        int user_id FK
        int post_id FK
        int parent_comment_id FK
        text content
        datetime created_at
    }

    Like {
        int id PK
        int user_id FK
        int post_id FK
    } 

```

# 명세
| App      | URL Pattern                    | View                       | Description                     |
| -------- | ------------------------------ | -------------------------- | ------------------------------- |
| config   | /admin/                         | admin.site            | Django admin        |
| config   | /                        | MainPageView            | 메인페이지        |
| config   | blog/                        | blog url            | 블로그 url        |
| config   | accounts/                        | accounts url            | 계정 관련 url        |
| blog     | blog/                             | PostListView               | 블로그 게시물 목록              |
| blog     | blog/search/<str:tag>                        | PostSearchView                 | 제목, 내용, 글쓴이 중에 선택하여 검색               |
| blog     | blog/<int:id>                      | PostDetailView             | 블로그 게시물 상세              |
| blog     | blog/write                        | PostCreateView             | 블로그 게시물 생성              |
| blog     | blog/edit/<int:id>               | PostUpdateView             | 블로그 게시물 수정          |
| blog     | blog/delete/<int:id>               | PostDeleteView             | 블로그 게시물 삭제              |
| accounts | accounts/login                      | CustomLoginView               | 사용자 로그인                     |
| accounts | accounts/logout                      | LogoutView               | 사용자 로그아웃                     |
| accounts | accounts/register/                      | SignUpView               | 사용자 등록                     |
| accounts | accounts/edit                      | UserProfileUpdateView               | 사용자 정보 수정                     |
| accounts | accounts/password_change                        | CustomPasswordChangeView            | 비밀번호 변경                   |


# 와이어 프레임

[Figma URL](https://www.figma.com/design/teJ06xvveV1K8VuVuRbss0/Untitled?node-id=0-1&t=5dxv9WNU6DnQAgnH-0)

# 화면 설계
![main](https://github.com/user-attachments/assets/05e89b5c-c006-4ee8-b6d9-158648c5beae)
![login](https://github.com/user-attachments/assets/f0ee4c9d-fad6-412d-a14e-028a0569fd83)
![register](https://github.com/user-attachments/assets/20055c76-6bff-4680-a868-b39e0b79be45)
![post_list(not_logged_in)](https://github.com/user-attachments/assets/97fd1ea2-198c-4c55-b5a4-2d02a7b0c49e)
![post_list](https://github.com/user-attachments/assets/4489777d-0bf5-48eb-b25b-a72e2dc3019c)
