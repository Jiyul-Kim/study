let input = prompt("실행하시겠습니까?");
while (!input) {
    input = prompt("입력을 제대로 하세요!!");
}
const todoList = [];

while (input !== "quit" && input !== 'q'){
    let guess = prompt("어떤 메뉴를 실행하시겠습니까?");
    if (guess === "quit") break;
    if (guess === "new") {
        guess = prompt("Add A Todo");
        todoList.push(guess)
        console.log(todoList)
    } else if (guess === "list") {
        alert(`하실 일은 이렇게 되십니다.`);
        console.log("*********")
        for (let i=0; i<todoList.length; i++){
            console.log(`${i}: ${todoList[i]}`)
        }
        console.log("*********")

    } else if (guess === "delete") {
        const index = parseInt(prompt("삭제할 인덱스를 입력해주세요."));
        if (!Number.isNaN(index)) {
            todoList.splice(index, 1)
            console.log(todoList)
        } else {
            console.log("알 수 없는 인덱스입니다.")
        }
    } else {
        alert("없는 메뉴입니다.");
    }
}
console.log("Quit App")

