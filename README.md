# MyBlog

<img src="static/README_images/django-logo.png" width="100%"/>

<br>

## 1. 프로젝트 목표

1. Django의 Class-Based Views를 활용하여 효율적이고 재사용 가능한 코드 구조 만들기
2. 사용자 친화적이고 반응형 디자인을 도입한 웹페이지
3. 보안성과 확장성을 고려한 백엔드 시스템 개발
4. 사용자 경험을 개선하는 다양한 기능 구현

<br>

## 2. 주요 기능

### 1. 사용자 관리 (CustomUser 모델)

- 회원가입 및 로그인/로그아웃 기능
    - django-recaptcha를 사용한 로봇 방지 기능
    - dnspython을 활용한 이메일 유효성 검사
- 로그인/로그아웃 기능
- 프로필 페이지 (프로필 사진 및 자기소개 포함)
- 사용자 정보 수정 기능

### 2. 블로그 포스트 관리

- 포스트 작성, 수정, 삭제 기능
- 이미지 업로드 지원
- 카테고리 분류 시스템
- 조회수 집계

### 3. 댓글 시스템

- 포스트에 대한 댓글 작성 기능
- 답글(중첩 댓글) 기능
- 댓글 삭제 기능
- soft 삭제 구현 (is_deleted 필드 활용)

### 4. 좋아요 기능

- 포스트 및 댓글에 대한 좋아요 기능
- 사용자당 포스트 하나에 한 번만 좋아요 가능 (unique_together 제약조건)

### 5. 카테고리 관리

- 동적 슬러그 생성을 통한 검색 친화적 URL 구조(slugify)
- 카테고리별 포스트 목록 제공

### 6. 검색 및 필터링

- 포스트 제목, 내용, 작성자 기반 검색 기능
- 카테고리별 필터링 기능

### 7. 페이지네이션

- 포스트 목록에 대한 페이지네이션 구현

### 8. 권한 관리

- 관리자, 작성자, 일반 사용자 등 역할별 권한 설정
- 객체 레벨 권한 구현 (예: 자신의 포스트만 수정/삭제 가능)

이 프로젝트를 통해 Django의 CBV 기능들을 활용하여 실제 운영 가능한 수준의 기능을 갖춘 블로그를 개발하는 것이 최종 목표입니다.

<br>

## 3. WBS

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
    추가 기능 구현 :2024-08-29, 3d
    테스트 :2024-08-30, 2d

    section 문서 작성
    README 작성 :2024-08-31, 2d

    section 발표 준비
    발표 준비 :2024-09-01, 1d
