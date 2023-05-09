function rollDie(numSides){
    if (numSides === undefined){
        return numSides = 6
    }
    return Math.floor(Math.random() * numSides + 1)
}

function greet(person, msg = "Hey there") {
    return (`${msg}, ${person}!`)
}

// const cats = ["레어", "삼초니", "양말이"]
// const dogs = ["레오", "초코"]

// const animals = [...cats, ...dogs]

const cats = {
    name : "레어",
    family : "k-short",
    isCute : true
}
const dogs = {
    name : "레오",
    family : "poodle",
    legs : 4
}


