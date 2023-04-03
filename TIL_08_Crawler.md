> 2023.03.28

# 크롤링 -> 스크래이핑

두개의 차이점 : 범위
크롤링은 범위가 크다
스크래이핑은 범위가 한정. 원하는 부분만

- API HTML&CSS 브라우저컨트롤 SCRAPY

크롤링 윤리

앱키값이 깃허브에 올라가지않도록 조심하기

네이티브 앱키 : 안드로이드,IOS에서 사용
REST API키 : 검색 등의 서비스 이용시
JavaScript 키 : 지도,주소검색 AI서비스
Admin 키 : 카카오

API document

카카오 개발자(kakao developers)

rest api key를 header에 넣어서 접근한다.

파이썬에는 상수가 없다.

대문자와 언더바로 변수를 만들면 그것은 상수라고 약속을 했다.

\${} : 자바스크립트 문법

pasing : 문자열을 다른 형태로 바꾸는 행위

HTML 스크래이핑

- text, 속성값을 중점으로
- HTML Element 단위로 생각하기
  - bs4 BeautifulSoup
    - 해당 객체는 DOM 구조를 가지고 있다.
    - 엘리먼트

Type Casting

- 형태를 바꾸는 것

파싱(pasing)

- 문자열의 형태를 바꿈

테스트 코드를 잘 써보자!

크롤링

- id부터 찾기

img는 data-original을 가져오는 것

> 2023.03.29 (수)
> API 크롤링 -> 비동기 통신 사용
> Selenium

모바일에서 크롤링 하는게 좋다 -> 모바일은 구조가 단순하다.

# 셀레니움

프론트엔드
browser 컨트롤

Driver : python을 통해 다른 프로그램을 조작할때 필요한 명령어 집합, 매개체

# 선형대수학

데이터사이언스스쿨 고급선형대수까지 읽기

넘파이 판다스 시각화 연습하기

# 01. API크롤링 - KAKAO 예시

KAKAO_API_KEY=asdasdads
KAKAO_WEB_SEARCH_URL = "https://dapi.kakao.com/search/web?query={}"

```python
header={
  "authorization":"Kakao{}".format(KAKAO_API_KEY)
}

import requests

response = requests.get(
  KAKAO_WEB_SEARCH_URL.format(""),
  headers=header
)

response.status_code

# response.content : html&css&js 같은 페이지 코드를 가져올 때 사용
# response.json()  : 시리얼라이즈 된 json 데이터를 자동으로 디시얼리라이즈 해줌
datas = response.json()
datas

datas.keys()

documents = datas['documents']
documents

# JSONArray를 Pandas 데이터 프레임으로 만들기
import pandas as pd

pd.DataFrame(documents)
```

# 02. HTML 스크래이핑

```python
html_str = """
<html>
  <head>
    <title>안녕하세요</title>
  </head>
  <body>
    <div id="container">
      <p class='p1'>hello</p>
      <p>Bye</p>
    </div>
  </body>
</html>"""
```

- html 형식의 문자열 내에 원하는 데이터가 존재
- HTML Element에 원하는 데이터가 있다.

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_str,"html.parser")
soup
```

## find

- find("태그명", "속성 값을 딕셔너리로 표현") : 한 개의 엘리먼트 찾기
- find_all("태그명", "속성 값을 딕셔너리로 표현") : 여러 개의 엘리먼트 찾기

```python
container_div = soup.find("div",{"id":"container"})

soup.find_all("p")

soup.find("p")

# 클래스가 p1인 p 엘리먼트를 모두 찾아보기
soup.find_all('p', {'class': 'p1'})

# 텍스트 추출
#  - 반드시 element 객체인 상태에서만 가능
soup.find('p', {'class': 'p1'}).text

# 두 개의 p 태그 내에 있는 텍스트 추출하기
p_tags = soup.find_all("p")
print(p_tags[0].text)
print(p_tags[1].text)

for p in p_tags:
  print(p.text)
```

## 선택자(Selector)를 사용해서 찾기

- select("선택자") : 선택자에 의해 엘리먼트를 여러 개 선택
- select_one("선택자") : 선택자에 의해 엘리먼트를 한 개만 선택

```python
# select_one을 이용해 .p1 찾기
soup.select_one("#container > .p1")

container_div.select_one(".p1")

soup.select("#container > p")
```

## 텍스트, 속성 추출

```python
# Bye만 추출해 보세요
soup.select("#container > p")[-1].text

# .p1을 가져오고 싶으면?
soup.select_one("#container > .p1").get("class") # get(속성명)

soup.select_one("#container > .p1")['class']
```

## 네이버 환율 정보 스크래이핑

```python
import requests
from bs4 import BeautifulSoup

NAVER_FINANCE_URL="https://finance.naver.com/marketindex/"

response=requests.get(NAVER_FINANCE_URL)
soup=BeautifulSoup(response.content,'html.parser')

# 스크래이핑 결과물을 데이터 프레임으로 만들어 주기
exchange_list = soup.select_one("#exchangeList")
exchange_list

fin_list = exchange_list.find_all("li") # exchange_list.select("li")
len(fin_list)

sample_li = fin_list[0]
sample_li
```

# 03.G마켓 베스트 상품 크롤링

태그명:nth-child(n)

```python
# 상품명
best_item_sample.select_one("a.itemname").text

# 이미지 url 따기
best_item_sample.select_one("img.lazy")

# src 가져오기 , src는 비동기화 상태일 경우 이미지가 없을 수 있음. data-original로 가져올것
image_url = "https:"+best_item_sample.select_one("img.lazy")['data-original']
print(image_url)

from urllib.request import urlretrieve

urlretrieve(image_url, "gmarket_image.png")
```

# 04. 사이트 API 크롤링

```python
# 응답을 어떻게 받았을까? - content-type 확인하기
data = response.json()
data

data['datas'][0]['closePrice']

# 개발자툴에서 네트워크 , fetch확인

import pandas as pd

kospi_df = pd.DataFrame(price_info_datas)
kospi_df.tail()
# tail() - 마지막 5개 자료 호출
# head() - 초반에 5개 자료 호출

# 비교연산자 가능
kospi_df_0329 = kospi_df[kospi_df["localDate"] >= "20230101"]
kosdaq_df_0329 = kosdaq_df[kosdaq_df["localDate"] >= "20230101"]
usd_df_0329 = usd_df[usd_df["localDate"] >= "20230101"]
```

> 2023.03.31

# scrapy Framework

- HTML
- API
- Selenoum

Iterator
Generator
yield

# Xpath

# Spider

- 크롤링 봇

scrapy startproject name

scrapy genspider GmarketNsetSellers gmarket.co.kr

settings의 모듈 위치 확인

ITEM_PIPELINES

- 저장한 데이터의 후처리 작업 수행을 하는 위치

items.py 와 spider.py 중요

- items.py : 모델- > 크롤링 할 항목

파이프라인 추가

- settings.py 65번줄

- scrapy crawl GmarketBestSellers : spider의 이름

slack

- 수신 webhook

저장
scrapy crawl GmarketBestSellers -o gmarket.csv -t csv

복습 - 딥러닝 이전까지 끝내기
1.python

- for문
- sequence
  - list,tuple,set,dict
  - iterable
  - 함수 , def -> parameter , Default parameter , keyword parameter , position parameter
- 클래스 -> 기본 (멤버변수,메소드,객체) , 상속의 개념
- import , from

  2.pandas
