# 230506 TIL

<details>
<summary>목차</summary>

- [비교 연산자](#------)
- [IF 구문](#if---)
  * [else if](#else-if)
  * [else](#else)
- [조건부 네스팅 (Nesting)](#---------nesting-)
- [Truth-y / False-y](#truth-y---false-y)
- [논리 연산자](#------)
  * [&& (AND)](#----and-)
  * [|| (OR)](#----or-)
  * [! (NOT)](#---not-)
- [SWITCH](#switch)
  * [break](#break)
  * [default](#default)
- [ETC.](#etc)
  * [console.log](#consolelog)
  * [JS 파일과 html 파일 연동](#js-----html------)
</details>

# 비교 연산자

연산자 | 설명 | 예시 | 결과
---------|----------|---------|---------
  &#62; | 보다 큰 | 3 > 2 / 2 > 2 | true / false
 &#60; | 보다 작은 | 3 < 2 / 3 < 3 | false
 &#62;= | 보다 크거나 같은 | 30 >= 31 / 30 >= 30 | false / true
  &#60;= | 보다 작거나 같은 | 30 <= 31, 30 <= 30 | true
  == | 값이 동일한 | 1 == 1 | true
  != | 값이 동일하지 않은 | 2 != 1 | true
  === | 값과 타입 모두 같은지 비교 | "1" === "1" | true
  !== | 값과 타입 모두 다른지 비교 | "1" !== 2 | true  

유니코드에 따라서 문자나 특수문자도 비교를 할 수 있음.
ex. 대문자가 소문자보다 숫자가 더 작음

> 초반에는 삼중 등호를 이용하는 게 좋다고 합니다 ^_^



# IF 구문
```js
let rating = 3;
if (rating === 3) {
    console.log("참")
}
```
## else if
if가 거짓일  경우 else if로 넘어간다.
```js
let rating = 2;
if (rating === 3) {
    console.log("결과는 3")
}
else if (rating === 2) {
    console.log("결과는 2")
}

>>> "결과는 2"
```

## else
if와 else if 모두가 거짓일 때 마지막 항목인 else가 실행된다.
```js
let rating = 4;
if (rating === 3) {
    console.log("결과는 3")
}
else if (rating === 2) {
    console.log("결과는 2")
}
else {
    console.log("해당 범위 안에 없는 값입니다.")
}

>>> "해당 범위 안에 없는 값입니다."
```
# 조건부 네스팅 (Nesting)
조건이 중첩된다면 if 안에 또 다시 if를 써줄 수 있습니다.

> 단, 조금 무거워질 수도 있습니다.

# Truth-y / False-y
Truthyness / Falseness

JS에선 다음 경우를 제외하면 모두 truthy이다.
- false
- 0
- "" (emthy string)
- null
- undefined
- NaN

# 논리 연산자
> 다른 두 표현식을 합쳐 여러 논리를 하나로 결합함으로써 하나의 큰 논리를 형성한다.

## && (AND)
**둘 다 참이여야 한다.**
<br>`true && true`

👌 예제. <br>
엄마가 놀아도 된다고 허락을 해주심. 대신! **숙제와 방 청소를 해야만 놀 수 있다고 하심** 이럴 때 && 으로 표현해줄 수 있는 것. <br>

`"숙제 하기" && "방청소 하기"`


## || (OR)
**한 쪽만 참이어도 된다.**
<br>`true || false` > **true**

👌 예제. <br>
엄마가 놀아도 된다고 허락을 해주심. **숙제를 하거나 방 청소를 하면 놀 수 있다고 하심** 이럴 때 && 으로 표현해줄 수 있는 것. <br>

`"숙제 하기" || "방청소 하기"`


## ! (NOT)
값을 반전시키는 역할 <br>
`false = false <br>
!false = true`

# SWITCH
구문이 어렵게 생겨서 많이 쓰이지도 않음. 구문 외우지 마세요!
<br>
<br>

사용 예시.
```js
const day = 2;
switch (day) {
    case 1:
        console.log("월");
    case 2:
        console.log("화");
    case 3:
    console.log("수");
}

>>> "화", "수"
```
지정한 case 부터 계속 출력 된다. <br>

Q. 🤨 그럼 화요일만 출력하게는 어떻게 하는데?
## break
```js
const day = 2;
switch (day) {
    case 1:
        console.log("월");
        break;
    case 2:
        console.log("화");
        break;
    case 3:
        console.log("수");
        break;  
}

>>> "화"
```
## default
유효한 case가 모두 없다면 디폴트 값으로 넘어가게 됨.
```js
const day = 6;
switch (day) {
    case 1:
        console.log("월");
        break;
    case 2:
        console.log("화");
        break;
    default:
        console.log("님!! 뭘 표현하고 싶은지 모르겠음!!")  
}

>>> "님!! 뭘 표현하고 싶은지 모르겠음!!"
```

<br>
<br>

# ETC.
## console.log
> console.log (출력 내용)

## JS 파일과 html 파일 연동

1. app.js 파일을 만든다.
2. html 파일을 만들고, `<head> 나 <body>`에 `<script>` 태그를 통해 연결해준다.
(주로 body 가장 밑에 둔다.)
```html
<body>
    <script scr="app.js"></script>
</body>
```