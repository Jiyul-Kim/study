// axios.get("https://swapi.dev/api/people/1")
// .then (res => {
//     console.log("response", res)
// })
// .catch(e => {
//     console.log("ERROR", e)
// })

const getStarWarsPerson = async (id) => {
    try {
        const res = await axios.get(`https://swapi.dev/api/people/${id}`);
        console.log("response", res)
    } catch(e){
        console.log("ERROR", e)
    }
}
getStarWarsPerson(5);
getStarWarsPerson(10);