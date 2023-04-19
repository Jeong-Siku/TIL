# 기초이론

## 컴퓨터
- 하드웨어
  - 입력장치
  - 출력장치
  - 중앙처리장치
  - 주기억장치
  - 보조기억장치
- 소프트웨어
  - 시스템 소프트웨어
  - 응용 소프트웨어

## 컴퓨터 프로그램

## 임베디드 프로그램

## 컴퓨터의 언어
- 기계어

## 프로그래밍 언어
- 인터프리터 언어
- 컴파일러 언어

## 빅데이터
- 정형:구조와 데이터 내용이 별도로 저장
- 반정형:데이터 내용 안에 구조에 대한 설명이 함께 존재
- 비정형


## 빅데이터 속성
- 규모
- 다양성
- 속도
- 정확성
- 가치

## 데이터베이스
- 데이터 & 정보
- 정보처리
- 정보시스템
- 데이터베이스
  - 공유데이터
  - 통합데이터
  - 저장데이터
  - 운영데이터  
- 데이터베이스의 특징
  - 실시간 접근성
  - 계속 변화
  - 동시 공유
  - 내용 기반 참조
  - 데이터의 무결성(오류x)
  - 데이터의 독립성
  - 보안
  - 중복 최소화
  - 제작 및 수정 용이
  - 안정성 향상

- `특성`에 따른 데이터 분류
  - `범주형` 데이터(정성적)
    - 명목형
    - 순서형
  - `수치형` 데이터(정량적)
    - 이산형
    - 연속형

- 파일 시스템 ⟷ 데이터베이스 관리 시스템(DBMS)
  - 정의기능
  - 조작기능
  - 제어기능

- 데이터베이스관리 시스템 세대
  - 1세대 : 네트워크, 계층
  - 2세대 : 관계형
  - 3세대 : 객체지향 , 객체관계
  - 4세대 : NoSQL , NewSQL DBMS

- 데이터베이스 시스템
- 스키마
- 인스턴스

- 3단계 데이터베이스 구조
  - 외부 단계
  - 개념 단계
  - 내부 단계

- 3단계 데이터베이스 구조의 사상 또는 매핑
  - 외부/개념사상 : 응용 인터페이스
  - 개념/내부사상 : 저장 인터페이스
    - 데이터 독립성
      - 논리적 데이터 독립성
      - 물리적 데이터 독립성

- 데이터 사전
- 데이터 디렉터리
- 사용자 데이터베이스
- 데이터베이스 사용자
  - 데이터베이스 관리자
  - 최종 사용자
  - 응용프로그래머

- 데이터 언어
  - 데이터 정의어
  - 데이터 조작어
    - 절차적 데이터 조작어
    - 비절차적 데이터 조작어(선언적 언어)
  - 데이터 제어어

- 데이터베이스 관리시스템
  - 질의처리기
  - 저장데이터 관리자

- 데이터 모델링
- 2단계 데이터 모델링
  - 개념적 데이터 모델링
  - 논리적 데이터 모델링
- 데이터모델
  - 개념적 데이터 모델
  - 논리적 데이터 모델
- 데이터 모델의 구성
  - 데이터 구조
  - 연산
  - 제약조건 → 데이터 무결성 유지 목적

- 개체-관계 모델
- 개체-관계 다이어그램
- 개체 : 구별되는 모든 것
- 속성
- 개체 타입
- 개체 인스턴스
- 개체 집합

- 논리적 데이터 모델의 개념

- SQL

# Python
>인터프리터 언어, `객체지향적 동적 타이핑 대화형 언어`

## 변수
>값을 저장하는 공간 , 메모리에 만들어진다.

## 변수명 = Data
- 작업영역 = 저장영역
- 식별자

## 자료형
- 기본자료형 = 리터럴 데이터(단일 종류)
- 진법
- str은 `콘테이너`
- 형변환
  - 묵시적 변환
  - 명시적 변환

## 표준입출력

## 연산자
- 산술 연산자
- 관계 연산자
- 논리 연산자
- 비트 연산자
- 대입 연산자
- 복합 대입 연산자
- 멤버 연산자
- 아이디 연산자

