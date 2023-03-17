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
