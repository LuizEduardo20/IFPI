const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, '../data/perguntas.json');

function getPerguntas() {
  return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
}

function addPergunta(questao) {
  const perguntas = getPerguntas();
  questao.id = perguntas.length ? perguntas[perguntas.length - 1].id + 1 : 1;
  perguntas.push(questao);
  fs.writeFileSync(filePath, JSON.stringify(perguntas, null, 2));
}

function deletePergunta(id) {
  let perguntas = getPerguntas();
  perguntas = perguntas.filter(q => q.id !== id);
  fs.writeFileSync(filePath, JSON.stringify(perguntas, null, 2));
}

module.exports = { getPerguntas, addPergunta, deletePergunta };
