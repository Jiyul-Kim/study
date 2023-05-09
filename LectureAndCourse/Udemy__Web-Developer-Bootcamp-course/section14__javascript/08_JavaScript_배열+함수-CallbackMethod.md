# 230508 TIL

# Callback Method
## FOREACH
> 배열에 있는 각각의 아이템이 함수에 전달되는 메소드
- for of 루프가 등장하기 전에는 훨씬 자주 쓰임

```js
// 쉽게 풀어쓴 버전
const numbers = [1,2,3,4,5];

function print(element){
    console.log(element)
}
numbers.forEach(print)

>>>
1
2 
... 5
```
```js
// 실제로는 이렇게 사용합니다.
const numbers = [1,2,3,4,5];

numbers.forEach(function (el){
    console.log(el)
})
```


<hr>

# 230509 TIL
### 암시적 반환
> return 값이 한 개 일 때, {return}을 쓰지 않고 간결하게 줄이는 방법
> <br> 꼭 **표현식이 하나여야 함.**
```js
const add = (a,b) => {
    return a + 
}
```
```js
const add = (a,b) => (
    a + b
)
```

```js
const add = (a, b) => a + b
```
## time 관련 콜백
### setTimeout (배열과는 상관 X)
> 실행을 연기 / 대기 / 중단 등을 하는 작업 일정에 관한 메소드

```js
// EX
setTimeout(() => {
    console.log("hello")
}, 3000) // 여기 만큼의 시간이 흐른 다음 출력
```
### setInterval
> 전달할 함수를 호출하는데 콜백을 매 특정 밀리 초 마다 호출하는 함수



```js
setInterval(() => {
    console.log(Math.random())
}, 2000);

// 값이 2초 간격으로 출력됨
```
그럼 setInterval를 멈추게 하고 싶으면 어떻게 해야할까?
```js
const ID = setInterval(() => {
    console.log(Math.random())
}, 2000);

clearInterval(id)
```
```js
```