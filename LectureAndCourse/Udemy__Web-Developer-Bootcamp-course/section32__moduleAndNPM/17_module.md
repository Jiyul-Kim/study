## module.export
두 개의 js 파일을 이어주고, 출력하게 도와준다.

1. 1차 시도
```js
// math.js
const add = (x,y) => x + y;

const PI = 3.14350;

const square = x => x * x;
```
```js
// app.js
const math = require('./math')
console.log(math)
```
>![](images/2023-05-20-00-30-40.png)
math.js에서 app.js로 기능을 전달해주지 않았기 때문에 빈 객체가 반환된다.

2. 2차 시도 (module.export 사용)
```js
// math.js
const add = (x,y) => x + y;

const PI = 3.14350;

const square = x => x * x;

module.exports.add = add;
module.exports.PI = PI;
module.exports.square = square;
```

> ![](images/2023-05-20-00-31-39.png)
값이 아닌 해당 모듈의 기능이 반환이 됐다.

3. 3차 시도 (인수 넣어주기)

```js
// app.js
const math = require('./math')
console.log(math.PI)
console.log(math.square(9))
```
![](images/2023-05-20-00-33-08.png)

원하던 value가 출력됐다.

4. 불러올 객체만 구조 분해하기
```js
// app.js
const {PI, square} = require('./math')
console.log(PI)
console.log(square(9))
```

- export 할 변수를 객체로 묶어 한 번에 moudule.export 하기
```js
// math.js
const math = {
    add: add,
    PI: PI,
    square: square
}

module.exports = math;
```
- exports shorthand
```js
exports.square = square;
exports.PI = PI;
```