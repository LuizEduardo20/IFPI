const sequelize = require('./database');
const User = require('../models/User');
const Question = require('../models/Question');
const Estatistica = require('../models/estatisticas');

async function initDatabase() {
    try {
        console.log('Iniciando sincronização do banco de dados...')
        // Sincroniza os modelos com o banco de dados
        await sequelize.sync({ force: true }); // force: true vai recriar as tabelas
        console.log('Banco de dados inicializado com sucesso!');
        
        // Criando algumas perguntas de exemplo
        console.log('Criando perguntas de exemplo...')
        
        const pergunta1 = await Question.create({
            question: "Qual é a capital do Brasil?",
            correctAnswer: "Brasília",
            options: ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
            difficulty: 1
        });
        console.log('Pergunta 1 criada:', pergunta1.toJSON());

        const pergunta2 = await Question.create({
            question: "Qual é o maior planeta do sistema solar?",
            correctAnswer: "Júpiter",
            options: ["Saturno", "Júpiter", "Netuno", "Urano"],
            difficulty: 2
        });
        console.log('Pergunta 2 criada:', pergunta2.toJSON());

        // Criando estatísticas iniciais
        console.log('Criando estatísticas iniciais...')
        const estatisticas = await Estatistica.create({
            userId: null,
            totalRespondidas: 0,
            acertos: 0,
            erros: 0
        });
        console.log('Estatísticas iniciais criadas:', estatisticas.toJSON());

        console.log('Dados iniciais criados com sucesso!');
    } catch (error) {
        console.error('Erro detalhado ao inicializar o banco de dados:', error);
        throw error; // Propaga o erro para ser tratado no nível superior
    }
}

module.exports = initDatabase; 