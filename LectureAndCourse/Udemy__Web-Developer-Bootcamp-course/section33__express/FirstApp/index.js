const express = require('express')
const app = express()

// app.use ((req, res) => {
//     console.log('we got a new requset')
//     res.send({color :" red"})
// }) 
// > 이건 res.send로 응답을 보낼 때 마다 하나의 요청으로 끝나버림. 
// 하나 이상의 응답을 얻는 HTTP 요청을 받을 수 없다.

app.get('/', (req, res) => {
    res.send('Welcome to the home page!')
})

app.get('/r/:subreddit', (req, res) => {
    const {subreddit} = req.params;
    res.send(`<h1>Browsing the ${subreddit} subreddit</h1>`)
})
app.get('/r/:subreddit/:postID', (req, res) => {
    const {subreddit, postID} = req.params;
    res.send(`<h1>Viewing post ID: ${postID}on the ${subreddit} subreddit</h1>`)
})
app.get('/cats', (req, res) => {
    res.send('meow!')
})
app.post('/cats', (req, res) => {
    res.send('post requset to /cats!!! this is diffrent than a get requset!')
})
app.get('/dogs', (req, res) => {
    res.send('Woof!')
})


app.get('/search', (req, res) => {
    const {q} = req.query;
    if (!q){
        res.send('NOTHING FOUND!')
    }
    res.send(`<h1>Search results for: ${q}</h1>`)
})


app.get('*', (req, res) => {
    res.send('post requset to /cats!!! this is diffrent than a get requset!')
})

app.listen(3000, () => {
    console.log('listening on port 3000')
}) 