# 풀스택프로그래밍

> 2023.03.17

## OT

data fog  
data lake  
data mart  
데이터엔지니어 데이터사이언스 데이터분석

---

# web?

> 인터넷통신 -> 연결 가능한 환경

## C-S(Client-Server) 구조

- client = 인터넷이 가능한 모든 환경
  1. 요청(request)
- server <- `개발`이 주목적
  - API = 메뉴판
  - 처리
  2. 응답(response)  
     </br>
- Sever의 처리
  - Front End: 클라이언트가 볼 수 있는 `화면`
    - HTML,CSS
    - JavaScript
  - Back End - python, JS,Java(+spring),golony... - Data 처리
    <br>
- 3계층 구조와 연관

## HTML,CSS,JS

> Front End(화면)

</br>

# HTML (Hyper Text Markup Language)

- 이동가능한
- `tag`(mark) : 표식
- 정해진 것만 써야한다.

```bash
XML
  - 정해진 구조가 없다.
```

```bash
vscode extension : Live server , prettier , colorize , DotENV , Output Colorizer , Rainbow CSV , Inline SQL , HTML CSS Support , Auto Rename Tag , Auto Close Tag , CSS Navigation , Material icon Theme , Stylelint
```

## html 기본

- `! + tap` 은 기본적인 설정이 작성됨
- 주석 : `cmd + /`
- <ㄱ> 작성 : `태그명 + tap`

- head : HTML 문서의 정보 설정 부분
- meta : 메타데이터 설정
  - 메타데이터 : 데이터를 표현하기 위한 데이터

### _제목 태그_

- 제목 태그 : hn , n은 숫자 1~6

</br>

### _시멘틱 태그_

- div: 상위 태그
- 시멘틱 태그
  - header
  - main
    - p(ph)
  - aside
  - footer

</br>

## 문자 콘텐츠

> 문자 태그는 블록태그와 인라인 태그로 나뉜다.

#### 1. _block tag_

> > 컨텐츠의 너비에 상관없이 가로 전체를 차지한다.

- 리스팅
- ol(ordered list), ☆ul(unordered list)
- ol : 숫자가 부여되는 리스트
- ul : 불릿(점)으로 나열되는 리스트
- li 태그를 이용해서 리스팅

</br>

- dt(Description title)
- dl(Description List)
- dt(Description Term)
- dd(Description Details)

  > > > 항목들에 대한 설명을 작성

- p(paragraph) : 문단을 설정
- hr(Horizontal Rule) : 수평선 긋기
- pre(Preformatted Text) : 프롬프트 창 설정

#### 2. _inline tag_

> > 컨텐츠의 너비만큼 차지한다.  
> > 블록 태그 내에 인라인 태그 작성은 가능하다.  
> > 인라인 태그 내에 인라인 태그 작성 ok.  
> > 인라인 태그내에 블록 태그는 bad

- a(Anchor) : 다른 url로 연결할 수 있는 하이퍼 링크 생성
  - href에 이동할 url을 적는다.
  - \<a href="" target="\_blank"></a>
- strong : 특정 범위의 글자를 굵게 표시
- i(italic) : 특정 범위의 글자를 기울여서 표시
- span : 범위를 지정하기 위해 사용
  - \<span style="color:red"> \</span>
- img
  - src : 이미지 주소(경로)
  - alt : 이미지가 존재하지 않는 경우 표시할 텍스트.  
    시각장애인들을 위한 TTS 수행하기 위한 텍스트
  - title : 이미지 위에 마우스를 올렸을 때 표시할 텍스트
  - <a ref=""> <img> </a> : 이미지를 눌렀을 때 사이트로 이동

## 테이블 태그

- table : 표 태그
  - \<table border="1">
  - thead : 컬럼을 작성하는 구간
  - tbody : 테이블의 데이터가 작성되는 구간
  - tfoot : 테이블의 데이터를 요약하거나 마무리하는 구간
  - tr(table row) : 한 행을 만들 때 사용
  - td(table data) : tr 내부에 채워지는 cell을 만들 때 사용
  - th(table head) : tr 내부에 채워지는 컬럼의 이름을 만들 때 사용

## 양식 태그

- form : 웹 서버에 사용자가 입력한 내용을 제출하기 위한 태그

