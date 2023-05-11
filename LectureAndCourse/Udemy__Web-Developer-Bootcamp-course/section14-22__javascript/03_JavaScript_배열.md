# 230506 TIL

<details>
<summary>목차</summary>

- [Array, 배열이란?](#array-------)
- [배열 구조](#-----)
  * [배열은 INDEX 되어 있다.](#----index------)
  * [막간의 TIP👍 배열에서 문자열 인덱싱 찾기](#----tip------------------)
  * [배열 재정의 하기](#---------)
- [배열 methods](#---methods)
  * [push - 배열 끝에 추가](#push-----------)
  * [pop - 배열 끝 요소 삭제](#pop-------------)
  * [shift - 배열의 시작에서 삭제](#shift--------------)
  * [unshift - 배열의 시작에서 추가](#unshift--------------)
  * [concat - 접합](#concat-----)
  * [includes - 배열에 특정 값이 포함되있는지 true와 false로 나타냄](#includes--------------------true--false-----)
  * [indexOf - 있으면 위치 값을, 없다면 -1 반환](#indexof-------------------1---)
  * [reverse - 배열 뒤집기](#reverse---------)
  * [slice - 배열의 일부 복사](#slice------------)
  * [splice - 기존 요소 제거 / 대체 / 추가 / 내용 변경](#splice-----------------------------)
  * [sort - 배열을 줄이는 매서드](#sort--------------)
    + [sort 기본 배열의 주의점](#sort-----------)
- [JS는 배열의 내용끼리 비교하지 못한다.](#js-------------------)
- [배열은 const의 내용을 바꿔줄 수 있다.](#----const--------------)
- [중첩 배열 (nasted)](#-------nasted-)

</details>

# Array, 배열이란?
1. 값의 집합이다.
2. 값의 순서 있는 집합이다.
3. 예시
    > 최신 댓글 / 더 어려워지는 게임 레벨 / 재생목록의 노래들 

# 배열 구조
`let variable = []`
```js
let colors = ["red", "orange", "yellow"];
```
> 배열에는 모든 타입을 넣을 수 있다!
> `["color", 12, undifiend, null]`

## 배열은 INDEX 되어 있다.
<br>

>|도윤|호영|시진|재경|혜성|우진|라움|하율|
>|-|-|-|-|-|-|-|-|
>|0|1|2|3|4|5|6|7|

```js
let friends = ["도윤", "호영", "시진", "재경", "혜성", "우진", "라움", "하율"];
friends[0];

>>> "도윤"
```
## 막간의 TIP👍 배열에서 문자열 인덱싱 찾기
```js
friends[0][1];

>>> "윤"
```
## 배열 재정의 하기
```js
let friends = ["도윤", "호영", "시진", "재경", "혜성", "우진", "라움", "하율"];
friends[0] = "지율"; // 도윤 > 지율로 변경
friends[8] = "도윤"; // 마지막에 도윤 추가

>>> ["지율", "호영", "시진", "재경", "혜성", "우진", "라움", "하율", "도윤"]
```

> 타입도 바꿀 수 있고, 값도 바꿀 수 있음!

<br>
<br>

# 배열 methods
## push - 배열 끝에 추가
`friends.push("희정");`
## pop - 배열 끝 요소 삭제
`friends.pop()`
## shift - 배열의 시작에서 삭제
`friends.shift()`
## unshift - 배열의 시작에서 추가
`friends.unshift("지율")`


## concat - 접합
- 두 개를 합쳐서 새 문자열을 만드는 것
```js
let cats = ["레어", "삼촌"];
let dogs = ["초코", "레오"];

cats.concat(dogs);
["레어", "삼촌", "초코", "레오"]
```

## includes - 배열에 특정 값이 포함되있는지 true와 false로 나타냄
```js
let cats = ["레어", "삼촌"];
cats.includes("레어");

>>> true
```

## indexOf - 있으면 위치 값을, 없다면 -1 반환
```js
let cats = ["jiyul", "doyoon", "heejung", "jeakyu"];
cats.indexOf("jeakyu");
>>> 3
cats.indexOf("jooa");
>>> -1
```

## reverse - 배열 뒤집기
> ⚠️ 주의 ⚠️ 배열을 완전 깨트림.
```js
let cats = ["레어", "삼촌"];
cats.reverse();

>>> ["삼촌", "레어"]
```

## slice - 배열의 일부 복사
```js
values.slice() // 전체 복사
values.slice(n, m) // start와 end를 적어줄 수 있음
```
```js
// 예시
let friends = ["도윤", "호영", "시진", "재경", "혜성", "우진", "라움", "하율"];
friends.slice(3,6);

>>> ['재경', '혜성', '우진']

let girls = friends.slice(-2)
>>> girls = ['라움', '하율']
```


## splice - 기존 요소 제거 / 대체 / 추가 / 내용 변경
> 원래 배열 자체를 변경한다. 복사본을 만들지 않음!!

> ```js
> let items = array.splice(start, (deleted), ("추가할 요소"))
>```
만약 삭제할 요소가 없고 추가만 한다면 `(1, 0, "ㅁ")` 이런식으로 쓰면 됨.

<br>
배열 중간에 넣는게 효율적이지도 않아서 splice를 자주 쓰지 않음

## sort - 배열을 줄이는 매서드
숫자는 작은 것에서 큰 순으로, 문자는 소문자에서 대문자로
### sort 기본 배열의 주의점
```js
let scores = [1, 435, 45,3, 64, 787, -12, 3457, 89];
scores.sort();

>>> [-12, 1, 3, 3457, 435, 45, 64, 787, 89]
```
뭔가 이상하게 정리되지 않음? 왜냐면 sort는 숫자 **맨 앞 자리**를 기준으로 숫자를 정리해줌

그래서 이건 함수로 해결해줘야한다.

# JS는 배열의 내용끼리 비교하지 못한다.
```js
// 예시
[] === []; // false
[1] === [1]; // false
```
> 실제로 비교하는 건 메모리에서 참조되는 값이다. (일종의 데이터 주소 값)

# 배열은 const의 내용을 바꿔줄 수 있다.
> const 자체를 바꾸는 것은 안되지만, 해당 배열의 콘텐츠를 바꾸는 것은 아주 무관하다!
```js
const nums = [1, 2, 3];
nums.push(4);

>>> [1, 2, 3, 4]

// 만약에 nums 자체를 바꾼다면?
nums = 1;
>>> TypeError
nums = [1, 2, 3, 4];
>>> TypeError
```

<br>

# 중첩 배열 (nasted)
```js
const board = [
    ['O', null, 'X'],
    [null, 'X', 'O'],
    ['X',  'O', null]
]
```
🤔 만약 두 번째 줄의 null을 바꿔주고 싶다면 어떻게 할까?
> board[1] = [null, 'X', 'O']<br>
> board[1][0] = [null]