const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('home')
})

let listaAluno = []

router.get('/cadastro', (req, res) => {
    res.render('cadastro')
})

router.get('/aluno', (req, res) => {
    res.render('aluno')
})

router.post('/aluno', (req, res) => {
    const disciplina = req.body.disciplina
    const nota1 = parseFloat(req.body.nota1)
    const nota2 = parseFloat(req.body.nota2)

    let media = (nota1 + nota2) / 2

    listaAluno.push({
        disciplina: disciplina,
        nota1: nota1,
        nota2: nota2,
        media: media
    })

    res.render('aluno', 
        { 
            listaAluno: listaAluno 
        }
    )
})

module.exports = router