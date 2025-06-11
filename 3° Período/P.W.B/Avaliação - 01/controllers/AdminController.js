const { getPerguntas, addPergunta, deletePergunta } = require('../models/perguntas')
const { getEstatisticas, reiniciarEstatisticas } = require('../models/estatisticas')

class AdminController {
    static index(req, res) {
        const perguntas = getPerguntas()
        const estatisticas = getEstatisticas()
        res.render('pages/admin', { perguntas, estatisticas })
    }

    static adicionarPergunta(req, res) {
        const { pergunta, alternativa1, alternativa2, alternativa3, correta } = req.body
        addPergunta({ 
            pergunta, 
            alternativa1, 
            alternativa2, 
            alternativa3, 
            correta: parseInt(correta) 
        })
        res.redirect('/admin')
    }

    static deletarPergunta(req, res) {
        const id = parseInt(req.params.id)
        deletePergunta(id)
        res.redirect('/admin')
    }

    static reiniciarEstatisticas(req, res) {
        reiniciarEstatisticas()
        res.redirect('/')
    }
}

module.exports = AdminController 