# 230508 TIL
<details>
<summary>목차</summary>

- [Callback Method](#callback-method)
  * [FOREACH](#foreach)
  * [MAP](#map)
  * [ARROW Function](#arrow-function)
- [230509 TIL](#230509-til)
    + [암시적 반환](#------)
  * [time 관련 콜백](#time------)
    + [setTimeout (배열과는 상관 X)](#settimeout----------x-)
    + [setInterval](#setinterval)
  * [FILTER](#filter)
  * [EVERY && SOME / 불리언 메서드](#every----some----------)
    + [EVERY](#every)
    + [SOME](#some)
  * [REDUCE](#reduce)
    + [최댓값 구하기](#-------)
    + [초기값](#---)
  * [arrow + this](#arrow---this)

</details>

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
## MAP
> 콜백 함수를 수령해서 배열의 요소를 복제한다. <br><br>
> 그 다음 콜백의 반환 값을 이용해서 새로운 배열로 변한다.

```js
const texts = ["house", "go", "sleep"];
const caps = texts.map(function (t) {
    return t.toUpperCase();
})
texts; // ['house', 'go', 'sleep']
caps; // ['HOUSE', 'GO', 'SLEEP']
```

```js
const numbers = [1,2,3,4,5];
const doubles = numbers.map(function (num) {
    return num * 2
})

>>> doubles;
>>> [2, 4, 6, 8, 10]
```
## ARROW Function
> 함수를 정의하는 최신 구문
> <br> 기존의 함수 표현식보다 더 간결하다.

```js
// 기존의 함수 표현식
const add = function(x, y) {
    return x + y;
}
```
```js
// arrow (=>) 사용
const add = (x, y) => {
    return x + y;
}
```
만약 인수가 1개면 중괄호 안써도 상관없음. 그렇지만 규칙성을 위해서는 중괄호 넣는 것이 좋을 것 같다!


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
const add = (a, b) => a + b;
```

```js
const add = (a, b) => a + b;
```

## time 관련 콜백

### setTimeout (배열과는 상관 X)

> 실행을 연기 / 대기 / 중단 등을 하는 작업 일정에 관한 메소드

```js
// EX
setTimeout(() => {
  console.log("hello");
}, 3000); // 여기 만큼의 시간이 흐른 다음 출력
```

### setInterval

> 전달할 함수를 호출하는데 콜백을 매 특정 밀리 초 마다 호출하는 함수

```js
setInterval(() => {
  console.log(Math.random());
}, 2000);

// 값이 2초 간격으로 출력됨
```

그럼 setInterval를 멈추게 하고 싶으면 어떻게 해야할까?

```js
const ID = setInterval(() => {
  console.log(Math.random());
}, 2000);

clearInterval(id);
```

## FILTER

> 요소로 구성된 배열에서 필터링을 하거나 부분 집합을 모아 새 배열을 만드는데 쓰인다.
> <br> 원본 배열을 바꾸는 것은 아니다.

```js
// EX
const numbers = [1, 2, 3, 4, 5, 6, 7];

numbers.filter((n) => {
  return n === 4;
})[4];
```

## EVERY && SOME / 불리언 메서드

### EVERY

> 콜백의 내용에 따라 배열이 **모두 참**일 때 true를 반환한다. 만일 하나라도 false라면 every 메소드도 false를 반환한다.

```js
const exams = [80, 92, 75, 88, 87, 99];

exams.every(socre => socre >= 75);

>>> true
```

```js
const exams = [80, 92, 73, 88, 87, 99]; // 배얼에 75점 이하인 73점이 있다.

exams.every(socre => socre >= 75);

>>> false
```

### SOME

> 콜백의 내용에 따라 배열이 **최소 한 개 이상 true**인지를 테스트한다.
> <br> 어떤게 true인지는 알려주지 않는다. 단지 한 개 이상 true가 있다고만 알려주는 메소드.

## REDUCE

> 배열을 가져다가 점차 줄여가면서 마지막에는 결국 하나의 값만 남긴다.

```js
// EX
[3, 5, 7, 9, 11].reduce((accumulator, currentValue) => {
    return accumulator + currentValue:
});
```

| Callback   | accumulator | currentValue | return value |
| ---------- | ----------- | ------------ | ------------ |
| firstCall  | 3           | 5            | 8            |
| secondCall | 8           | 7            | 15           |
| thirdCall  | 15          | 9            | 24           |
| thirdCall  | 24          | 11           | 35           |

예시로 더 쉽게 배워보자.

```js
const prices = [1000, 500, 320, 1500, 2000];

let total = 0 ;
for(let price of prices){
    total += price
}

>>> 5320
```

```js
const prices = [1000, 500, 320, 1500, 2000];
const total = prices.reduce((total, price) => total + price);

>>> 5320
```
### 최댓값 구하기
```js
const prices = [1000, 500, 320, 1500, 2000];

const minPrice = prices.reduce((min, price) => {
    if (price < min){
        return price;
    }
    return min;
})

>>> 320
```
### 초기값
```js
const evens = [2, 4, 6, 8];
evens.reduce((sum, num) => sun + num, 100)

// reduce(내용, 초기값) => 인수가 두 개임
>>> 120
```
## arrow + this
> 일반 함수와 달리 화살표 함수에서 this 키워드는 다르게 동작한다.