function sing() {
    console.log("도");
    console.log("레");
    console.log("미");
}

function great(firstName, lastName) {
    console.log(`hi ${firstName}${lastName}!`);
}
// great("도윤", "김")

function repeat(message, nnumTime) {
    let result = '';
    for (let i = 0; i < nnumTime; i ++) {
        result += message;
    }
    console.log(result)
}

function isSnakeEyes(num1, num2) {
    if (num1 === num2) {
        console.log("Snake Eyes!")
    } else {
        console.log("Not Snake Eyes!")
    }
}

function add (){
    return
    console.log("return이 끝냈기 때문에 없는 취급돼요")
}

function capitalize (arg){
    return firstCap = arg[0].toUpperCase() + arg.slice(1)
    
}

function sumArray (ary) {
    let result = 0;
    for(let i = 0; i < ary.length; i ++){
        result += ary[i];
    }
    return result 
}

const week = ["Monday", "Tuesday", "Wednesday" ,"Thursday", "Friday", "Saterday", "Sunday"];
function returnDay (day) {
    if (0 >= day || day > 8) {
        return null
    }
    return day = week[day - 1];
    
}