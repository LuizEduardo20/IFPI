const express = require('express')
const router = express.Router()

listaOperadores = []

router.get('/', (req, res) => {
    res.render('home')
})

router.post('/tabela', (req, res) => {
    const codigo = req.body.codigo
    const data = req.body.data
    const tipo = req.body.tipo
    const quantidade = parseInt(req.body.quantidade)
    const preco = parseFloat(req.body.preco)

    precoLiquido = 0

    if(tipo == 'compra'){
        precoLiquido = preco + (0.05 / 100)

    } else if(tipo == 'venda'){
        precoLiquido = preco - (0.05 / 100)
    }

    const array = [codigo, data, tipo, quantidade, preco, precoLiquido]
    
    listaOperadores.push(array)

    res.render('tabela',
        {
            listaOperadores: listaOperadores
        }
    )
})

module.exports = router