const button = document.querySelector("button");
const h1 = document.querySelector("h1");
button.addEventListener("click", () => {
  const newColor = makeRandColor();
  document.body.style.backgroundColor = newColor;
  h1.innerText = newColor;
  
});

const makeRandColor = () => {
  const r = Math.floor(Math.random() * 255);
  const g = Math.floor(Math.random() * 255);
  const b = Math.floor(Math.random() * 255);
  if (r+b+g < 450){
    h1.style.color = "white"; 
   }
  return `rgb(${r}, ${g}, ${b})`;
};
