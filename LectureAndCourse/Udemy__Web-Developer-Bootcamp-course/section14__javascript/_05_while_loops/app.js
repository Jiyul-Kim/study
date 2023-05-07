// let count = 0;
// while (count < 10) {
//     count ++ ;
//     console.log(count)
// }

// const SECRET = "babo";

// let guess = prompt("시크릿 코드를 입력하세요.");
// while(guess !== SECRET){
//     guess = prompt("시크릿 코드를 입력하세요.");
// }
// console.log("시크릿코드가 맞습니다.")


let maximum = parseInt(prompt("최대 숫자를 입력하세요."));
while (!maximum) {
    maximum = parseInt(prompt("유효한 숫자를 입력하세요.."));
}

const targetNum = Math.floor(Math.random() * maximum) + 1;
console.log(targetNum);

let guess = parseInt(prompt("첫 추측 값을 입력하세요."))
let attempts = 1;


while (parseInt(guess) !== targetNum) {
    if(guess === 'q') break;
    attempts ++;
    if(guess > targetNum){
        guess = prompt("너무 높으니 추측 값을 다시 입력하세요.");
    } else {
        guess = prompt("너무 낮으니 추측 값을 다시 입력하세요.");
    }
}
if(guess === 'q') {
    console.log("게임을 종료합니다.")
} else {
    console.log("win")
    console.log(`맞췄어요! ${attempts}번 만에 맞췄습니다.`);
}
