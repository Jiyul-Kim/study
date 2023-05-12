# 230507 TIL

<details>
<summary>목차</summary>

- [함수](#--)
  * [함수 만들기](#------)
  * [인수 (arguments)](#----arguments-)
    + [메서드는 곧 함수다](#----------)
    + [인수는 식별 능력이 없다.](#-------------)
    + [두 개 이상의 인수 받기](#-------------)
      - [만약 두 개 이상의 인수 중 하나만 입력한다면?](#--------------------------)
  * [RETURN](#return)
    + [return의 역할 1. 값 함수에 저장](#return-----1---------)
    + [return의 역할 2. 함수 끝내기](#return-----2-------)
    + [return은 하나의 값만 출력한다.](#return-------------)
- [230508 TIL](#230508-til)
  * [Scope (범위) / python의 지역변수, 전연벽수 얘기](#scope--------python---------------)
    + [⚠️ 함수 안에서 정의된 변수들은 그 함수로 범위가 한정되어 있다.](#------------------------------------)
    + [Block](#block)
      - [🤷‍♀️ var](#------var)
    + [렉시컬 범위](#------)
      - [그러나 부모 함수는 자식 함수의 변수를 가져다 쓸 순 없다.](#--------------------------------)
  * [함수 표현식](#------)
  * [고차 함수](#-----)
    + [함수를 인수로 받는 함수](#-------------)
    + [반환 함수](#-----)
      - [팩토리 함수](#------)
  * [메소드(method) 만들기](#----method-----)
    + [객체에 함수 넣기](#---------)
      - [속기법 (shorthand)](#-----shorthand-)
  * ["THIS"](#-this-)
    + [어떤 객체를 가르키는 지가 중요하다! (결과값이 달라짐)](#-------------------------------)
</details>

# 함수
> 코드의 재사용 가능한 일부로서 언제든 사용할 수 있도록 이름을 붙여놓은 것

1. 코드의 중복을 줄이는데 유용하다.
2. 코드를 더 읽기 쉽고 이해하기 쉽게 만든다.

## 함수 만들기
> 1. 함수 정의하기
> 2. 함수 실행하기

```js
function funcName(){
    //do something
}

>>> funName()
```

## 인수 (arguments)
> 함수에 입력하는 값

<br>
함수는 인수를 받고 <br>> 함수라는 기계 안에 있는 여러 내용을 인수와 연관지어 무언갈 만들어 냄. <br>> 함수라는 기계는 결과물을 내뱉어줌
<hr>

### 메서드는 곧 함수다
`num.push('')` `"hello".toUpperCase()`
와 같이 `변수.method()` 는 이미 있는 함수의 인수를 입력하는 것이다.
<hr>

### 인수는 식별 능력이 없다.
인수는 단지 받은 값을 그대로 돌려보내줄 뿐이다.
```js
// EX

function great(firstName) {
    console.log(`hi ${firstName}!`);
}

great("도윤")
>>> hi 도윤!

great(1232345325)
>>> hi 1232345325!

great() // 인수를 안넣을 때
>>> hi undefiend! //  기본값인 undefined가 뜸.
```
### 두 개 이상의 인수 받기
```js
// EX
function great(firstName, lastName) {
    console.log(`hi ${firstName}${lastName}!`);
}

great("도윤", "김")
>>> hi 도윤김!
```
인수는 쉼표로 구분한다.

> 인수를 두 개 이상 사용할 때 가장 중요한 것은 **순서** 이다.

#### 만약 두 개 이상의 인수 중 하나만 입력한다면?

> 그냥 undifind일 뿐입니다.

## RETURN
> 함수의 출력 값
### return의 역할 1. 값 함수에 저장
🤔 console.log로도 충분히 출력 값이 나오는데 return을 써야 하는 이유가 뭐죠?
<br>
<br>
바로, 함수 안에 **값을 캡쳐해두기** 위해서 입니다!
콘솔 로그를 쓰면, 그냥 그 순간 뿐이에요. 값이 계속 저장되는 건 ㄴㄴ
<br>
그렇기 때문에, 우리는 값을 **저장하고 보관** 하기 위해서 return을 써야 합니다.

### return의 역할 2. 함수 끝내기
```javascript
function add (){
    return
    console.log("return이 끝냈기 때문에 없는 취급돼요")
}
```
### return은 하나의 값만 출력한다.

만일 두 개 이상의 값을 출력하고 싶다면 하나의 배열로 만들어서 내보내야함.

<hr>

# 230508 TIL

## Scope (범위) / python의 지역변수, 전연벽수 얘기
> "변수 가시성"을 참조한다. 변수를 JS의 어느 부분에 정의하느냐가 액세스 지점을 결정한다.

```js
// EX.
function collectEggs(){
    let totalEggs = 6;  
}
console.log(totalEggs)
```
🤨 함수 안에 선언된 totalEggs를 함수 밖에서 사용하려면 어떻게 될까?
<br> > 바로, 이런 에러가 출력된다. <br>
`ReferenceError: totalEggs is not defined`

### ⚠️ 함수 안에서 정의된 변수들은 그 함수로 범위가 한정되어 있다.
> 함수 안에 있는 변수랑 함수 밖의 변수는 완전 다른거임!!

```js
// EX
let bird = "앵무새";
function birdWath(){
    let bird = "왜가리"
    console.log(bird) 
}
birdWath() // 왜가리
console.log(bird) // 앵무새
```
### Block
> (함수 제외) 기본적으론 중괄호가 있는 모든 곳
```js
if () {
    //// black ////
};
```
#### 🤷‍♀️ var
let과 const는 block안에 있는 변수로만 이용이 가능하지만, **var**는 변수 밖에서도 사용이 가능하다.
```js
for (let i = 0; i < 3 ; i ++) {
    const msg = "졸리당";
};
console.log(i);
console.log(msg);

>>> SyntaxError: Unexpected end of input
```
```js
for (var i = 0; i < 3 ; i ++) {
    var msg = "졸리당";
};
console.log(i); 
console.log(msg);

>>> 3 // i 까지 출력 가능함 ;;;!!
>>> 졸리당
```
🤔 그럼 왜 var를 쓰면 안되죠?
> 충돌 이슈가 있어요!!

### 렉시컬 범위
```js
// EX
function outer() {
    let hero = "블랙 펜서";

    function inner() {
        let cryForHelp = `${hero}, 도와줘!` // 부모 함수의 변수를 가지고 옴
        console.log(cryForHelp);
    }
    inner();
}
outer();

>>> 블랙 펜서, 도와줘!
```
> 부모 함수의 안에 중첩된 내부 함수는 해당 외부 함수의 범위 또는 범위 내에서 정의된 변수에 접근할 수 있다.

#### 그러나 부모 함수는 자식 함수의 변수를 가져다 쓸 순 없다.

## 함수 표현식
> 변수 안에 함수를 저장하는 방식
```javascript
// 이전
function add(x, y) { // add 라는 함수 명이 없으면 안됨
    return x + y
}
```
```javascript
const add = function (x, y) {
    return x + y
}
// FunctionExpression
// 함수 명도 필요하지 않고, 변수에 따로 저장도 가능함!
```

## 고차 함수
> 다른 함수와 함께 작동하거나, 다른 함수에서 작동하는 함수를 고급스럽게 표현한 것
### 함수를 인수로 받는 함수
```javascript
function callTwice (func) {
    func();
    func();
}
function rollDie(){
    const roll = Math.floor(Math.random() * 6) + 1
    console.log(roll)
}
callTwice(rollDie)

>>> 2
>>> 1
```

### 반환 함수
> 함수 내에서 함수를 값으로 반환

#### 팩토리 함수
> 함수를 계속 만들어주는 함수
```javascript
function makeBetweenFunc(min, max) {
    return function (num) {
        return num >= min && num <= max;
    }
}
makeBetweenFunc(0, 120)
// ƒ (num) {
//     return num >= min && num <= max;
// }
const isChild = makeBetweenFunc(0, 18)
// ƒ (num) {
//     return num >= min && num <= max;
// }
isChild(40) // false
isChild(8) // true

const isAdult = makeBetweenFunc(19, 64)
isAdult(9) // false
isAdult(19) // true
```
논리가 이해돼서 더 신기함..

## 메소드(method) 만들기
> 메소드란? `"hello".toUpperCase()` 에서 `.toUpperCase()` 같은 것 

- 메소드는 객체에 종속된 특성으로, 함수에 포함되는 개념이다.
- 그러나 모든 함수가 메소드인 것은 아니다.

### 객체에 함수 넣기
```js
const myMath = {
    PI : 3.14,
    square : function(num) {
        return num * num;
    },
    cube : function(num){
        return num ** 3
    }
}
myMath.cube(2)
myMath.squre(3)
```
#### 속기법 (shorthand)
```js
const myMath = {
    PI : 3.14,
    square(num) {
        return num * num;
    },
    cube(num){
        return num ** 3;
    }
}
```

## "THIS" 
> 메서드에 있는 객체를 가리킬 때 사용한다.
```js
const dog = {
    name: "레오",
    color: "브라운",
    breed: "푸들",
    meng() {
        console.log(color) // caught ReferenceError: color is not defined
    }
}
```
color라는 객체는 bloack되있음으로 소환! 할 수 없다. 이럴 때 쓰는게 **this** 메소드

```js
const dog = {
    name: "레오",
    color: "브라운",
    breed: "푸들",
    meng() {
        console.log(`${this.name}가 멍멍! 짖었다.`)
    }
}
dog.meng()

>>> 레오가 멍멍! 짖었다.
```

### 어떤 객체를 가르키는 지가 중요하다! (결과값이 달라짐)

```js
const dog = {
    name: "레오",
    color: "브라운",
    breed: "푸들",
    meng() {
        console.log(`${this.name}가 멍멍! 짖었다.`)
    }
}

const dog2 = dog.meng;

dog2
// ƒ meng() {
//     console.log(`${this.name}가 멍멍! 짖었다.`)
// }
dog2() // undefined가 멍멍! 짖었다.
dog.meng() // 레오가 멍멍! 짖었다.
```
`dog.meng()`에서 괄호는 `dog`라는 객체를 가르켰다.
<br> 그러나 dog2는 window 객체를 가르킨다.(가장 상위 객체)
<br> 즉, `dog2()`는 `window.dog2()` 와 같은 말이라서, 우리가 원하는 값이 나오지 않은 것.