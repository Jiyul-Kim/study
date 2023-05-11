// const allImages = document.getElementsByTagName('img');

// for(let img of allImages){
//     console.log(img.src)
// }

// const squareImages = document.getElementsByClassName('square');
// for(let img of squareImages){
//     img.src = "https://upload.wikimedia.org/wikipedia/commons/e/e0/Male_Silkie.png"
// }

// 코딩 연습 52

// const doneTodos = document.querySelectorAll(".done");
// const checkbox = document.querySelector("input:nth-of-type(2)")

// 코딩 연습 58
const div = document.querySelector("#container")
for (let i=0; i < 100; i++){
    const newButton = document.createElement('button');
    newButton.innerText = "text";
    div.appendChild(newButton)
}