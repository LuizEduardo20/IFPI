const express = require('express')
const app = express()
const port = 3000

app.use(express.urlencoded({extended : false}))
app.set('views', 'views')
app.set('view engine', 'ejs')

app.get('/', (req, res) => {
  res.render('home')
})

const lista = []

app.post('/tabela', (req, res) => {
  const codigo = req.body.codigo
  const data = req.body.data
  const tipo = req.body.tipo
  const quantidade = parseInt(req.body.quantidade)
  const valor = parseFloat(req.body.valor)

  let valorLiquido = 0

  if(tipo == 'compra'){
    valorLiquido = (quantidade * valor) + ((quantidade * valor) * 0.05 / 100)

  } else if (tipo == 'venda'){
    valorLiquido = (quantidade * valor) - ((quantidade * valor) * 0.05 / 100)
    
  }

  const array = [codigo, data, tipo, quantidade, valor, valorLiquido]

  lista.push(array)

  res.render('tabela', 
    {
      lista: lista
    }
  )
})

app.listen(port, () => {
  console.log(`App de exemplo esta rodando na porta ${port}`)
})
