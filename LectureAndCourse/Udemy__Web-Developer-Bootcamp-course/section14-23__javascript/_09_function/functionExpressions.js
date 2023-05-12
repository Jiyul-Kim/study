const add = function (x, y) {
    return x + y
}
// 코딩 연습 44번
const square = function (x) {
    return x * x
}


function callTwice (func) {
    func();
    func();
}
function rollDie(){
    const roll = Math.floor(Math.random() * 6) + 1
    console.log(roll)
}
// callTwice(rollDie)

/////////////////

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
