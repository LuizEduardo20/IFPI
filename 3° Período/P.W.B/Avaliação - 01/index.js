const express = require('express')
const app = express()
const port = 3000
const router = require('./routes/routers')
const expressLayouts = require('express-ejs-layouts')
const session = require('express-session')

app.set('views', 'views')
app.set('view engine', 'ejs')
app.set('layout', 'layout')
app.use(expressLayouts)

app.use(express.urlencoded({ extended: false }))
app.use(express.static('public'))

app.use(session({
    secret: 'chave-secreta-do-jogo',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}))

app.use('/', router)

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})
