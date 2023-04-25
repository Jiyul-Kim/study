# 웹 개발이란?

## 인터넷이란?

**연결된 장치 묶음**

- 오늘날에는 모든 장치가 그 묶음에 포함됨.
- 그 묶음들은 서로 어떻게 소통할까?

## 라우팅

1의 인터넷이 라우팅을 통해 2의 인터넷에 연결해주는 각각의 기기는 IP 주소로 개별 시스템을 식별함

> 인터넷은 모든 것을 가능하게 하는 인프라. like 고속 도로 > 이게 모여서 웹이 되는 거임

## 웹이란?

HTTP (프로토콜)
: 특정한 의사 소통이 이루어지는 방식에 대한 일련의 표준화된 규칙

## 브라우저의 역할

우리의 정보를 웹 페이지에 보기 좋게 표시하는 것

## 클라이언트

- 서버에서 무언가를 요청하는 장치인 컴퓨터
- 우리는 서버에 리소스를 **요청**함

## 웹이 우리에게 보여지는 과정

우리는 어떤 **HTTP**를 통해 **요청**을 보냄 → 서버가 그걸 받고 **HTML, CSS, JavaScript**로 응답함 → **브라우저**가 해당 지침을 받아 **웹 페이지를 구축**

## FE / BE

주방에서 일하는 사람은 BE, 서빙하고 그런 사람은 FE

<img src="https://github.com/Jiyul-Kim/study/blob/main/images/Untitled.png" width="50%" height="50%" />
### FE

브라우저에서 실행되는 도구 (html/css/js) 에 중점

### BE

브라우저가 아닌 서버에서 실행되는 것에 초점

---

# HTML / CSS /JS

브라우저가 이해하는 유일한 언어

## HTML - 명사 / 구조

> 페이지의 내용을 설명 (markup laguague)

### Tag (element) ###

1. p (paragraph)
2. h 1 ~ 6

- 이걸로 글자 크기를 주지 말자. CSS에서 주는게 훨~~~ 씬 나음.
- h1은 한 페이지 당 하나

3. list (ol, ul > li)

   - ol (Ordered List)
   - ul (Unordered List)

4. a (anchor)

   - href <- 링크 연결 어트리뷰트

5. img

   - src="" <- 소스 경로 어트리뷰트
   - alt="" <- 이미지에 부가 설명 넣는 어트리뷰트. 스크린 리더가 읽어 줌.

6. span
7. div

### Inline and Block ###

<img src="https://github.com/Jiyul-Kim/study/blob/main/images/inlineVSblock.png"  width="40%" height="40%"/>

inline은 한 라인에 모든 요소들이 나오는거임. 
CSS에서 변경 가능 

### 제너릭 컨테이너 ###
**span, div**
1. div
   + 무언가를 잡아두는, 또는 요소를 그룹화 하는 제너릭 컨테이너 
   + block
2. span
   + inline 

### Entities (엔티티) ###
> ex. & #9824;

키보드로 치기 어려운 특수문자 등을 html에 코드로 입력하는 것 

https://www.freeformatter.com/html-entities.html

### 시멘틱 마크업 ###
```
시멘틱: 의미와 관련된 
의미 있는 마크업, 그 요소의 내용의 의미에 관련된 마크업 
```

옛날에는 div 위주로 쓰였는데, 최근에는 여러 tag가 나오면서 main, header, nav, footer, section 등... 의 이름만 보면 무슨 기능을 하는지 아는 tag들이 나왔음.
이처럼 **딱 보고 뭔지 알 수 있게끔** 의미 있게 쓰이는 마크업이 *시멘틱 마크업*

사람들 마다 다르게 써서 좀 헷갈릴 수 있음!! 

1. div 대체
   + main 
      + 페이지의 주요 내용
      + 반복되는 내용 X

2. nav
   + 페이지에서 내비게이션 링크를 제공하는 것들을 나타냄

3. section
   + 내용의 한 부분 웹 사이트의 독립적인 부분 

4. article
   + 독립적으로 나뉠 수 있거나 다시 사용될 수 있는 것 
   + 날씨 위젯 같은 거 

5. aside
   + 사이드바 같은 거  

6. header / footer

7. figure
   + 이미지에 캡션 달아줄 수 있는 것 

## CSS - 형용사 / 어떻게 보여줘야하는지 설명 ##
    - HTML 요소, 페이지의 내용 설명을 **보조**
    - 글자 크기 폰트 등 그런 디자인 적 요소
## JS - 동사 / 논리, 동작, 동사 구축 ##

상호작용을 . 뭔가를 작동하고 있게 해줌.
