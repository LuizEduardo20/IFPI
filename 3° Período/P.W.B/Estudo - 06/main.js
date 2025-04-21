const express = require('express')
const app = express()
const port = 3000

const router = require('./public/routers/router')

app.use(express.urlencoded({extended : false}))
app.use(express.static('public'));
app.set('views', 'views')
app.set('view engine', 'ejs')

app.use('/', router)

app.listen(port, () => {
  console.log(`App de exemplo esta rodando na porta ${port}`)
})