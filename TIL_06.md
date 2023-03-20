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