</br>

- form 내에 다른 form이 올 수는 없다.
  - action : 입력된 데이터를 전달할 서버의 URL
  - method : 서버로 전송할 HTTP 방식(get, post 등)

</br>

- input : 사용자로부터 입력을 받기위한 태그
  - \<input type="text" placeholder="이름을 입력하세요" />
  - \<input type="password" placeholder="비밀번호를 입력하세요" />
  - \<input type="email" placeholder="이메일을 입력하세요" />
  - \<input type="tel" placeholder="전화번호를 입력하세요" />

</br>

- textarea : 여러 줄을 입력할 수 있는 태그
  - \<input type="checkbox" />

</br>

- name 속성 : 서버가 클라이언트에게 데이터를 받을 때 키값으로 사용!
  - 남자 \<input type="radio" name="gender" />  
    여자 \<input type="radio" name="gender" />

</br>

- type="file" : 파일 업로드 할 때 사용
  - \<input type="file" />

</br>

- type="submit" : 서버에게 데이터를 전달할 때 사용
  - \<input type="submit" value="보내기!" />

---

## attribute(속성)

- 클래스 : 설계도
- 객체 : 만들어진 것
- Tag -> 객체(object) -> `요소`(element)
- <태그명 속성명 = "속성값" 속성명="속성값">
  - ex) \<a href=""> </a>
    - a : 태그명
    - href : 속성명
    - "" : 속성값
      - `id` : 전체 문서에서 `단 하나`만 부여  
         `중복된 id 값 존재 x`  
         고유한 엘리먼트 지정
      - `class` : `중복`이 가능하게 부여 가능, `여러 개` 부여 가능  
         중복되는 스타일링
      - name
        - form에만 쓰인다.

## DOM(Document Object Model, 문서 내 객체 구조)

=> Java Script 용어

> 문서를 구성하고 있는 Element의 구조. 꾸준히 DOM을 파악하기(손으로 그리는게 좋다.)

- Element & Element 사이의 관계
  - 부모
  - 자식
  - 자손(후손)
  - 형제 : prev sibling, next sibling(기준을 바탕으로)
    - 자식은 자손에 포함된다
    - 자손은 자식에 포함되지 않는다.

# CSS(Cascade Style Sheet)

> cascade(상속?)-DOM과 관련,자손과 자식에 영향  
> **2023.03.20 (월)**

## 1. 태그\*아이디\*클래스 선택자

- style sheet는 head에서 작업
- style 태그를 작성 후 내부에 태그 선택자를 작성
  - 태그 선택자
    - 태그명{}
  - 아이디 선택자
    - #id명{}
  - 클래스선택자
    - .클래스속성값{}
    - 여러 클래스를 동시에 선택
      - .클래스속성값.클래스명속성값...{}
    - 태그에서 특정 클래스만 선택
      - 태그.클래스명{}

## 02. cascade\_성질확인

> 부모엘리먼트를 스타일링하면 그 성질이 자손에게 전해진다.  
> DOM과 연관있다.

## 03. 관계선택자

> 부모, 형제, 자식, 자손  
> css는 부모, 형제는 사용하지 않는다.

- ★✭★자식 선택자
  - `>`
  - 부모 > 자식
  - .부모속성값 > .자식속성값
- 자손 선택자(부모 자손): `전부` 다 가져온다. 그리디하다
  - `공백`
  - .부모속성값 .자식속성값

## 04. 속성선택자(attribute selector)

- `[속성명="속성값"]`{}
- 일반적으로는 태그명을 앞에 붙여서 사용
- 태그명[속성명="속성값"]{}

## 05. 가상선택자

> 있을 수도 있고, 없을 수도 있는데, 있으면 선택

- not selector
  - 선택자1 중에 선택자 2가 `아닌 것`
  - .선택자1:`not`(.선택자2){}
- `nth-child`
  - n: 숫자
  - n번째 요소(Element)
  - 수식도 가능
  - .선택자:nth-child(n){}

# 부트스트랩(Bootstrap)

> 프론트엔드 툴킷(도구상자). 디자인을 못하는 개발자들이 주로 사용.  
> 사이트에서 필요한 코드를 가져와서 쓸 것. 어떤 형태를 지닌 기능인지 대략적으로 살펴볼 것

