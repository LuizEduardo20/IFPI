const { getPerguntas, getPerguntaById } = require('../models/perguntas')
const { getEstatisticas, atualizarEstatisticas } = require('../models/estatisticas')

class JogoController {
    static home(req, res) {
        const estatisticas = getEstatisticas()
        if (!req.session.perguntasRespondidas) {
            req.session.perguntasRespondidas = []
        }
        res.render('pages/home', { estatisticas })
    }

    static iniciarJogo(req, res) {
        const perguntas = getPerguntas()
        if (perguntas.length === 0) {
            return res.redirect('/')
        }

        const perguntasDisponiveis = perguntas.filter(p => 
            !req.session.perguntasRespondidas.includes(p.id)
        )

        if (perguntasDisponiveis.length === 0) {
            const estatisticas = getEstatisticas()
            return res.render('pages/fim-quiz', { estatisticas })
        }

        const pergunta = perguntasDisponiveis[Math.floor(Math.random() * perguntasDisponiveis.length)]
        const estatisticas = getEstatisticas()
        res.render('pages/jogo', { pergunta, estatisticas })
    }

    static verificarResposta(req, res) {
        const { perguntaId, resposta } = req.body
        const pergunta = getPerguntaById(parseInt(perguntaId))
        
        if (!pergunta) {
            return res.redirect('/jogo')
        }

        const acertou = parseInt(resposta) === pergunta.correta
        atualizarEstatisticas(acertou)
        
        if (!req.session.perguntasRespondidas.includes(pergunta.id)) {
            req.session.perguntasRespondidas.push(pergunta.id)
        }

        const estatisticas = getEstatisticas()
        res.render('pages/resultado', { acertou, pergunta, estatisticas })
    }

    static resultado(req, res) {
        const estatisticas = getEstatisticas()
        res.render('pages/resultado', { estatisticas })
    }

    static reiniciarJogo(req, res) {
        req.session.perguntasRespondidas = []
        res.redirect('/jogo')
    }
}

module.exports = JogoController 