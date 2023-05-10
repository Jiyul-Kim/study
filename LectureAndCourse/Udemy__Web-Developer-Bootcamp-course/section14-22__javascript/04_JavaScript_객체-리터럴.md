# 230506 TIL


# 객체 리터럴이란? (like python dictionary! 🌟)
정보를 저장하고 여러 타입이나 조각의 데이터를 결합할 수 있다는 점에서 배열과 유사한 데이터 구조를 가졌다.

- 순서가 중요한 배열과 다르게, **순서가 중요하지 않다.**

- 객체는 키 - 값 또는 프로퍼티라는 걸 이용해서 데이터가 저장된다.
- 자루 안에 여러 쌍들이 들어있다고 생각하면 편해요.
- 정보에 **레이블**을 넣어줘서 이 정보가 어떤 정보였는지 **쉽게 파악할 수 있게 해준다.**

    - 여기서 배열과의 차이점이 생긴다. 배열의 경우
    `[23, 2001, 240]` 이렇게만 적어두면 이 데이터가 뭐였는지 알 수 없게된다.
    - 객체는
    `{age:23, birthYear:2001, footSize:240}` 이런식으로 저장하게 돼서 이 데이터가 뭔지 파악하기 쉽다!

## 생성
```js
const person = {
    fistName : "Jiyul",
    lastName : "kim"
    age : 23,
    tags : ['#infj', '#animation'],
    isFunny : false
};
```
> ⚠️ key는 모두 **string**으로 만들어진다!
<hr>

## 호출
### key 호출
```js
person["lastName"]
>>> "kim"
// key가 스트링이기 때문에 [""] 따옴표 넣어주는 거임.
```
```js
// method 처럼 호출하기
person.lastName
>>> "kim"
```
<hr>

## 수정
```js
const midterms = {
    doyoon : 50,
    jiyul : 20
};

// 채점하고 보니 지율의 점수가 39점이었던 거임. 

midterms.jiyul = 39
> 39
```
<hr>

## 배열 + 객체
### 배열에 객체를 넣었을 때
```js
const shoppingCart = [
    {
        product: "젠가",
        price : 10000,
        qyt : 1,
    },
    {
        product: "껌",
        price : 1000,
        qyt : 3,
    },
    {
        product: "물",
        price : 2300,
        qyt : 10,
    }
]
```
### 객체에 배열을 넣었을 때
```js
const student = {
    firstName : "yoon",
    lastName : "Kim",
    strengths: ["run", "game"],
    exams : {
        midterm: 90,
        final : 85
    }
}
```