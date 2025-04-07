function maiorMenor(){
    const valores = [10, 20, 30]

    const maior = Math.max(...valores)
    const menor = Math.min(...valores)

    console.log(`O maior valor é ${maior}`)
    console.log(`O menor valor é ${menor}`)
}
maiorMenor()
