const express = require('express')
const app = express();
const path = require('path')
const { v4: uuid } = require('uuid')

app.use(express.urlencoded({extended:true}))
app.use(express.json())
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')

const comments = [
    {
        id: uuid(),
        username: "jiyul",
        comment: 'i want to go home'
    },
    {
        id: uuid(),
        username: "doyyon",
        comment: 'no more'
    },
    {
        id: uuid(),
        username: "heejung",
        comment: 'im done'
    },
    {
        id: uuid(),
        username: "jeakyu",
        comment: '...'
    }
]

app.get('/comments', (req, res) => {
    res.render('comments/index', { comments })
})

app.get('/comments/new', (req, res) => {
    res.render('comments/new')
})

app.post('/comments', (req, res) => {
    const {username, comment} = req.body
    comments.push({username, comment, id: uuid(),})
    res.redirect('/comments')
})

app.get('/comments/:id', (req, res) => {
    const {id} = req.params;
    const comment = comments.find(c => c.id === id)
    res.render('comments/show', {comment})
})

app.get('/tacos', (req, res) => {
    res.send('GET /tacos response')
})

app.post('/tacos', (req, res) => {
    const {meat, qty} = req.body
    res.send(`here are your ${meat} ${qty} `)
})

app.listen(3000, () => {
    console.log('on port 3000')
})

