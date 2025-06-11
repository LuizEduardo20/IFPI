// Array to store questions
let perguntas = []

// Get all questions
function getPerguntas() {
  return perguntas
}

// Get a specific question by ID
function getPerguntaById(id) {
  return perguntas.find(p => p.id === id)
}

// Add a new question
function addPergunta(pergunta) {
  const id = perguntas.length > 0 ? Math.max(...perguntas.map(p => p.id)) + 1 : 1
  perguntas.push({ id, ...pergunta })
}

// Delete a question by ID
function deletePergunta(id) {
  perguntas = perguntas.filter(p => p.id !== id)
}

module.exports = {
  getPerguntas,
  getPerguntaById,
  addPergunta,
  deletePergunta
} 