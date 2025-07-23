const express = require('express')
const router = express.Router()
const operacaoController = require('../controllers/operacao.controller');
const usuarioController = require('../controllers/usuario.controller');


router.get('/novo',
    usuarioController.mustBeAuthenticated,
    (req, res) => {
        res.render('pages/nova_operacao', {
            title: 'Nova Operação',
        });
    })

router.post('/salvar',
    usuarioController.mustBeAuthenticated,
    operacaoController.save)


router.get('/operacoes',
    usuarioController.mustBeAuthenticated,
    operacaoController.getUserPosts
)

router.get('/editar/:id',
    usuarioController.mustBeAuthenticated,
    operacaoController.editForm)

router.post('/atualizar/:id',
    usuarioController.mustBeAuthenticated,
    operacaoController.update)

router.post('/excluir/:id',
    usuarioController.mustBeAuthenticated,
    operacaoController.delete)

module.exports = router