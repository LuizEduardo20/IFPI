function inverterPalavra(palavra) {    
    let palavraInvertida = '';
    for(let i = palavra.length - 1; i >= 0; i--) {
        palavraInvertida += palavra[i];
    }
    return palavraInvertida;
}

function ehPalindromo(palavra) {
    palavra = palavra.toLowerCase();
    
    for(let i = 0; i < palavra.length / 2; i++) {
        if(palavra[i] !== palavra[palavra.length - 1 - i]) {
            return false;
        }
    }
    return true;
}

const palavra = "JavaScript";
console.log('Palavra original:', palavra);
console.log('Palavra invertida:', inverterPalavra(palavra));

console.log('ana é palíndromo?', ehPalindromo('Paulo'));
console.log('javascript é palíndromo?', ehPalindromo('javascript'));
console.log('ovo é palíndromo?', ehPalindromo('ovo'));
