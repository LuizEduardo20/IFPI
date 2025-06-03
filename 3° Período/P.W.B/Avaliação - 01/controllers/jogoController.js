const { getPerguntas } = require('../model/pergunta');
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

exports.telaJogo = (req, res) => {
  const perguntas = getPerguntas();
  if (perguntas.length === 0) {
    return res.render('pages/jogo', { pergunta: null, painel: req.session.painel || { perguntas: 0, acertos: 0, erros: 0 }, erro: 'Nenhuma pergunta cadastrada.' });
  }
  const pergunta = perguntas[Math.floor(Math.random() * perguntas.length)];
  req.session.perguntaAtual = pergunta;
  res.render('pages/jogo', { pergunta, painel: req.session.painel || { perguntas: 0, acertos: 0, erros: 0 } });
};

exports.responder = async (req, res) => {
  const { resposta } = req.body;
  const pergunta = req.session.perguntaAtual;
  if (!req.session.painel) req.session.painel = { perguntas: 0, acertos: 0, erros: 0 };
  req.session.painel.perguntas++;

  let acertou = false;
  if (resposta === pergunta.respostaCorreta) {
    req.session.painel.acertos++;
    acertou = true;
  } else {
    req.session.painel.erros++;
  }

  // Salva a resposta no banco
  await prisma.resposta.create({
    data: {
      perguntaId: pergunta.id,
      respostaDada: resposta,
      correta: acertou,
      perguntaTexto: pergunta.pergunta,
      alternativaATexto: pergunta.alternativaA,
      alternativaBTexto: pergunta.alternativaB,
      alternativaCTexto: pergunta.alternativaC
    }
  });

  res.render('pages/resultado', { pergunta, resposta, acertou, painel: req.session.painel });
};

exports.continuar = (req, res) => {
  res.redirect('/jogo');
};