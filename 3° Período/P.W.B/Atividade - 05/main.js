const express = require('express')
const app = express()
const port = 3000

const router = require('./router')

app.use(express.urlencoded({extended: false}))
app.set('views', 'views')
app.set('view engine', 'ejs')

app.use('/', router)

app.listen(port, () => {
    console.log(`Example app listening on port http://localhost:${port}`)
})
