const numeros = [3, 7, 2, 10, 15];

function media(){
    const soma = numeros.reduce((acc, num) => acc + num);
    
    const media = soma / numeros.length;
    
    return {
        soma: soma,
        media: media
    };
}

const resultado = media()
console.log(resultado.soma)
console.log(resultado.media.toFixed(2))