## 레이아웃

> 표시해야할 사항들  
> Bootstrap Layout Grid system : Element의 가로길이가 중요하다.

### 그리드 시스템(Grid system)

- 반응형 디자인 : 화면의 크기에 자동으로 반응
- 기본적으로 가로길이를 `12등분`한다.
- Element의 개수가

### 컨테이너(Containers)

> 부트스트랩을 적용시키기 위한 환경

- 가장 기본적인 레이아웃 요소
- 기본 그리드 시스템을 사용할 때 필요: 12등분을 적용하는 요소
- class="container"

## 폼(Forms)

- `form-control` : 폼에서 가장 중요한 클래스
  - class="form-control"

## 컴포넌트(Components)

- 버튼은 누르는 Element에는 대부분 적용 가능

Sass,Scss는 제외하고 볼 것
lg -> 모니터
mg -> 태블릿
sm -> 스마트폰

## CDN

> 직접 다운로드없이 링크를 통해 컴퓨터에 부담을 줄여 사용할 수 있게 해준다.
> 헤드에 모두 넣는것보다 사이트에 써있는 것처럼 헤드와 바디부분에 나눠서 넣는 것이 좋다.

```
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>

    <!-- 부트스트랩 css -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />

    <!-- jQuery -->
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>

    <!-- 팝업을 위한 js -->
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
      crossorigin="anonymous"
    ></script>

    <!-- 부트스트랩을 위한 js -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
      crossorigin="anonymous"
    ></script>

    <!-- 위에 순서가 꼬이지 않도록 주의. 인식이 안되는 경우가 발생 -->
  </head>
```

- row추가
- column으로 row에 들어갈 엘리멘트 개수를 지정

### 클래스 속성값

- mt-5 : empty top
- text-center
- for : 연결되어있는 곳을 표시
- form 태그
  - input 등 서버에 입력을 위한 형태를 갖추기 위한 태그
  - form-group
    - label과 input태그를 연결시켜 레이아웃에 기본값에 잘 나타나도록 돕는다.

```bash
<body>
    <!-- 부트스트랩의 그리드 시스템을 사용하기 위해서는 container가 필요하다 -->
    <div class="container">
      <!-- row 만들기 -->
      <div class="row mt-5">
        <!-- 가로길이 총 12개의 그리드 사용 -->
        <div class="col-12 text-center">
          <h1>로그인</h1>
        </div>
        <!-- <div class="col-6">반갑습니다</div> -->
      </div>

      <!-- 로그인 row -->
      <div class="row mt-5">
        <div class="col-12">
          <form>
            <div class="form-group">
              <label for="user_id">아이디</label>
              <!-- 입력창은 기본적으로 클래스에 form-control 넣을 것 -->
              <input
                type="text"
                class="form-control"
                placeholder="로그인할 아이디 입력"
                id="user_id"
              />
            </div>
            <div class="form-group mt-5">
              <label for="user_password">비밀번호</label>
              <input
                type="password"
                class="form-control"
                id="user_password"
                placeholder="비밀번호를 입력하세요"
              />
            </div>
            <input type="submit" value="로그인" class="btn btn-danger" />
          </form>
        </div>
      </div>
    </div>
  </body>
```

- 하나의 row 태그 내에 들어갈 엘리먼트의 개수는 col-n을 통해 조절할 수 있으며, row태그 내에 자식의 개수를 통해 엘리먼트를 확정시킬 수 있다.

# DJANGO

> 2023.03.21 (화)

## 프레임워크(Framework)란?

## Django 설치하기

### 01. 가상환경 설정

- 전역설치
  - 모든 파이썬 project에서 사용
- 지역설치
  - project별 패키지 설치
- pip3 install virtualenv
- conda create -n `django-env`

- virtualenv venv

- source activate venv/bin/activate
- conda activate django-env

Django 설치

- conda install django==2.1.7
  (pip3 install django==2.1.7)
- environment location: /Users/seojeongsik/opt/anaconda3/envs/django-env

Django `프로젝트 만들기`

> 프로젝트는 웹서비스의 전체적인 환경을 관리하고,App은 소규모단위를 이용해 프로젝트를 구성한다.

- django-admin startproject my_communuty
- cd my_community

Django 서버 실행하기

