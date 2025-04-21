const express = require('express')
const router = express.Router()

let lista = []

router.get('/', (req, res) => {
    res.render('home')
})

router.get('/aluno', (req, res) => {
    res.render('aluno', { lista: lista })
})

router.post('/aluno', (req, res) => {
    const disciplina =  req.body.disciplina
    const nota1 = parseFloat(req.body.nota1)
    const nota2 = parseFloat(req.body.nota2)
    const media = (nota1 + nota2) / 2

    lista.push({
        disciplina: disciplina,
        nota1: nota1,
        nota2: nota2,
        media: media
    })

    res.render('aluno', 
        {
            lista: lista
        }
    )
})

router.get('/novaEntrada', (req, res) => {
    res.render('novaEntrada')
})

router.get('/professor', (req, res) => {
    res.render('professor')
})

module.exports = router