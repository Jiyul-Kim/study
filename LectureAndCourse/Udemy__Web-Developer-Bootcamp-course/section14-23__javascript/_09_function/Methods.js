// const myMath = {
//     PI : 3.14,
//     square : function(num) {
//         return num * num;
//     },
//     cube : function(num){
//         return num ** 3
//     }
// }
/// shorthand

const myMath = {
    PI : 3.14,
    square(num) {
        return num * num;
    },
    cube(num){
        return num ** 3;
    }
}

/// 45번 퀴즈
const square = {
    area(side) {
        return side * side;
    },
    perimeter (side) {
        return side * 4
    }
}
square.area(10);
square.perimeter(10);


const dog = {
    name: "레오",
    color: "브라운",
    breed: "푸들",
    meng() {
        console.log(`${this.name}가 멍멍! 짖었다.`)
    }
}

const dog2 = dog.meng;

// ƒ meng() {
//     console.log(`${this.name}가 멍멍! 짖었다.`)
// }
// dog2() // undefined가 멍멍! 짖었다.
// dog.meng() // 레오가 멍멍! 짖었다.


// 코딩 연습 46번
const hen = {
    name : "Helen",
    eggCount : 0,
    layAnEgg () {
        this.eggCount += 1
        return "EGG"
    }
}
hen.layAnEgg(1)
hen.eggCount