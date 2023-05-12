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
const btn = document.querySelector('#b2')
btn.onclick = function(){
    console.log("클릭하새요")
}
function scream() {
    console.log('뿌애앵')
}
btn.onmouseenter = scream;
```
```js
document.querySelector("h1").onclick =() =>  alert('h1을 클릭하셨어요!')
```
#### 단점
동일한 이벤트에 대해 두 개의 서로 다른 콜백 함수를 지정할 수 없다.

### addEventListener (method)
1. 요소 선택
```js
const butoon = document.querySelector ('h1');
```
2. 메소드 사용
```js
button.addEventListener('click', () => alert('h1을 클릭하셨어요'))
```
감지하고 싶은 어떤 이벤트든 전달할 수 있다.
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