## 제어문
- 조건문
  - if
  - 삼항 연산자
- 반복문: 중첩 가능
  - for , else
    - range
  - while
    - 무한반복
    - break
    - continue
- random
  - randint
  - random
  - uniform
  - randrange

## 리스트
- 순서o,수정가능, [] or list()
- 인덱스
- 슬라이싱
- 메소드
- 얕은 복사
- 깊은 복사

## 튜플
- 불변 순서
- 값 변경 불가
- 인덱스 가능 , count
- +로 튜플 추가가능
- 1개 요소일 시 `,` 반드시 필요
- 괄호 생략 가능
- () or tuple()

## 딕셔너리
- 이뮤터블한 `키`와 뮤터블한 `값`을 가진 순서 없는 집합
- {} or dict()
- 인덱스로 접근 불가, 키로 접근
- 메소드

## 함수
- def
- return
- 매개변수와 return 생략가능
- 인수
- 매개변수
- `*`arg: `가변`인자
- `**`kwargs: `딕셔너리`
- 전역변수 , 지역변수
- 재귀호출

## 메모리 영역
- 운영체제 → 메모리
- 메모리가 있으면 할당요청 거절 x
- 할당된 메모리 공간은 재할당 x
- 할당된 메모리를 해제하면 빈영역으로 인식
  - 코드영역
  - 스택영역
  - 데이터영역
  - 힙영역

- 정적할당: 자동회수
- 동적할당: 명시적 회수

# 객체지향
- 객체의 상호작용
- 객체란?
- 객체간의 관계
  - 집합관계
  - 사용관계
  - 상속관계
- 캡슐화: 보존, 보호, 은닉성
  - 클래스와 객체
  - 접근제한자
- 상속성
- 다형성
  - 오버라이딩
- 추상화
  - 객체에서 클래스 만들기

## 클래스
- 객체
- 인스턴스
- 필드
- 메소드

## 생성자
- def `__inin__`(self)

## 메소드
- 매개변수, 인자
- 클래스가 가지고 있는 기능

## 멤버
- 인스턴스 멤버
  - 인스턴스 필드, 인스턴스 메소드
- 정적 멤버
  - 클래스 => 정적필드 , 정적메소드, 클래스 메소드
  - @classmethod , cls
  - 클래스 변수

## 캡슐(은닉)
- 공개속성, 비공개속성
- `__속성명`으로 사용
## 상속
- class 자식클래스(부모클래스)
- 다중상속 가능
## 다형
- 메소드 오버라이딩
  - 메소드 무력화 : 서브클래스에서 메소드 중복 작성시 발생
## 추상
- 추상클래스
  - 실체 클래스의 부모 클래스

## 연산자오버로딩
>연산자가 복수의 기능 수행

## 문자열
- 인덱싱과 슬라이싱 가능
  - __문자열함수__
  - count()
  - find()
  - index()
  - join()
  - upper()
  - lower()
  - replace()
  - split()
  - strip()
  - rstrip()
  - lstrip()
  - isdigit()
  - islower()
  - isupper()
  - title()
  - capitalize()
  - startswith()
  - endswith()

## 정규표현식
- 메타문자 : 원래 그문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자
- 문자클래스 : [-],범위 및 매치
- Dot(.) : 모든 문자와 매치, [.]은 문자를 뜻함
- 반복(*) : *앞에 있는 문자가 0~무한대 반복에 사용
- 반복(+) : +앞에 있는 문자가 1~무한대 반복에 사용
- 반복({m,n}, ?) : 앞에 문자의 반복 횟수를 고정
  - ? : 앞에 문자가 0~1번 사용 

## re 모듈
>정규 표현식을 지원하기 위해 제공하는 모듈
- re.compile
- re의 모듈
  - match
    - group
    - start
    - end
    - span
  - search
  - findall
  - finditer

- 메타문자 : 매치가 진행되면 현재 매치되고 있는 문자열의 위치가 변경됨
- 문자열 소비가 없는 메타문자
  - ㅣ,^,$,\A,\Z,\b

- 그루핑
- 전방탐색
  - (?=...): 긍정형 전방탐색
  - (?!...): 부정형 전방탐색

