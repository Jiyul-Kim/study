# 230506 TIL
# Not A Number (NAN)
> 0 / 0 <br> 1 + NaN

- 수학과 산수에서 무의미 하거나 혹은 불가능해서 정의할 수 없는 것.
- 숫지로 간주된다.

<br>
<br>

# Varialbles
## let 
```js
// basic form
let someName = value ;
```
## const (상수)
contstant의 줄임말

**항상 일정한 값이다. 바뀌지 않는다!**

> ### 그래서 왜 쓰는건데?ㅍ
> <br> 예로 들어 원주율, 변동률 같이 변하지 않는 값들에 유용하게 쓰일 수 있다.


### 변수 이름에 대한 규칙
1. 첫 문자는 소문자여야 하고, 숫자나 특수문자가 나오면 안된다.
2. 단어를 여러 개 써야 한다면 wordWord 라고 쓰면 된다.
3. 불리언 변수를 쓸 때는 ' isWordTrue ' 이런 식으로 쓰면 의미 전달에 좋다.

<br>
<br>

# Primitivce Types
## Booleans
true or flase <br>
1 or 0
## Strings (문자열)
> = TEXT 🖊️
```js
let name = "jiyul"
```
<br>

🤔 Q. 만약에 나는 "졸리다." 라고 말했다. 이런식으로 큰따옴표를 포함하고 싶다면?
```js
let say = '나는 "졸리다." 라고 말했다.';
```
이런 식으로 작은 따옴표로 문자열을 묶어주면 됨.

### 문자열은 인덱스 되어 있다.
<br>

>|C|H|I|C|K|E|N|
>|-|-|-|-|-|-|-|
>|0|1|2|3|4|5|6|

### 문자열은 서로 합칠 수 있다.
``` js
let phoneName = "iphone";
let version = "11 pro";

phoneName + version
>>> iphone11 pro
// 여기서 잠깐! string + stirng은 띄어쓰기가 된 채로 출력되지 않음. 파이썬과 동일하니까 참고하기 
```

### 문자열과 숫자를 더하면 어떻게 될까?
파이썬의 경우는 TypeError가 뜸. 서로 다른 타입이라서!

그런데 JS는 신기하게 더하기가 된다. 대신, 숫자를 string으로 자동 변환해서 string + string 형태가 되는 것.

<hr>

### METHOD
> thing.method(arg)

+ 문자열은 여러 개를 연달아 쓸 수 있음.
<br> ex. name.toUpperCase().trim ()
<br> 먼저 쓴 것 부터 실행되니 참고하기~

#### toUpperCase / toLowerCase
1. 대문자로 변환
    ```js
    let msg = "idontwannabeyouanymore";
    msg.toUpperCase()

    >>> 'IDONTWANNABEYOUANYMORE'
    ```
2. 소문자로 변환
    ```js
    let msg = "IDONTWANNABEYOUANYMORE";
    msg.toLowerrCase()

    >>> 'idontwannabeyouanymore'
    ```
#### Trim
문자열 좌우에 있는 공백을 전부 깎아내주는 메쏘드

```js
let msg = "   hello my name is jiyul   ";
msg.trim()

>>> 'hello my name is jiyul'
```
#### indexOf
문자열에서 주어진 인수가 나타나는 문자열 인덱스와 그 자릿수를 반환한다.
```js
"언제까지 어깨 춤을 추게 할거야!".indexOf("언") // 0
"언제까지 어깨 춤을 추게 할거야!".indexOf("!") // 17
"언제까지 어꺠 춤을 추게 할거야!".indexOf("무") // -1 (not)
```

#### Slice (파이썬의 string[fist:end]와 같음)
한 개 이상의 인수를 받을 수 있고, 받은 인수 만큼 문자열을 잘라서 분리해낼 수 있다.

```js
let msg = "언제까지 어깨 춤을 추게 할거야!";
msg.slice(5)

>>> '어깨 춤을 추게 할거야!'

msg.slice(5, 7)
>>> '어깨'
```

#### replace
> replace("바꿔지는 문자", "바꾸려는 문자")

```js
let msg = "언제까지 어깨 춤을 추게 할거야!";
msg.replace("어깨", "무릎")

>>> '언제까지 무릎 춤을 추게 할거야!'
```

#### repeat
문자열을 반복하고 싶을 때 사용
> repeat (count)

```js
"ha".repeat(10)
>>> "hahahahahahahahahaha"
```

### Template Literals (파이썬의 formating과 비슷한듯!)
문자열 안에 표현식을 내장할 수 있는 문자열들 만들고 해당 표현식은 평가된 후에 문자열로 바뀐다.

1. 백틱 기호를 쓴다. **`**
2. 기본 구조
    > ```js
    > `text ${}`
    > ```


3. 예시
```js
let product = "와우 껌";
let price = 1000;
let qty = 5;

`당신은 ${qty}개의 ${product}를 샀습니다. 총 금액: ${qty * price} 입니다.`

>>> '당신은 5개의 와우 껌를 샀습니다. 총 금액: 5000 입니다.'

```

## Null & Undefined
### undefined
정의된 값이 없을 때 출력.
<br> JS : "에.. 주인님 뭘 원하시는지 모르겠고 정의된 것도 없는데요.. 🤷‍♀️"
<br> 꽤 자주 본다고 합니다.

### null
일부러 값을 지정하지 않는 것으로 설정 
<br>자주 보는 타입은 아니여유

<br>
<br>

# Math Object
## method
### floor : 소수점 삭제
```js
Math.floor(23.90);
>>> 23
```
### random : 0과 1 사이에 소수점을 랜덤으로 생성
```js
Math.random();
>>> 0.8595389172042904
```
#### 만약에 1 이상의 랜덤 값을 얻고 싶을 땐..?
좀.. 황당함.
```js
Math.floor(Math.random()*5);
>>> 3 // 대신에 0 ~ 4 까지의 수만 나오니 1 ~ 5 가 나오길 원하면 그냥 여기에 +1 해주면 됨!
```
### pow : 제곱
```js
Math.pow(2, 3);
>>> 8
```