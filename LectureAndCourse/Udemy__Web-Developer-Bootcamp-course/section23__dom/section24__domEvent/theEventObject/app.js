document.querySelector('button').addEventListener('click', function() {
    console.log('dd')
})

const input = document.querySelector('input');
input.addEventListener('keydown', function(e) {
    console.log(e.key)
    console.log(e.code)
})
// input.addEventListener('keyup', function() {
//     console.log('keyup')
// })