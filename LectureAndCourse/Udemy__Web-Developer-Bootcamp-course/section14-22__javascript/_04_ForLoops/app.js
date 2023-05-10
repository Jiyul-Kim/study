// for (let i = 1; i <= 10; i+=5) {
//     console.log(i);
// }

// for (let i = 2; i <=20; i += 2 ) {
//     console.log(i);
// }

// for (let i = 1; i <=20; i += 2 ) {
//     console.log(i);
// }
// for (let i = 100; i >= 0; i -= 10 ) {
//     console.log(i);
// }
// for (let i = 10; i <= 1000; i *= 10 ) {
//     console.log(i);
// }
// for (let i = 25; i >= 0; i-=5){
//     console.log(i)
// }

// for(let i=0; i<=10; i++) {
//     console.log(`i is ${i}`)
//     for(let j=1; j<4; j++){
//         console.log(`    j is: ${j}`)
//     }
// }

const seatingChart = [
    ['지율', "도윤", "호영" ],
    ["시진", "재경", "혜성"],
    ["우진", "라움", "하율"]
]

for(let i = 0; i < seatingChart.length; i++) {
    const row = seatingChart[i];
    for(let j=0; j < row.length; j++){
        console.log(row[j]);
    }
}