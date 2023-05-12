const btn = document.querySelector('#b2')
btn.onclick = function(){
    console.log("클릭하새요")
}
function scream() {
    console.log('뿌애앵')
}
btn.onmouseenter = scream;

document.querySelector("h1").onclick =() =>  alert('h1을 클릭하셨어요!')

const btn3 = document.querySelector('#b3')
btn3.addEventListener('dblclick', () => alert("btn3"))