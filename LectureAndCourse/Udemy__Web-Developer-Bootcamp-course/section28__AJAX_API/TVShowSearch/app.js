const form = document.querySelector("#searchForm");
const imageContainer = document.querySelector('#imageCantainer')

form.addEventListener('submit', async function(e) {
    e.preventDefault();
    const searchTerm = form.elements.query.value;
    const config = {params : {q: searchTerm}}
    const res = await axios.get(`https://api.tvmaze.com/search/shows`, config)
    makeImages(res.data)
    form.elements.query.value = '';
    
})

const makeImages = (shows) => {
    while (imageContainer.firstChild){
        imageContainer.removeChild(imageContainer.firstChild)
    }
    for(let result of shows){
        if(result.show.image){
            const img = document.createElement('IMG');
            img.src = result.show.image.medium;
            imageContainer.append(img)

        }
    }
}
