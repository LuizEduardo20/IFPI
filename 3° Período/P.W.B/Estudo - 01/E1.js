// Conhecendo o Express e criando rotas.

const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello, World!')
})

app.get('/rota', (req, res) => {
  res.send('Bem vindo a pagina 2!!')
})

app.listen(port, () => {
  console.log(`App de exemplo esta rodando na porta ${port}`)
})