- python manage.py runserver
- ip주소를 대체할 수 있는 도메인
  - port: (ex.8000)
  - 로컬호스트: 내컴퓨터 주소 (ex.127.0.0.1)

## MTV 이해하기

> Django프레임워크의 뼈대는 MTV라는 구조로 이뤄졌다. MTV는 Model, Template, View를 의미한다

### 01.Model

> 데이터의 표현을 의미한다.웹 애플리케이션에서 사용할 데이터의 모양

- 데이터들은 데이터베이스에 명세&관리(CRUD) 작업이 일어날 수 있다.
- UserModel로 객체를 만들면 관리가능한 Data가 된다.
- 파이썬 객체를 활용하여 쿼리없이 객체를 관리할 수 있도록 돕는다.
  - save() -> insert
  - get() -> select
  - 프로그래밍 언어를 sql로 전환
- ORM

```bash
class UserModel(models.Model):
		# Field 정의
    username=models.CharField(max_length=32, verbose_name='사용자명')
    password=models.CharField(max_length=32, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

		# 메타데이터 정의
    class Meta:
        db_table = 'tb_users'
```

### 02. View

> 사용자의 요청을 처리하고 결과를 반환시키기 위한 로직을 담당

- MTV MVC
- View = Controller
- client의 리퀘스트를 view가 받고 model을 거쳐 DB에 전달

### 03.Template

> 클라이언트가 볼 화면
> Response

- Data
  - Json
  - XML
- Page
  - HTML
  - CSS
  - JS

## 게시판 프로젝트 - 회원가입

### 01. Django Start App

- MSA(Micro Service architecture)

  - App은 프로젝트를 구성하는 하나의 모듈
  - `django-admin startapp user`
  - 객체

- 프로젝트앱

  - 프로젝트와 동일한 이름을 가진 App객체
  - 전체적인 관리를 하는 App

- 개발순서
  - 반드시 모델부터 개발할 것!
    - view, template는 순서 상관없음

### 02. App 등록하기

- 프로젝트앱에 `settings.py`을 통해 등록
  - settings.py는 프로젝트에 대한 설정이 들어간다.
  - INSTALLED_APPS리스트에 등록시킬 App의 이름을 문자열로 적는다.

### 03. 회원가입 화면 구현하기

#### 01. Model 구현

> 기능에 사용할 데이터를 먼저 생각하기

- models.py

  - models.Model : 클래스를 상속. 멤버변수를 이용해 테이블의 컬럼을 정의
    - 멤버변수가 컬럼이 된다
    - 클래스명이 테이블명이 된다.
  - models.CharField : 문자열 형태의 필드를 생성
  - max_length,verbose_name
  - models.DateTimeField : 년일월시간을 나타낼 때 사용하는 타입
    - auto_now_add : 현재시간으로 데이터가 추가

  #### 02. 모델변경 사항 적용하기(Migration)

  > 무중단 서비스. 마이그레이션을 통해 가능, 에러를 피하기 위해 사용. 모델이 바뀌면 마이그레이션 작업 필요

  1. 모델 변경 정보 생성

  - python manage.py makemigrations

  2. 모델 변경 사항 적용

  - python manage.py migrate

  #### 03. django admin 사용하기

  > 웹사이트 전체의 데이터를 관리하기 위한 도구.

- python manage.py createsuperuser
- python manage.py runserver
- 127.0.0.1:8000/admin

  #### 04. Admin과 Model 이어주기

  - /user/admin.py

  ```bash
  from django.contrib import admin
  from .models import User

  # Register your models here.
  class UserAdmin(admin.ModelAdmin):
    pass

  admin.site.register(User, UserAdmin)
  ```

  - _Back Office_
  - _관리자 정보_

### _관례\_python_

- 변수명, 함수명
  - 스네이크 케이스
  - 소문자,언더바
  - ex.student_name
- 클래스명
  - 파스칼 케이스
  - 첫글자 대문자, 이어지는 글자 대문자
  - ex. StudentName
- studentName
  - Java
  - cannel case
- student-name
  - HTML, CSS
  - kebab case

#### 04. Meta 클래스 구현하기

> 기본적으로 모델의 클래스 이름이 테이블의 이름이 된다. 이 때 클래스 이름이 아닌 데이터베이스의 특정 테이블과 모델을 연결하고 싶다면 Meta클래스를 사용한다.

