function crescimento(A, B){
    let popA = A;
    let popB = B;
    let anos = 0;

    for(let i = 0; i < 100; i++){
        const crescimentoA = popA * (3 / 100)
        const crescimentoB = popB * (1.5 / 100)
        popA += crescimentoA
        popB += crescimentoB
        anos++

        if(popA >= popB) break;
    }

    return {
        anos: anos,
        populacaoA: popA,
        populacaoB: popB
    }
}

const resultado = crescimento(80000, 200000)
console.log(`Anos necessários: ${resultado.anos}`)
console.log(`População A: ${resultado.populacaoA.toFixed(2)}`)
console.log(`População B: ${resultado.populacaoB.toFixed(2)}`)
