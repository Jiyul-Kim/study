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


```js
```