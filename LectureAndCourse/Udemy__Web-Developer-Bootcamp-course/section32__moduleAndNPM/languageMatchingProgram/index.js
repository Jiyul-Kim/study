import {franc, francAll} from 'franc'
import langs from 'langs'
// const franc = require('franc')
// const langs = require('langs')

const input = process.argv[2]
const langCode = franc(input, {minLength:2});

if (langCode === 'und') {
    console.log("sorry, cound't figure it out! try with more sample text" )
} else {
    const language = langs.where('3', langCode)
    
    console.log(language.name)

}
