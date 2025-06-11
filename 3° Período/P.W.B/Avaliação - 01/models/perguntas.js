let perguntas = []

function getPerguntas() {
  return perguntas
}

function getPerguntaById(id) {
  return perguntas.find(p => p.id === id)
}

function addPergunta(pergunta) {
  const id = perguntas.length > 0 ? Math.max(...perguntas.map(p => p.id)) + 1 : 1
  perguntas.push({ id, ...pergunta })
}

function deletePergunta(id) {
  perguntas = perguntas.filter(p => p.id !== id)
}

module.exports = {
  getPerguntas,
  getPerguntaById,
  addPergunta,
  deletePergunta
} 
