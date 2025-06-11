const Question = require('./Question');

// Métodos para manipular perguntas
const getPerguntas = async () => {
    try {
        console.log('Buscando todas as perguntas...')
        const perguntas = await Question.getAllQuestions()
        console.log('Perguntas encontradas:', perguntas)
        return perguntas
    } catch (error) {
        console.error('Erro ao buscar perguntas:', error)
        throw new Error('Erro ao buscar perguntas: ' + error.message)
    }
};

const getPerguntaById = async (id) => {
    try {
        console.log('Buscando pergunta por ID:', id)
        const pergunta = await Question.getQuestionById(id)
        console.log('Pergunta encontrada:', pergunta)
        return pergunta
    } catch (error) {
        console.error('Erro ao buscar pergunta:', error)
        throw new Error('Erro ao buscar pergunta: ' + error.message)
    }
};

const addPergunta = async (pergunta) => {
    try {
        console.log('Adicionando nova pergunta:', pergunta)
        const novaPergunta = await Question.createQuestion(pergunta)
        console.log('Pergunta adicionada:', novaPergunta)
        return novaPergunta
    } catch (error) {
        console.error('Erro ao adicionar pergunta:', error)
        throw new Error('Erro ao adicionar pergunta: ' + error.message)
    }
};

const deletePergunta = async (id) => {
    try {
        console.log('Deletando pergunta:', id)
        const resultado = await Question.deleteQuestion(id)
        console.log('Pergunta deletada:', resultado)
        return resultado
    } catch (error) {
        console.error('Erro ao deletar pergunta:', error)
        throw new Error('Erro ao deletar pergunta: ' + error.message)
    }
};

// Métodos adicionais úteis
const getPerguntasPorDificuldade = async (dificuldade) => {
    try {
        console.log('Buscando perguntas por dificuldade:', dificuldade)
        const perguntas = await Question.getQuestionsByDifficulty(dificuldade)
        console.log('Perguntas encontradas:', perguntas)
        return perguntas
    } catch (error) {
        console.error('Erro ao buscar perguntas por dificuldade:', error)
        throw new Error('Erro ao buscar perguntas por dificuldade: ' + error.message)
    }
};

module.exports = {
    getPerguntas,
    getPerguntaById,
    addPergunta,
    deletePergunta,
    getPerguntasPorDificuldade
};