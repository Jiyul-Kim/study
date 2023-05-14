const multiply = (x, y) => x * y;

const square = (x) => multiply(x, x);

const isRightTraiangle = (a, b, c) => {
    return square(a) + square(b) === square(c);
}

isRightTraiangle(3, 4, 5)

console.log("첫 번째 print");
setTimeout(() => {
    console.log("3분 뒤에 print 됩니다.");
})
console.log("두 번째 print");
