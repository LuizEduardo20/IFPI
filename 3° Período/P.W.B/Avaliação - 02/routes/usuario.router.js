const express = require('express')
const router = express.Router()
const usuarioController = require('../controllers/usuario.controller')


router.get('/entrar', (req, res) => {
    res.render('pages/user/signin',
        {
            title: 'Entrar',
        })
})

router.post('/login', usuarioController.login)

router.get('/logout', usuarioController.logout)

router.get('/novo', (req, res) => {
    res.render('pages/user/signup',
        {
            title: 'Novo Usuário',
        })
})

router.post('/salvar', usuarioController.save)

module.exports = router