- Meta클래스는 모델클래스의 `내부클래스`로 구성된다

  - 테이블의 이름을 붙일 때 변수명
    - tb_user
    - tbl_user

  ALTER

- 메타데이터변경

  CREATE

- 테이블 생성

_\_\_str\_\_은 정보의 변경이 아니어서 migration은 필요하지않다._

_마이그레이션을 할 때는 서버를 잠시 끊었다하기(ctrl + c)_

```
class
인스턴스:실체화
오브젝트:개념적
접근연산자: .

메소드는 수정이 아닌 호출을 위한 것 . static=클래스=메소드에 하나 존재
멤버변수는 각 객체마다 존재

상속은 확장
오버라이딩: 1. 부모에서 추상적인 개념이 자식에서 구체화되는 것 2. 수정하는 것
super() : 부모
argument: 인자
parameter: 매개변수
```

> 23.03.22 (수)
> 작업 시작시 activate와 해당 프로젝트로 이동(cd)

app : 동작가능한 서비스(독립적인 작은 서비스)
서버
Response:
-data
-page

#### template

- ui를 만들기 전에는 그림을 그려볼 것
- form
  - action : 어디로 데이터를 보낼 것인가.(url)
    - action="."은 현재 띄워진 url을 그대로 사용
  - method : 어떤 방식으로 데이터를 보낼 것인가.
    - Parameter : 클라이언트가 서버에게 보내는 데이터
      - Get : 가지고 오는 것 = SELECT
        - parameter를 `URL`에 실어서 보낸다.
          1. 일반적으로 Query String을 활용
          2. path parameter
        - 가볍고 빠르지만 보안에 취약하다. 많은 값을 전달하기 힘들다. 텍스트 데이터만 전달 가능.
      - Post : 데이터 등록 = INSERT
        - parameter를 `BODY`에 실어서 보낸다.
          - body : 객체 내에 데이터를 실을 수 있는 곳.
          - 무겁고 느리지만 보안에 취약x. 큰 데이터 전송가능. 다양한 데이터를 전송 가능
      - 절대적인 것은 아님

※ Get 방식
www.naver.com/webtoon/wed`?num=1&date=20230322` : URL + QueryString

- 김밥주세요? 몇개=1개
  www.naver.com/webtoon/wed`/1/20230322` : URL + PathParameter
- API 만들 때 자주 사용

※

