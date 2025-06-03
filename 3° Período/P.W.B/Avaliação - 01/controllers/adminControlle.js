const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

exports.listarPerguntas = async (req, res) => {
  const perguntas = await prisma.pergunta.findMany();
  res.render('admin', { perguntas, css: 'admin' });
};

exports.adicionarPergunta = async (req, res) => {
  const { pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta } = req.body;
  await prisma.pergunta.create({
    data: { pergunta, alternativaA, alternativaB, alternativaC, respostaCorreta }
  });
  res.redirect('/admin');
};

exports.excluirPergunta = async (req, res) => {
  await prisma.pergunta.delete({ where: { id: parseInt(req.params.id) } });
  res.redirect('/admin');
};
