# CSS란?

CSS는 Cascading Style Sheets의 약자로 기본적인 스타일이 이미 지정된 HTML 요소를 개발자가 직접 다양한 스타일로 디자인할 수 있는 언어이다.

# CSS 기본 문법

CSS 문법은 크게 `셀렉터`와 `선언 블록`으로 나뉜다.

먼저 셀렉터로 스타일을 지정할 HTML 요소나 id, class 등을 선택한 뒤 그에 대한 스타일을 선언 블록인 중괄호{} 사이에 지정한다. 그리고 각각의 스타일 속성들은 세미콜론;으로 구분한다.

![](CSS%20기초.png)

# HTML에 CSS 적용하기

1. 인라인 스타일 (Inline Style)  
   HTML 태그 내에 `style 속성`을 이용하여 CSS를 지정할 수 있다. 이 방법의 경우 이미 스타일을 적용할 요소가 지정되어 있기 때문에 선택자 및 선언 블록없이 바로 스타일 속성값을 지정한다.

2. 내부 스타일 시트(Internal Stylesheet)  
   HTML 문서의 <head> 태그 내에 <style> 태그를 삽입하고 해당 태그 사이에 CSS 문법을 작성해 스타일을 지정할 수 있습니다. 이 경우 해당 HTML 문서에만 스타일이 적용됩니다.

3. 외부 스타일 시트(External Stylesheet)  
   HTML 문서 내부가 아닌 외부에서 CSS 파일을 작성했다면, HTML 문서의 <head> 태그 내에 <link> 태그를 삽입하여 HTML 문서에 CSS를 연결할 수 있습니다. <link> 태그의 rel 속성을 stylesheet로 지정하고 herf 속성으로 CSS 파일의 경로를 지정하여 연결할 수 있습니다.