- URI : `http://`www.naver.com/ -> scheme(스킴), 스킴을 포함한 전부
- ★URL : HOST(도메인 With port{80}) + Path -> `naver.com/~/~..` , 스킴만 빠진 것
- URN : Path -> /webtoon/wed/...
- Protocol : 규약. 인터넷을 어떤 규약으로 사용할 것인가?
  - HTTP(HyperText Transfer Protocol)
  - HTTPS( " Secure)
  - FTP(File Transfer Protocol)
- `http://`www.naver.com/webtoon/wed : 스킴 + 호스트 + path ?쿼리스트링을 통한 정확한 정보
- URN은 API로 대체하여 사용한다.
  - API는 메뉴판 같은 존재

# view

- 화면을 띄울 수 있는 `코드`를 response해준다.
- 렌더링할 때 templates를 우선시 하기에 디렉토리 파일을 적을 필요없다
- FBV
- render : 화면을 보여주는 함수
  API
- 클라이언트가 요청할 수 있는 URL을 모아놓은 것
  - Application : 프로그램
  - Programming : 제어
  - Interface : 창구

urls.py

- 메인프로젝트 앱의 urls.py는 API , 메뉴판이며 메인프로젝트앱의 메뉴들은 각 앱들을 뜻한다.
- 프로젝트 앱에 urls.py를 지나고 앱에 urls.py를 간다.
- urlpatterns : 이 변수명은 고정
  - url 등록
- include('user.urls') : user App에 있는 urls.py에 urlpatterns에 등록 되어 있는 모든 url을 한꺼번에 포함시켜주는 기능
- www.naver.com/news
- / 까지 메인프로젝트의 home

- model에 새로운 데이터콜럼을 추가하면 마이그레이션 작업에서 기존에 있던 데이터들을 어떻게 처리할지 묻는다.

---

- post

  - 데이터를 생성하고 싶을 때 사용하는 방식

- form의 기본 방식은 get이다.

- 회원가입 기능을 구현
  1. 회원 가입 화면 url
     - html 파일 보기
     - GET /user/register/
  2. 회원 등록 기능 url
     - 값을 다 입력한 다음 서버에게 보내는 url
     - POST /user/register/
- action=get or post로 동일한 url이 어떤 기능을 할지 구별한다.

- action="."은 현재 띄워진 url을 그대로 사용

views.py에서 기능을 구현(get과 post 구분)

register.html에서 작성한 name 속성은 클라이언트가 보낸 데이터가 무엇인지 서버가 알 수 있도록하는 키값이다.

※
오류가 났을 시 아래에서 위로 살펴볼 것. 내가 만든 코드를 살펴볼 것. 오류 문자를 현재 사용하고 있는 프로그램 이름과 함께 작성해서 물어볼 것.

CSRF 토큰 : 랜덤하게 암호화 된 16진수 정수

- 디도스 방지
- Register.html에서 form내부에 작성해야한다.
  - {% csrf_token %}

> 23.03.23 (목)

> admin을 통해 관리자페이지에 기능 추가

- list_display

※ **중요**

1. 설계
   - 어떤 data를 사용할 것인가?
     - 머신러닝,분석
     - data가 어떤건지
   - 코드 작성부터 한다면 잘못된 것
2. Data IO(Input Output)가 잘되는지 확인
3. 재설계
   - 이 데이터를 이용해서 어떻게 구현할까를 고민
     - 알고리즘/비즈니스로직

request.POST가 빈값이면 에러가 발생한다
request.POST.get을 사용하면 에러메세지를 반환하지 않고 name 변수값을 반환

parameter : 클라이언트가 서버에게 보낸 값
attribute : 서버가 클라이언트에게 `보여줄` 데이터 ex.res_data
attribute와 같이 전달되는 데이터는 `전달될` 데이터

request = 비즈니스로직 : 사용자가 보낸 데이터를 바탕으로 도출하는 것

if와 elif의 순서를 바꿨을 때 어떤 문제가 발생할까?

view에서 attribute와 template를 합쳐서 전달한다.

- template + attribute = View Resolver , Template engine

※표현식

- Template engine은 `표현식`을 통해 HTML에서 파이썬모드 사용을 가능하도록 기능을 제공한다.
  - `{{ }}` : Expression Block -> 표현식 블록(출력을 담당, python코드를 HTML로 변환.단, 무조건 변수에 들어있는 값을 변환한다.)
  - `{% %}` : Syntax Block -> 문법 블록(파이썬)

복호화 암호화

- Hash, SHA
- 복호화가 안된다 : 확인하는 비밀번호도 암호화하여 체크
- 알고리즘 고정화 : 비밀번호들의 암호화 과정에서 필요한 규칙을 고정하기 위해
- view에서 해당 기능 import

조회하기

- check_password

★Session : 서버가 클라이언트의 정보를 저장하는 공간

- 세션에 정보가 없다면 로그인하지않았다고 판단함
  1. 브라우저 종료
  2. 시간제한
- 로그인을 하는 순간 공간이 발생

cookie

- 클라이언트의 공간 : 브라우저에서 활동하는 기록들을 기입
- 서버에는 존재하지않음
- 서버마다 다르게 인식
- JWT
- Oauth 2

개발자툴-application-cookie

redirect

- 클라이언트를 해당 url로 이동시킨다.
  render
- 화면을 띄워준다.

pk=id

try
except

---

# 템플릿 상속

## 1. 공통 부분 분리

책과 수업의 구성이 다르다. 해볼 것

- 프로젝트앱에 구성
- user앱에 구성
  - {% block contents %}
  - {% endblock %}

# Django Form

- forms.py

## 커스터마이징

- {% %}
- id_for_label : id 속성값

  - id 값 -> id_password , id_user_id
  - input_type : text,password.email
  - field.name : form 클래스의 변수명
  - field.label은 forms.py에서 수정 가능

- .is_valid() : 유효성 검증
- clean : 오버라이딩을 통해 검증내용을 추가
- required : 필수적인 부분에 입력
