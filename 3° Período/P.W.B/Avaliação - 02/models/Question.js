const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Question = sequelize.define('Question', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    question: {
        type: DataTypes.TEXT,
        allowNull: false
    },
    correctAnswer: {
        type: DataTypes.STRING,
        allowNull: false
    },
    options: {
        type: DataTypes.JSON,
        allowNull: false
    },
    difficulty: {
        type: DataTypes.INTEGER,
        defaultValue: 1
    }
});

// Métodos CRUD
Question.createQuestion = async (questionData) => {
    try {
        return await Question.create(questionData);
    } catch (error) {
        throw new Error('Erro ao criar pergunta: ' + error.message);
    }
};

Question.getQuestionById = async (id) => {
    try {
        const question = await Question.findByPk(id);
        if (!question) throw new Error('Pergunta não encontrada');
        return question;
    } catch (error) {
        throw new Error('Erro ao buscar pergunta: ' + error.message);
    }
};

Question.updateQuestion = async (id, questionData) => {
    try {
        const question = await Question.findByPk(id);
        if (!question) throw new Error('Pergunta não encontrada');
        return await question.update(questionData);
    } catch (error) {
        throw new Error('Erro ao atualizar pergunta: ' + error.message);
    }
};

Question.deleteQuestion = async (id) => {
    try {
        const question = await Question.findByPk(id);
        if (!question) throw new Error('Pergunta não encontrada');
        return await question.destroy();
    } catch (error) {
        throw new Error('Erro ao deletar pergunta: ' + error.message);
    }
};

Question.getAllQuestions = async () => {
    try {
        return await Question.findAll();
    } catch (error) {
        throw new Error('Erro ao buscar perguntas: ' + error.message);
    }
};

Question.getQuestionsByDifficulty = async (difficulty) => {
    try {
        return await Question.findAll({
            where: { difficulty }
        });
    } catch (error) {
        throw new Error('Erro ao buscar perguntas por dificuldade: ' + error.message);
    }
};

module.exports = Question; 