- sub 메서드로 문자열 바꾸기

## 파일입출력
- EOF마커
- 위치표시자
- "r" , "w", "a", "r+"
- pickle
  - dump()
  - load()

## 예외처리
>오류가 발생할 때 프로그래머가 작성한 코드를 실행하는 방식
- try
- except

## 데이터베이스
### SQL
- 정의어
  - 테이블 생성 : create
  - 테이블 변경 : alter
  - 테이블 삭제 : drop
- 조작어
  - 생성: insert
  - 조회: select
  - 갱신: update
  - 삭제: delete

## pymysqp
>sql문법을 사용해 데이터베이스를 다루는 라이브러리. cursor 객체를 사용해 mysql을 다룬다.
- connect
- cursor
- execute
- fetchone

## 데이터
- 피쳐 : 데이터테이블의 하나의 열이름에 해당
- 데이터 인스턴스: 하나의 데이터, 튜플, 한줄
- 차원의 저주
- 데이터의 분류
  - 연속형 데이터
  - 이산형 데이터: 명서등비

## numpy
- 리스트 간의 연산을 지원하는 과학계산용 라이브러리
- 벡터나 행렬 같은 선형대수의 표현법을 코드로 처리
- 배열 생성
  - np.array([])
- np.shape
- np.reshape
  - -1
- np.flatten
- 인덱싱: [행][열] or [행,열]
- 슬라이싱
- np.arrange : 증가값으로 실수도 가능
- np.ones
- np.zeros
- np.empty
- np.ones_like
- np.zeros_like
- np.empty_like
- np.identity
- np.eye(n,m,k)
- np.diag
- 분포함수
  - 균등분포함수:unoform
  - 정규분포함수:normal
- 연산함수
  - sum(axis=0)
  - mean
  - std
  - sqrt
- 축(axis)
- 연결함수
  - vstack
  - hstack
  - concatenate
- T
- 사칙연산 함수
  - 요소별 연산
  - 벡터의 내적 연산
- 브로드캐스팅 연산
  - 하나의 행렬과 스칼라 값
  - 행렬과 벡터
- 비교연산
  - all
  - any
  - where: 문자열의 변경도 가능
  - argsort
  - argmax
  - argmin
- 불린 인덱스: 조건
- 팬시 인덱스: 인덱스

# 판다스
>데이터 테이블을 다루는 도구. 기본적으로 넘파이를 사용
 - 데이터프레임
 - 시리즈
 - 시리즈객체
   - 데이터
   - 인덱스: 중복가능
   - 데이터타입
- 시리즈 객체 생성하기
  - dict, data, index
- 데이터프레임 객체

## 판다스 DATA 추출
- 데이터로딩
  - xlsx
    - openpyxl
    - pip install openpyxl
    - read_excel
- 데이터 추출(열 이름 사용)
  - head와 tail함수
- 데이터 추출(행 번호 사용)
  - 인덱스 번호로 호출
- 데이터 추출(행,열 모두 사용)
- loc,iloc
- reset_index
- drop 함수

## 판다스 그룹별 집계
- 그룹별 집계(groupby)
  - 피봇테이블 기능과 유사
  - 분할-적용-결합
  - 멀티인덱스 그룹별 집계
- get_group
- 집계
  - agg 함수:min,넘파이 mean 등
- 변환(transformation)
- 필터(filter)

## 판다스 병합과 연결
- 병합(merge)
- SQL(join)
  - 내부조인:innerjoin
  - 완전조인:outerjoin
  - 왼쪽조인:left_on
  - 오른쪽조인:right_on
- 인덱스에 의한 병합
- 연결(concatenate)
  - concat
  - append

## 데이터 시각화
- matplotlib
- seaborn

## Matplotlib
- 파이플롯(pyplot)
- 축을 여러개 만들 때 서브플롯으로 축 객체 공간 확보
  - add_subplot(,,)
  - subplots

## seaborn
- 행, 열, 데이터프레임
- hue
- regplot
- pairplot
- scatterplot
- describe()
- barplot
- np.unique
- violinplot
- swarmplot

## Word cloud