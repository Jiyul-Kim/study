const express = require('express')
const app = express();
const path = require('path')
const redditData = require('./data.json')

app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, '/views'))

app.get('/', (req, res) => {
    res.render('home')
})

app.get('/cats', (req, res)=> {
    const cats = [
        '나비', '레어', '치즈', '젖소', '냐옹이'
    ]
    res.render('cats', { cats })
})

app.get('/r/:subreddit', (req, res)=> {
    const {subreddit} = req.params;
    const data = redditData[subreddit]
    // console.log(data)
    if (data) {
        res.render('subreddit' , {...data})
    } else {
        res.render('notfound', {notfound})
    }
})

app.get('/rand', (req, res) => {
    const num = Math.floor(Math.random() * 10 ) + 1;
    res.render('random', {num: num})
})

app.listen(3000, () => {
    console.log('listening on 3000')
})