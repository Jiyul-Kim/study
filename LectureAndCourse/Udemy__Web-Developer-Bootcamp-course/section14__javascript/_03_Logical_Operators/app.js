// const password = prompt("비밀번호를 입력하세요.");

// if (password.length >= 6 && password.indexOf(" ") === -1) {
//     console.log("유효한 비밀번호")
// } else {
//     console.log("올바르지 않은 비밀번호 입니다.")
// }

const age = -10;
if (age >= 0 && 0 < age < 5 || age >= 65) {
    console.log("Free")
} else if (age >= 5 && age < 10) {
    console.log("$ 10")
} else if (age >= 10 && age < 65) {
    console.log("$ 20")
} else {
    console.log("뭔가 이상해요")
}

