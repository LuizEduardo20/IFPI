const express = require('express')
const router = express.Router()
const { getPerguntas, addPergunta, deletePergunta, getPerguntaById } = require('../models/perguntas')
const { getEstatisticas, atualizarEstatisticas, reiniciarEstatisticas } = require('../models/estatisticas')

router.get('/', (req, res) => {
  const estatisticas = getEstatisticas()
  res.render('pages/home', { estatisticas })
})

router.get('/jogo', (req, res) => {
  const perguntas = getPerguntas()
  if (perguntas.length === 0) {
    return res.redirect('/')
  }
  const pergunta = perguntas[Math.floor(Math.random() * perguntas.length)]
  const estatisticas = getEstatisticas()
  res.render('pages/jogo', { pergunta, estatisticas })
})

router.post('/verificar', (req, res) => {
  const { perguntaId, resposta } = req.body
  const pergunta = getPerguntaById(parseInt(perguntaId))
  
  if (!pergunta) {
    return res.redirect('/jogo')
  }

  const acertou = parseInt(resposta) === pergunta.correta
  atualizarEstatisticas(acertou)
  const estatisticas = getEstatisticas()
  res.render('pages/resultado', { acertou, pergunta, estatisticas })
})

router.get('/resultado', (req, res) => {
  const estatisticas = getEstatisticas()
  res.render('pages/resultado', { estatisticas })
})

router.get('/admin', (req, res) => {
  const perguntas = getPerguntas()
  const estatisticas = getEstatisticas()
  res.render('pages/admin', { perguntas, estatisticas })
})

router.post('/admin/adicionar', (req, res) => {
  const { pergunta, alternativa1, alternativa2, alternativa3, correta } = req.body
  addPergunta({ pergunta, alternativa1, alternativa2, alternativa3, correta: parseInt(correta) })
  res.redirect('/admin')
})

router.post('/admin/deletar/:id', (req, res) => {
  const id = parseInt(req.params.id)
  deletePergunta(id)
  res.redirect('/admin')
})

router.post('/reiniciar', (req, res) => {
  reiniciarEstatisticas()
  res.redirect('/')
})

module.exports = router