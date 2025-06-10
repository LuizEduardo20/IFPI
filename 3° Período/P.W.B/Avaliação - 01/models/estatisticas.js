// Objeto para armazenar as estatísticas
let estatisticas = {
  totalRespondidas: 0,
  acertos: 0,
  erros: 0
}

// Função para obter as estatísticas
function getEstatisticas() {
  return estatisticas
}

// Função para atualizar as estatísticas
function atualizarEstatisticas(acertou) {
  estatisticas.totalRespondidas++
  if (acertou) {
    estatisticas.acertos++
  } else {
    estatisticas.erros++
  }
}

// Função para reiniciar as estatísticas
function reiniciarEstatisticas() {
  estatisticas = {
    totalRespondidas: 0,
    acertos: 0,
    erros: 0
  }
}

module.exports = {
  getEstatisticas,
  atualizarEstatisticas,
  reiniciarEstatisticas
} 