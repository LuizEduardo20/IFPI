const Operacao = require('../models/operacao')

exports.save = function (req, res) {
    const operacao = new Operacao(req.body, req.session.usuario.id)
    operacao.validate()
    if (operacao.errors.length > 0) {
        return res.send(operacao.errors)
    } else {
        operacao.create()
            .then((result) => {
                res.send(`Operação salva com sucesso com o id: ${result}`)
            })
            .catch((error) => {
                res.status(500).send(error)
            })
    }
}

exports.getUserOperations = function (req, res) {
    const operacao = new Operacao({}, req.session.usuario.id)
    operacao.readUserOperations()
        .then((result) => {
            res.render('pages/myoperations', {
                title: 'Minhas Operações',
                operations: result,
                paginaAtiva: 'operacao',
                usuario: req.session.usuario
            })
        })
        .catch((error) => {
            res.status(500).send(error)
        })
}

exports.editForm = function (req, res) {
    const Operacao = require('../models/operacao');
    const operacao = new Operacao({}, req.session.usuario.id);
    operacao.idDaOperacao = req.params.id;
    operacao.readById()
        .then((result) => {
            if (!result) return res.status(404).send('Operação não encontrada');
            res.render('pages/editar_operacao', {
                title: 'Editar Operação',
                operacao: result,
                usuario: req.session.usuario
            });
        })
        .catch((error) => res.status(500).send(error));
}

exports.update = function (req, res) {
    const Operacao = require('../models/operacao');
    const operacao = new Operacao(req.body, req.session.usuario.id);
    operacao.idDaOperacao = req.params.id;
    operacao.validate();
    if (operacao.errors.length > 0) {
        return res.send(operacao.errors);
    } else {
        operacao.update()
            .then(() => {
                res.redirect('/operacoes/operacoes');
            })
            .catch((error) => res.status(500).send(error));
    }
}

exports.delete = function (req, res) {
    const Operacao = require('../models/operacao');
    const operacao = new Operacao({}, req.session.usuario.id);
    operacao.idDaOperacao = req.params.id;
    operacao.delete()
        .then(() => {
            res.redirect('/operacoes/operacoes');
        })
        .catch((error) => res.status(500).send(error));
}