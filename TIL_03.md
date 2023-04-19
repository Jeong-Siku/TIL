# Numpy
>기본 리스트와 달리 리스트와 리스트간의 연산이 가능.  
>파이썬의 고성능 과학 계산용 라이브러리
- 정적할당
- 행렬 연산 특화
- 반복문 사용하지 않음
- 텐서: 선형대수의 데이터 배열 ex.스칼라, 벡터, 행렬 ,3차원텐서,n차원텐서

## 배열 생성
- `import numpy ns np`
- `test_array=np.array([1,4,5,8],float)`
    - 매개변수1: 배열정보
    - 매개변수2: 데이터 타입
- 배열의 원소를 입력할 때는 반드시 `리스트 형식`으로 입력

## 파이썬 리스트와 넘파이 배열의 차이점
- 배열의 모든 구성 요소에 값이 존재해야함
- 하나의 데이터 타입만 사용
- 각 값 메모리 크기가 동일
- 가변불가 , 일그러진 사각형 불가, 직접 저장

## 메소드
- `np.array(l).dtype`
- **`np.array(l).shape`**  
    - ex. (10, )
    - `,`의 개수는 차원을 나타낸다.
     
- `np.array(l).ndim`
- `np.array(l).size`

## 배열의 구조
- (a, )
- 타입은 튜블
- 매개변수 dtype

## reshape
- 배열을 원하는 모양으로 생성 및 변형
- `x= np.array([[1,2,5,8],[1,3,5,8]])`  
- `x.reshape(-1,)`
    - 매개변수1쪽이 고차원을 뜻함  
    - `-1`은 자동으로 맞추는 것나. `나머지`라고 생각
    - 고차원, 저차원 위치에 모두 가능
    - 원소 개수가 안맞을 시 `nan`으로 나타남

## flatten()
- 데이터 그래도 `1차원`으로 변경

## 인덱싱
- `상대적인 주소`로 `값`에 접근
- np.array()[`행`][`열`] or [`행`,`열`]로 표현
- `shape`에서 출력되는 랭크 순으로 인덱싱에 접근

## 슬라이싱
- 인덱스를 사용하여 리스트 일부를 잘라내어 변환
- 넘파이 배열은 `행`과 `열`을 나눠 슬라이싱 가능
- 증가값
- `np.array()[시작 인덱스:마지막 인덱스:증가값]`

## arange
- range 함수와 같이 차례대로 값을 생성
- `np.arange(시작 인덱스, 마지막 인덱스, 증가값)`
- 증가값에 실수형 가능

## 기타 함수
- `T` : 행렬의 방향을 바꾼다.
- `ones` 함수
    - 1로만 구성된 넘파이 배열 생성
    - `np.zeros((행,열),dtype)`
- `zeros` 함수
    - 0으로만 구성된 넘파이 배열을 생성
- `empty` 함수

- `ones_like` 함수
    - 기존 넘파이 배열과 같은 크기로 만들어 내용을 1로 채움
    - `np.ones_like(np.array())`
- `zeros_like` 함수
    - 기존 넘파이 배열과 같은 크기로 만들어 내용을 0로 채움
    - `np.zeros_like(np.array())`
- `empty_like` 함수
    - 기존 넘파이 배열과 같은 크기로 만들어 빈상태로 만듦
## 단위행렬 함수
- `identity` 함수
    - 단위행렬(i행렬)을 생성
    - 매개변수 n으로 nxn 단위행렬을 생성
    - `np.identity(n)`
- `eye` 함수
    - `eye(N,M,k)`
    - `N`은 행의 개수, `M`은 열의 개수
    - `k`는 열의 값을 기준으로 시작 인덱스
- `diag` 함수
    - 행렬의 대각성분 값을 추출
    - `np.diag(np.array())`

## 분포 함수
- uniform 함수: `균등분포` 함수
    - `np.random.uniform(시작값, 끝값, 데이터개수)`
- normal 함수: `정규분포` 함수
    - `np.random.normal(평균값, 분산, 데이터개수)`

- 연산함수: 배열 내부 연산을 지원하는 함수
- 축: 배열의 랭크가 증가할 때마다 새로운 축이 추가되어 차원 증가
    - axix의 `0`은 `고차원` 방향
- sum 함수
    - 각 요소의 합을 반환
    - 랭크가 2 이상인 배열일 경우 축으로 연산의 방향을 설정
    - `matrix.sum(axis=n)`

## 연결 함수
>두 객체 간의 결합을 지원하는 함수
- `vstack` 함수
    - 배열을 수직으로 붙여 하나의 행렬을 생성
- `hstack` 함수
  - 배열을 수평으로 붙여 하나의 행렬을 생성

- `concatenate` 함수
    - 축을 고려하여 두개의 배열을 결합
    - 스택과 달리 생성될 배열과 소스가 되는 배열의 차원이 같아야함
    - `np.concatenate((matrix1,matrix2),axis=n)`
    - `기본축`으로 axis=0으로 설정됨

## 사칙연산 함수
- 넘파이는 파이썬과 동일하게 배열 간 사칙연산 지원
- `요소별 연산`: 두 배열의 구조가 동일할 경우 같은 인덱스 요소들끼리 연산 
- 배열 간의 곱셈에서는 요소별 연산과 벡터의 내적 연산 가능
    - 벡터의 내적: 두 배열 간의 곱셈
    - 두 개의 행렬에서 첫번째 행렬의 열 크기와 두번째 행렬의 행크기가 동일해야함
- `dot` 함수
    - 벡터의 내적 연산

## 브로드캐스팅 연산
>하나의 행렬과 스칼라 값들 간의 연산이나 행렬과 벡터간의 연산
- 조건도 입력 가능
- 1차원에 T는 변하지 않음
- `행 또는 열의 개수가 1`일 시 아직 구조가 확정되지 않은 것으로 `확장` 가능하다.

## 비교연산
- `all` 함수
    - `np.all(조건)`
    - true or false
    - and
- `any` 함수
    - `np.any(조건)`
    - true or false
    - or

## where 함수
>불린형일 때 참인 값들의 `인덱스 반환`
- `np.where(매트릭스>5)`
- `np.where(매트릭스>5,참일때 반환값,거짓일 때 반환값)`

- `argsort`
- `argmax`
- `argmin`

## 불린인덱스
- 특정조건에 만족하는 대상 추출
- matrix[`조건`]
- 원본을 수정하지 않음

## 팬시인덱스
- 해당 인덱스에 위한 값은 반환
- matrix[`np.array([],int)`]
- 원본을 수정하지 않음