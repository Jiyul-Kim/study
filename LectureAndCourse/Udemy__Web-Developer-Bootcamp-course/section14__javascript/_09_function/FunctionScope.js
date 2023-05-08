// function collectEggs(){
//     let totalEggs = 6;  
// }
// console.log(totalEggs)

// let bird = "앵무새";
// function birdWath(){
//     let bird = "왜가리"
//     console.log(bird)
// }
// birdWath()
// console.log(bird)

// for (var i = 0; i < 3 ; i ++) {
//     var msg = "졸리당";
// };
// console.log(i);
// console.log(msg);

// for (let i = 0; i < 3 ; i ++) {
//     const msg = "졸리당";
// };
// console.log(i);
// console.log(msg);

function outer() {
    let hero = "블랙 펜서";

    function inner() {
        let cryForHelp = `${hero}, 도와줘!`
        console.log(cryForHelp);
    }
    inner();
}
outer();