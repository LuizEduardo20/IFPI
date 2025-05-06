const express = require('express')
const app = express()
const port = 3000
const route = require('./public/routers/router')
const expressLayouts = require('express-ejs-layouts')

app.use(express.urlencoded({extended : false}))
app.use(express.static('public'))

app.set('views', './public/views')
app.set('view engine', 'ejs')
app.set('layout', 'layout')
app.use(expressLayouts)

app.use('/', route)

app.listen(port, () => {
  console.log(`App rodando na porta ${port}`)
})