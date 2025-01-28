function getByID(id) {
    return document.getElementById(id);
}

// Elementos do DOM
let botaoConsultar = getByID('botaoConsultar');
let botaoInverter = getByID('botaoInverter');
let botaoLimpar = getByID('botaoLimpar');
let moedaBaseInput = getByID('moedaBase');
let moedaConversaoInput = getByID('moedaConversao');
let resultado = getByID('resultado');

// Pares de moedas mais comuns na Binance
const moedasComuns = {
    'BTC': ['USDT', 'BUSD', 'EUR', 'BRL'],
    'ETH': ['USDT', 'BUSD', 'BTC', 'BRL'],
    'BNB': ['USDT', 'BUSD', 'BTC', 'BRL'],
    'ADA': ['USDT', 'BUSD', 'BTC'],
    'DOGE': ['USDT', 'BUSD', 'BTC'],
    'XRP': ['USDT', 'BUSD', 'BTC'],
    'SOL': ['USDT', 'BUSD', 'BTC'],
    'DOT': ['USDT', 'BUSD', 'BTC'],
    'USDT': ['BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'XRP', 'SOL', 'DOT', 'BRL', 'EUR'],
    'BUSD': ['BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'XRP', 'SOL', 'DOT'],
    'BRL': ['BTC', 'ETH', 'BNB', 'USDT'],
    'EUR': ['BTC', 'ETH', 'USDT']
};

// Event Listeners
botaoConsultar.addEventListener('click', consultarPreco);
botaoInverter.addEventListener('click', inverterMoedas);
botaoLimpar.addEventListener('click', limparCampos);

function inverterMoedas() {
    let temp = moedaBaseInput.value;
    moedaBaseInput.value = moedaConversaoInput.value;
    moedaConversaoInput.value = temp;
    
    // Limpa o resultado anterior quando inverter
    resultado.innerHTML = '';
}

function limparCampos() {
    moedaBaseInput.value = '';
    moedaConversaoInput.value = '';
    resultado.innerHTML = '';
}

// Atualizar o datalist no HTML
function atualizarDatalist() {
    const datalist = getByID('moedasPopulares');
    datalist.innerHTML = ''; // Limpa o datalist existente
    
    // Adiciona todas as moedas base
    Object.keys(moedasComuns).forEach(moeda => {
        const option = document.createElement('option');
        option.value = moeda;
        datalist.appendChild(option);
    });
    
    // Adiciona moedas de conversão comuns
    ['USDT', 'BUSD', 'BRL', 'EUR'].forEach(moeda => {
        const option = document.createElement('option');
        option.value = moeda;
        datalist.appendChild(option);
    });
}

async function consultarPreco() {
    // Validação de campos vazios
    if (!moedaBaseInput.value || !moedaConversaoInput.value) {
        resultado.innerHTML = 'Erro: Por favor, preencha ambos os campos de moeda.';
        return;
    }

    let moedaBase = moedaBaseInput.value.toUpperCase();
    let moedaConversao = moedaConversaoInput.value.toUpperCase();

    // Validação de par de moedas
    if (moedasComuns[moedaBase] && !moedasComuns[moedaBase].includes(moedaConversao)) {
        // Tenta verificar se o par inverso existe
        if (moedasComuns[moedaConversao] && moedasComuns[moedaConversao].includes(moedaBase)) {
            // Se existir o par inverso, inverte automaticamente
            let tempMoeda = moedaBase;
            moedaBase = moedaConversao;
            moedaConversao = tempMoeda;
            
            // Atualiza os inputs
            moedaBaseInput.value = moedaBase;
            moedaConversaoInput.value = moedaConversao;
        } else {
            resultado.innerHTML = `Erro: Par de moedas ${moedaBase}/${moedaConversao} não disponível.<br>
                Moedas de conversão disponíveis para ${moedaBase}: ${moedasComuns[moedaBase].join(', ')}`;
            return;
        }
    }
    
    let url = `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;
    
    try {
        resultado.innerHTML = 'Consultando...';
        let response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`Par de moedas ${moedaBase}/${moedaConversao} não encontrado na Binance`);
        }
        
        let json = await response.json();
        let preco = parseFloat(json.price);

        // Se foi necessário inverter o par, inverte também o preço
        if (moedaBase !== moedaBaseInput.value.toUpperCase()) {
            preco = 1 / preco;
        }

        resultado.innerHTML = `
            <p><strong>Par de Moedas:</strong> ${moedaBaseInput.value.toUpperCase()}/${moedaConversaoInput.value.toUpperCase()}</p>
            <p><strong>Preço:</strong> ${preco.toFixed(8)} ${moedaConversaoInput.value.toUpperCase()}</p>`;
    } catch (error) {
        resultado.innerHTML = 'Erro: ' + error.message;
    }
}

// Inicializar datalist ao carregar a página
atualizarDatalist(); 