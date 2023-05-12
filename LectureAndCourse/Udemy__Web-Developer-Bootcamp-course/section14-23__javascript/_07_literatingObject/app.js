const testScores = {
    aa: 60,
    bb: 30,
    cc: 90,
    dd: 12,
    ee: 50
}

// for(let person of testScores){
//     console.log(person)
// }
let total = 0;
let scores = Object.values(testScores);
for(let score of Object.values(testScores)) {
    total += score;
}
console.log(total / scores.length)