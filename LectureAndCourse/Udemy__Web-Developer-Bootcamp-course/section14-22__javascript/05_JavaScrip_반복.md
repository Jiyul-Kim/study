# 230507 TIL

# Loop
어떤 기능을 반복하는 방법

## for Loops
```js
// 기본 구문
for (
    [initialExpression] ;
    [condition];
    [incrementExpression]
) {
    // output
}
```

## infinite Loops
JS가 가진 모든 메모리를 사용하게 된다. 예전에는 정지도 어려웠다네요.

> 코드쓸 때 신중하세요!

## Looping Over Arrays

```python
# PYTHON

animals = ['lions', 'tigers', 'bears']
for i, animal in enumerate(animals):
    print(i, animal)

0 lions
1 tigers
2 bears
```

```javascript
// JS

const animals = ['lions', 'tigers', 'bears'];
for (let i = 0; i < animals.length; i++ ) {
    console.log(i, animals[i])
}

0 'lions'
1 'tigers'
2 'bears'
```

## 중첩 Loop (...😭)
> 아주 기본이 되는 중첩 구문을 배워보자.
```javascript
for(let i=0; i<=10; i++) {
    console.log(`i is ${i}`)
    for(let j=1; j<4; j++){
        console.log(`    j is: ${j}`)
    }
}

i is 0
     j is: 1
     j is: 2
     j is: 3
.
.
.

i is 10
     j is: 1
     j is: 2
     j is: 3
```

### 중첩 배열 빼내기

```js
const seatingChart = [
    ['지율', "도윤", "호영" ],
    ["시진", "재경", "혜성"],
    ["우진", "라움", "하율"]
]

for(let i = 0; i < seatingChart.length; i++) {
    const row = seatingChart[i];
    for(let j=0; j < row.length; j++){
        console.log(row[j]);
    }
}

>>>

지율
도윤
호영
시진
재경
혜성
우진
라움
하율
```

## While Loops

> 기본 구문

```javascript
let num = 0;
while (num < 10) {
    console.log(num);
    num++;
}

>>>
0
1
2
3
... 9
```

> 반복 횟수가 정해지지 않을 때 for 보다 while을 사용하면 좋다.
> <br> 예로 들어, 누군가 죽어야지 끝나느 게임 같은

## 루프를 멈추고 싶다면? 🌟 Break!

## for of <- 배열과 궁합이 좋아요!
JS에 새로 생긴 기능!
인덱싱 되있는 걸 하나씩 빼오기 쉬운 구문이라고 생각하면 좋을 것 같아요.
> **기본 구문**
```javascript
for (variable of iterable) {
    statement
}
```

> 원래는 배열에서 내용을 빼낼려면 이렇게 for을 사용했어요.

```javascript
const subreddits = ['cringe', 'books', 'chickens', 'funny', 'pics', 'soccer'];

for (let i = 0; i < subreddits.length; i++) {
    console.log(`reddit.com/r/${subreddits[i]}`)
}
>>> 
reddit.com/r/cringe
reddit.com/r/books
reddit.com/r/chickens
reddit.com/r/funny
reddit.com/r/pics
reddit.com/r/soccer
```

```javascript
const subreddits = ['cringe', 'books', 'chickens', 'funny', 'pics', 'soccer'];

for(let sub of subreddits){
    console.log(`reddit.com/r/${sub}`)

>>>
reddit.com/r/cringe
reddit.com/r/books
reddit.com/r/chickens
reddit.com/r/funny
reddit.com/r/pics
reddit.com/r/soccer
}
```

## 객체 요소 빼오기
### for of는 안된다.
>  not iterable

객체를 for of 를 사용하면 해당 오류가 나온다.

### for in 을 사용하면?
> key1 <br>
> key2 <br>
> key3 . . . 

key의 값이 빠져 나오게 된다.

#### 번외) 만약 value값을 빼오고 싶다면?

```javascript
for(let person of testScores){
    console.log(testScores[person])
}
// 이런식으로 원래 객체[for in으로 뺀 객체] 를 쓰면 됨
```
<hr>

### 딱히 반복문 안쓰고 key와 value 값 빼낼려면?
#### Object.keys (method)
key값이 배열로 나옴
#### Object.values (method)
value값이 배열로 나옴
#### Object.entries (method)
key와 value 값이 배열로 나옴
`[key1:value1]`
`[key2:value2]`
