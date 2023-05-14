# 230514

# 비동기식 JS

## CallStack

### 들어가기 앞서 CallBack 이란?

> JS가 뒤에서 사용하는 매커니즘 혹은 기능

---

**콜 스택이란?**

> JS 해석기가 사용하는 매커니즘으로 여러 함수를 호출하는 스크립트에서 해당 위치를 추적한다.
> <br> 그리하여 JS가 위치를 알 수 있다.
>
> 쉽게 설명하자면 읽던 곳을 표시하기 위해 손👆이나 책갈피 등을 쓰는 것과 같음

### Stack

> 컴퓨터 과학의 기본 데이터 구조
> <br> 후입선출 (LIFO) 데이터 구조로 알려져 있다.
>
> <br> 즉, **가장 늦게 추가된 것을 가장 먼저 제거한다.**

### 예시

```js
const multiply = (x, y) => x * y;

const square = (x) => multiply(x, x);

const isRightTraiangle = (a, b, c) => {
  return square(a) + square(b) === square(c);
};

isRightTraiangle(3, 4, 5);
```

이런 코드를 예시로 생각해보자.

1. `isRightTraiangle(3, 4, 5)` 값을 받아 `isRightTraiangle` 함수는 `3+square(4) === square(5)`의 과정을 가진다.
   ![](2023-05-14-17-41-03.png)
2. 그 다음, square 함수를 호출 및 **스택을 쌓고**, multiply에게 `3` 의 값을 전달해준다.
   ![](2023-05-14-17-42-19.png)
3. `multiply`가 `multiply(3, 3)` 값을 전달 및 **스택을 쌓고** `9` 라는 값을 도출한다.
   ![](2023-05-14-17-43-32.png)
4. `multiply`에서 나온 `9`라는 값으로 `multiply`의 스택은 **제거**되고 `square`에게 9의 값을 전달해준다.
   ![](2023-05-14-17-44-31.png)
5. `square`는 값을 전달해준 뒤 **제거**되고 `isRightTraiangle`은 `9+square(4) === square(5)`라는 `square(a)` 결과를 내준다.
   ![](2023-05-14-17-45-50.png)
6. 이 과정을 계속 진행하다보면 결국 JS는 최종 결과인 **true**를 내준다.

---

🌻 JS는 콜 스택에 함수 호출을 **추가**하고 값이 반환될 때마다 **삭제**한다.

<hr>
<br>
서버에 요청을 보내고 DB 혹은 서버에서 응답을 받고 작동하거나 작동하지 않는 일이 있다고 가정을 한다. 그러면 5초 정도가 소모된다.
<br> 이 과정에서 사용자는 5초, 10초 이상을 기다리게 되고 **사용자에게는 좋은 경험은 아닐 것이다.**

## JS가 아닌 브라우저가 실제로 작업하고 있는 것이다.

`브라우저`는 JS로 작성되는 것이 아닌 대개 `C++`같은 언어로 작성된다.

=> 그래서 **JS가 할 수 없는 일**이 있다. JS는 브라우저에게 특정 작업을 처리하도록 넘긴다.

## WebAPI

> `브라우저는 Web APIs가 있다.` **Web APIs**는 일반적으로 JS에서 호출하여 브라우저로 전달하는 방법이다.

### 작동 방식

```js
console.log("Sending request to server!")
setTimeout(function() {
    console.log("Here is your data from the server...")
}, 3000)
console.log("I AM AT THE END OF THE FILE!")

>>> 
'Sending request to server!'
'I AM AT THE END OF THE FILE!'
// 3초 후
'Here is your data from the server...'
```

1. JS는 `"Sending request to server!"` 콘솔 로그를 인식하고 출력해준다.<br>
![](2023-05-14-18-23-06.png) 

2. JS의 콜 스택이 WEb API를 인식한다. 
![](2023-05-14-18-32-41.png)
![](2023-05-14-18-33-00.png)
3. JS: 브라우저야.. 나 `setTimeout`이 뭔지 모르겠성 ㅎ 타이머로 3초로 설정해주라 ㅋ 

4. 브라우저: ㅇㅋ 3초 뒤에 실행함. 

5. JS는 그 다음일을 한다. `"I AM AT THE END OF THE FILE!"`을 출력한다.
![](2023-05-14-18-33-34.png)

6. 브라우저는 시간을 체크하고 있고, 시간이 지나면 `"Here is your data from the server..."`를 출력해준다.

```js

```

```js

```

```js

```

```js

```

```js

```

```js

```
