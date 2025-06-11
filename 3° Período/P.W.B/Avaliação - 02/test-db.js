const Question = require('./models/Question');

async function testDatabase() {
    try {
        // Tenta buscar todas as perguntas
        const questions = await Question.findAll();
        console.log('Perguntas encontradas:', questions.length);
        console.log('Primeira pergunta:', questions[0].toJSON());
    } catch (error) {
        console.error('Erro ao testar o banco:', error);
    }
}

testDatabase(); 