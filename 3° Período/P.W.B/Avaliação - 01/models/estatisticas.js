let estatisticas = {
  totalRespondidas: 0,
  acertos: 0,
  erros: 0
}

function getEstatisticas() {
  return estatisticas
}

function atualizarEstatisticas(acertou) {
  estatisticas.totalRespondidas++
  if (acertou) {
    estatisticas.acertos++
  } else {
    estatisticas.erros++
  }
}

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