```

<br>

## 4. ERD

<img src="static/README_images/ERD.png" width="100%"/>

<br>

### 관계 설명

- CustomUser - Post : 1 대 N 관계
	- 한 사용자는 여러 개의 포스트를 작성할 수 있습니다.
	- Post.author_id가 CustomUser.id를 참조합니다.

- Category - Post : 1 대 N 관계
	- 한 카테고리는 여러 개의 포스트를 포함할 수 있습니다.
	- Post.category_id가 Category.id를 참조합니다.

- CustomUser - Comment: 1 대 N 관계
	- 한 사용자는 여러 개의 댓글을 작성할 수 있습니다.
	- Comment.author_id가 CustomUser.id를 참조합니다.

- Post - Comment: 1 대 N 관계
	- 한 포스트는 여러 개의 댓글을 가질 수 있습니다.
	- Comment.post_id가 Post.id를 참조합니다.

- Comment - Comment: 자기 참조 관계
	- 댓글은 다른 댓글의 답글이 될 수 있습니다.
	- Comment.parent_id가 Comment.id를 참조합니다.

- CustomUser - Like: 1 대 N 관계
	- 한 사용자는 여러 개의 좋아요를 할 수 있습니다.
	- Like.user_id가 CustomUser.id를 참조합니다.

- Post - Like: 1 대 N 관계
	- 한 포스트는 여러 개의 좋아요를 받을 수 있습니다.
	- Like.post_id가 Post.id를 참조합니다.

- Comment - Like: 1 대 N 관계
	- 한 댓글은 여러 개의 좋아요를 받을 수 있습니다.
  	- Like.comment_id가 Comment.id를 참조합니다.

<br>

## 5. URL 구조

| App      | URL Pattern                    | View                       | Description                     |
| -------- | ------------------------------ | -------------------------- | ------------------------------- |
| config   | /admin/                         | admin.site            | Django admin        |
| config   | /                        | MainPageView            | 메인페이지        |
| config   | blog/                        | blog url            | 블로그 url        |
| config   | accounts/                        | accounts url            | 계정 관련 url        |
| blog     | blog/                             | PostListView               | 블로그 포스트 목록              |
| blog     | blog/write                        | PostCreateView             | 블로그 포스트 생성              |
| blog     | blog/search/<str:tag>                        | PostSearchView                 | 게시물 검색               |
| blog     | blog/<int:pk>                      | PostDetailView             | 블로그 포스트 상세              |
| blog     | blog/edit/<int:pk>               | PostUpdateView             | 블로그 포스트 수정          |
| blog     | blog/delete/<int:pk>               | PostDeleteView             | 블로그 포스트 삭제              |
| blog     | blog/comment/<int:post_pk>/add/               | CommentCreateView             | 댓글 생성             |
| blog     | blog/comment/<int:comment_pk>/delete/               | CommentDeleteView              | 댓글 삭제              |
| blog     | blog/comment/<int:post_pk>/<int:comment_pk>/reply/               | CommentReplyView               | 답글 생성             |
| blog     | blog/post/<int:pk>/like/               | LikeToggleView               | 좋아요              |
| accounts | accounts/login                      | CustomLoginView               | 사용자 로그인                     |
| accounts | accounts/logout                      | LogoutView               | 사용자 로그아웃                     |
| accounts | accounts/register/                      | SignUpView               | 사용자 등록                     |
| accounts | accounts/edit                      | UserProfileUpdateView               | 사용자 정보 수정                     |
| accounts | accounts/password_change                        | CustomPasswordChangeView            | 비밀번호 변경                   |

<br>

## 6. 와이어 프레임 및 화면 설계 초안

[Figma URL](https://www.figma.com/design/teJ06xvveV1K8VuVuRbss0/Untitled?node-id=0-1&t=5dxv9WNU6DnQAgnH-0)

<table border="1" style="width:100%;">
  <colgroup>
    <col style="width: 50%;">
    <col style="width: 50%;">
  </colgroup>
    <tbody>
        <tr>
            <td>메인 페이지</td>
            <td>회원가입</td>
        </tr>
        <tr>
            <td>
		<img src="static/README_images/wf_main.png" width="100%"/>
            </td>
            <td>
                <img src="static/README_images/wf_register.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>로그인</td>
            <td>게시글 리스트</td>
        </tr>
        <tr>
           <td>
                <img src="static/README_images/wf_login.png" width="100%"/>
            </td>
	     <td>
                <img src="static/README_images/wf_post_list.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>게시글 리스트(로그인)</td>
            <td>프로필 수정</td>
        </tr>
        <tr>
            <td>
                <img src="static/README_images/wf_profile_post_list.png" width="100%"/>
            </td>
            <td>
                <img src="static/README_images/wf_profile.png" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>새 게시글 작성</td>
            <td></td>
        </tr>
        <tr>
            <td>
                <img src="static/README_images/wf_post_form.png" width="100%"/>
            </td>
            <td>
            </td>
        </tr>
    </tbody>
</table>

<br>

## 7. 구현 화면

<table border="1" style="width:100%;">
  <colgroup>
    <col style="width: 50%;">
    <col style="width: 50%;">
  </colgroup>
    <tbody>
        <tr>
            <td>메인 페이지</td>
            <td>회원가입</td>
        </tr>
        <tr>
            <td>
		<img src="static/README_images/main_page.PNG" width="100%"/>
            </td>
            <td>
                <img src="static/README_images/register.PNG" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>로그인</td>
            <td>게시글 리스트</td>
        </tr>
        <tr>
           <td>
                <img src="static/README_images/login.PNG" width="100%"/>
            </td>
	     <td>
                <img src="static/README_images/post_list.PNG" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>게시글 리스트(로그인)</td>
            <td>프로필 수정</td>
        </tr>
        <tr>
            <td>
                <img src="static/README_images/post_list_logged_in.PNG" width="100%"/>
            </td>
            <td>
                <img src="static/README_images/profile_edit.PNG" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>비밀번호 변경</td>
            <td>새 게시글 작성</td>
        </tr>
        <tr>
            <td>
                <img src="static/README_images/password_change.PNG" width="100%" width="100%"/>
            </td>
            <td>
		<img src="static/README_images/post_form.PNG" width="100%"/>
            </td>
        </tr>
        <tr>
            <td>게시글 자세히 보기</td>
            <td>게시글 자세히 보기2</td>
        </tr>
        <tr>
            <td>
                <img src="static/README_images/post_detail_1.PNG" width="100%"/>
            </td>
            <td>
		<img src="static/README_images/post_detail_2.PNG"/>
            </td> 
        </tr>
    </tbody>
</table>

<br>

## 8. 시연 영상

<table border="1" style="width:100%;">
  <colgroup>
    <col style="width: 50%;">
    <col style="width: 50%;">
  </colgroup>
    <tbody>
        <tr>
            <td>회원가입, 로그인</td>
            <td>둘러보기</td>
        </tr>
        <tr>
            <td>
		<img src="static/README_images/signup_login.gif"/>
            </td>
            <td>
                <img src="static/README_images/lookaround.gif"/>
            </td>
        </tr>
    </tbody>
</table>

<br>

## 9. 배포

URL [https://mini-project2-fk2n.onrender.com/]

<br>

## 10. 후기

Django CBV를 사용한 블로그 프로젝트를 완료하면서 계획했던 것보다 훨씬 시간을 많이 소요했고 어려웠지만 많은 것을 배웠습니다. 여러 CBV의 기능을 이해해가는 과정이 어려웠지만 프로젝트를 진행함에 따라 장고에 대한 이해도가 이 한 주 동안 크게 늘었습니다.
사용자 인증, 댓글 시스템, 좋아요 등의 기능을 구현하면서 우리가 일상적으로 사용하는 웹사이트들이 얼마나 복잡한 구조로 되어있는지를 체감했고, 이를 구현해 나가는 과정에서 많은 성취감을 느꼈습니다. django-recaptcha와 dnspython 같은 외부 라이브러리를 활용하면서 보안과 유효성 검사를 어떻게 웹사이트에 도입하는지와 그 중요성도 알게되었습니다.
프로젝트에서 가장 어려웠던 부분은 댓글의 답글 기능과 파일 디렉터리 구조 설계에 대한 이해, 그리고 tailwindCSS 였습니다. 앞으로 더 다양하고 많은 기술을 요구하는 프로젝트에도 도전해 보고 싶습니다.

<br>

---

