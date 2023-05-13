// Leave the next line, the form must be assigned to a variable named 'form' in order for the exercise test to pass
const form = document.querySelector('form');
const formContainer = document.querySelector('#list');

form.addEventListener('submit', function(e){
    e.preventDefault()

    const productInput = form.elements.product;
    const qtyInput = form.elements.qty;
    addProduct (productInput.value, qtyInput.value)
    productInput.value = "";
    qtyInput.value = "";
})

function addProduct (product, qty) {
    const newList = document.createElement('li')
    formContainer.appendChild(newList)
    newList.innerText = `${qty} ${product}`
}