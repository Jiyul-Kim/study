# 230512 TIL

# EVENTS

> 사용자들이 하는 행동에 반응하는 작업

## 이벤트 사용 방법

### 인라인 이벤트

![](images/%EC%9D%B8%EB%9D%BC%EC%9D%B8%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EC%98%88%EC%8B%9C1.gif)

```html
<button onclick="alert('클릭하세욥!!')">클릭하세요!</button>
```

🤷‍♀️ 쓰면 안되는 이유

1. HTML 안에 JS를 쓰는 것은 이상하다.
   - 마크업이 길어지고, 쓸 때도 짜증(ㅋㅋ)이 난다.
   - 계속 따옴표 신경써주는 것도 여간 귀찮다.
   - 여러 이벤트를 넣을려면 계속 세미콜론을 넣어줘야 한다.
2. 동일한 동작을 하는 버튼이 있을 경우
   - 비효율적인 무한 복붙 <= 코드도 길어지기 시작..
   - 많은 양의 동작을 한 번에 바꾸기가 어려움. (코드만 많기 떄문에.)

### JS에 이벤트 작성

> 인라인 이벤트보다 더 나은 방법인 JS에 작성하는 방식이다.<br>
> function으로 기능을 전달해준다.

```js
const btn = document.querySelector("#b2");
btn.onclick = function () {
  console.log("클릭하새요");
};
function scream() {
  console.log("뿌애앵");
}
btn.onmouseenter = scream;
```

```js
document.querySelector("h1").onclick = () => alert("h1을 클릭하셨어요!");
```

#### 단점

동일한 이벤트에 대해 두 개의 서로 다른 콜백 함수를 지정할 수 없다.

### addEventListener (method)

1. 요소 선택

```js
const butoon = document.querySelector("h1");
```

2. 메소드 사용

```js
button.addEventListener("click", () => alert("h1을 클릭하셨어요"));
```

감지하고 싶은 어떤 이벤트든 전달할 수 있다.

## 이벤트와 this

### 왜 사용해야 하나요?

```js
const makeRandColor = () => {
  const r = Math.floor(Math.random() * 255);
  const g = Math.floor(Math.random() * 255);
  const b = Math.floor(Math.random() * 255);
  return `rgb(${r}, ${g}, ${b})`;
};

const buttons = document.querySelectorAll("button");

for (let button of buttons) {
  button.addEventListener("click", function () {
    button.style.backgroundColor = makeRandColor();
    button.style.color = makeRandColor();
  });
}

const h1s = document.querySelectorAll("h1");
for (let h1 of h1s) {
  h1.addEventListener("click", function () {
    h1.style.backgroundColor = makeRandColor();
    h1.style.color = makeRandColor();
  });
}
```

> button과 h1에 사용되는 이벤트가 동일하게 쓰일 떄, 하드코딩을 위해서 쓰입니다.

### 제네릭 함수와 this

```js
for (let button of buttons) {
  button.addEventListener("click", colorize);
}

for (let h1 of h1s) {
  h1.addEventListener("click", colorize);
}

function colorize() {
  this.style.backgroundColor = makeRandColor();
  this.style.color = makeRandColor();
}
```

## 이벤트 객체 && 키보드 이벤트

### 키보드 이벤트

> 게임의 키보드 이벤트 처럼, 키보드로 입력한 내용을 리턴해줌.

#### KeyDown && KeyUp

```js
const input = document.querySelector("input");
input.addEventListener("keydown", function () {
  console.log("keydown");
});
input.addEventListener("keyup", function () {
  console.log("keyup");
});
```

![](images/keydown_keyup.gif)

### 키보드 이벤트 값 얻기

```js
const input = document.querySelector("input");
input.addEventListener("keydown", function (e) {
  console.log(e);
});
```

![](images/2023-05-13-19-27-38.png)

> 우리는 `code` 와 `key` 요소에 주목해야한다.

![](images/2023-05-13-19-30-34.png)

노란색친 부분이 `code` 값이다.
> 🌟
> <br> 즉, 실제 키보드 **위치에** 대응하는 것은 `code`이다.
> <br>입력된 **값만** 뭔지 알아내려면 `key` 를 이용하면 된다.
## form 이벤트
### preventDefault
#### 사용되는 이유
폼에 url을 거니 button을 통해 폼에 걸린 url로 이동을 한다.
<br>그러나 로그인이 실패할 경우에도 url로 이동되는 것을 막기 위해 해당 메서드를 이용한다.

```js
const tweetForm = document.querySelector("#tweetForm")
tweetForm.addEventListener('submit', function(e){
    e.preventDefault()
})
```
![](images/preventDefault.gif)
```js

```
