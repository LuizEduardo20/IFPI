const express = require('express')
const router = express.Router()

let listaOperacoes = []

router.get('/', function (req, res, next) {
    res.render('pages/home', {
        currentPage: 'home',
        listaOperacoes: listaOperacoes
    })
})

router.get('/operacoes', function(req, res, next) {
    res.render('pages/operacoes', {
        currentPage: 'operacoes',
        listaOperacoes: listaOperacoes
    })
})

router.get('/sobre', function (req, res, next) {
    res.render('pages/sobre', {
        currentPage: 'sobre',
        listaOperacoes: listaOperacoes
    })
})

router.post('/operacoes', function(req, res, next) {
    const data = req.body.data
    const codigo = req.body.codigo
    const acao = req.body.acao
    const precoBruto = parseFloat(req.body.precoBruto)
    const quantidade = parseInt(req.body.quantidade)
    const precoUnitario = (precoBruto * quantidade).toFixed(2)

    let precoLiquido = 0

    if(acao === 'Compra') {
        precoLiquido = ((precoBruto * quantidade) + ((precoBruto * quantidade) * 0.05 / 100)).toFixed(2)

    } else if(acao === 'Venda') {
        precoLiquido = ((precoBruto * quantidade) - ((precoBruto * quantidade) * 0.05 / 100)).toFixed(2)
    }

    const array = [data, codigo, acao, precoBruto, quantidade, precoUnitario, precoLiquido]
    listaOperacoes.push(array)

    res.render('pages/operacoes', {
        currentPage: 'operacoes',
        listaOperacoes: listaOperacoes
    })
})

router.get('/novaOperacao', function(req, res, next) {
    res.render('pages/novaOperacao', {
        currentPage: 'operacoes',
        listaOperacoes: listaOperacoes
    })
})

module.exports = router