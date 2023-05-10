const password = prompt("비밀번호를 입력해 주세요.")

// 6글자 이상
if (password.length >= 6) {
    if (password.indexOf(' ') === -1) {
        console.log("유효한 비밀번호입니다.")
    } else {
        console.log("공백이 있으면 안됩니다.")
    }
} else {
    console.log("비밀번호는 6자리 이상이거나 공백이 있으면 안됩니다.")
}
// space를 포함했는지

