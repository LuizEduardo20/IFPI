// Enviando e recebendo dados de uma requisição.

const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({ extended: true }))
app.set('view engine', 'ejs')
app.set('views', './components/views')

app.get('/', (req, res) => {
  res.render('home')
})

app.post('/resposta', (req, res) => {
    cidade = req.body.cidade
    resposta = ''

    if (cidade == 'teresina'){
        resposta = 'Que cidade Bacana'
    } else{
        resposta = 'Sua cidade é muito padrão'
    }
    
    res.render('resposta', {
        resposta: resposta
    });
})

app.listen(port, () => {
  console.log(`Example app listening on http://localhost:${port}`)
})
