// async function hello () {

// }

// const sing = async () => {
//     // throw "이런! 에러임!"
//     return "dddd"
// }

// sing().then ()

const login = async (username, password) => {
    if (!username || !password) throw "Missing Credentials"
    if (password === "bububu") return "welcome!"
    throw "invalid Password"
}
login("sfsf", "bububu")
    .then (msg => {
        console.log("logged in!")
        console.log(msg)
    })
    .catch(err => {
        console.log("Error!");
        console.log(err)
    })