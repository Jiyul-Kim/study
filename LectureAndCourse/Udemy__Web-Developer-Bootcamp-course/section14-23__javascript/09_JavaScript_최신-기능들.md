# 230509 TIL
<details>
<summary>목차</summary>

- [디폴트 매개변수](#--------)
  * [SPREAD (전개 구문)](#spread--------)
      - [string도 가능하다!](#string-------)
    + [배열 리터럴](#------)
    + [객체 리터럴](#------)
  * [REST](#rest)
  * [DESTRUCTURING (구조 분해)](#destructuring--------)
    + [배열 분해](#-----)
    + [객체 분해](#-----)
    + [매개 변수 분해](#--------)

</details>

# 디폴트 매개변수
> 만약 인수를 따로 넣어주지 않고, 디폴트 값이 있게끔 하려면 어떻게 할까?
```js
function rollDie(numSides){
    if (numSides === undefined){
        return numSides = 6
    }
    return Math.floor(Math.random() * numSides + 1)
}
```
이렇게 if를 넣어주면 해결은 되지만, 더 쉬운 방법이 있음!

```js
function greet(person, msg = "Hey there") {
    return (`${msg}, ${person}!`)
}
```
⚠️ 단! 주의점이 있다.
디폴트가 되는 인수는 매개변수의 순서를 고려해 처음에 위치하면 안됨!
<br> `msg = "Hey there", person` <= 이렇게 입력 X


```js
function greet(msg = "Hey there", person ) {
    return (`${msg}, ${person}!`)
}
greet("jiyul")

>>> "jiyul", undifiend! // 이렇게 출력되니 주의!
```

## SPREAD (전개 구문)
> 배열이 **펼쳐**지며 인수가 분리된다.
```js
Math.max(13, 5, 6, 23, 234, 675, 23423)
>>> 23423

const nums = [13, 5, 6, 23, 234, 675, 23423]
Math.max(nums)
>>> NaN // 배열이기 때문에 숫자로 쳐주지 않으니 NaN이 출력되는 것

Math.max(...nums)
>>> 23423 // ... 을 쓰면 각 배열이 펼쳐지기 때문에 (13, 5, 6, 23, 234, 675, 23423) 와 같게 되는거임! 
```
#### string도 가능하다!
```js
console.log(...'hello')

>>> h e l l o
```
### 배열 리터럴
```js
const cats = ["레어", "삼초니", "양말이"]
const dogs = ["레오", "초코"]

const animals = [...cats, ...dogs]

>>> ['레어', '삼초니', '양말이', '레오', '초코']
```
### 객체 리터럴
```js
const cats = {
    name : "레어",
    family : "k-short",
    isCute : true
}
const dogs = {
    name : "레오",
    family : "poodle",
    legs : 4
}

const catDog = {...cats, ...dogs}
>>> {name: '레오', family: 'poodle', isCute: true, legs: 4}
```
⚠️ 단, 주의점은 무엇을 뒤에 spread 하려고 넣는지가 중요함! 
dogs를 뒤에 넣었더니, **중복되는 객체**인 family에서 dogs의 밸류가 출력됨

## REST
> 매개 변수를 모아주는 기능
```js
function sum(){
}
sum(3)
sum(3, 5) // 5는 무시됨
```
이렇게 매개변수가 여러개를 모이게 하려면 쓰는게 rest임!
```js
function sum(...nums){
}
sum(3, 5) // nums = [3, 5]
sum(7, 10, 45, 768, 234) // nums = [7, 10, 45, 768, 234]
```
```js
// 이렇게 쓸 수 있어요!

function raceResults(gold, silver, ...everonElse) {
    console.log(`금매달 : ${gold}`)
    console.log(`은매달 : ${silver}`)
    console.log(`그리고 모두에게 감사합니다 : ${everonElse}`)
}

raceResults("지율", "도윤", "희정", "재규")

> 금매달 : 지율
> 은매달 : 도윤
> 그리고 모두에게 감사합니다 : 희정,재규
```
## DESTRUCTURING (구조 분해) 
> 값을 해체하고 꺼내고 선정하는 간편한 방식
> <br> 해체해서 별개의 변수 형태로 만들 수 있다.
### 배열 분해
```js
// 원래는 이렇게 쓰던 구문을
const scores = [987897, 87867, 766545, 65434, 434324]

const highScore = scores[0] // 987897
const secondHighScore = scores[1] // 87867

// 이렇게 바꿀 수 있다!
const [gold, second, ...everyoneElse] = scores;
gold // 987897
second // 87867
everyoneElse // [766545, 65434, 434324]
```
### 객체 분해
```js
// 원래라면?
const user = {
    email : "kjekje0412@naver.com",
    password : "sfsgsf",
    firstName : "jiyul",
    lastName : "Kim",
    born : 1845
}

const password = user.password;
const email = user.email;
// 이렇게 계~속 변수를 선언해주면서 불필요하게 나열했어야 할 것.

// 객체 분해를 이용하면?
const {email, password, firstName, lastName} = user;
```
참고, 객체 분해의 순서는 중요하지 않음. key의 이름 제대로 넣는게 중요!
<br>
<br>
분해된 요소에 새로운 key 이름을 주고 싶을 떈?

```js
const {born : birthYear} = user;
```
만약 디폴트 값이 없다면?
```js
const {born = NaN} = user;
```
### 매개 변수 분해
> 주로 객체와 쓰임
```js
const user = {
    email : "kjekje0412@naver.com",
    password : "sfsgsf",
    firstName : "jiyul",
    lastName : "Kim"
}

// 1. 이렇게 분해할 수 있다.
function fullName(user) {
    const {firstName, lastName} = user;
    return `${firstName} ${lastName}`
}

// 2. 매개변수 란에 분해를 적어줄 수 있다.
function fullName({firstName, lastName}) {
    return `${firstName} ${lastName}`
}

fullName(user)
>>> 'jiyul Kim'
```