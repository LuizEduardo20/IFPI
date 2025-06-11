const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const User = sequelize.define('User', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
        unique: true
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false
    },
    score: {
        type: DataTypes.INTEGER,
        defaultValue: 0
    }
});

// Métodos CRUD
User.createUser = async (userData) => {
    try {
        return await User.create(userData);
    } catch (error) {
        throw new Error('Erro ao criar usuário: ' + error.message);
    }
};

User.findByEmail = async (email) => {
    try {
        return await User.findOne({ where: { email } });
    } catch (error) {
        throw new Error('Erro ao buscar usuário: ' + error.message);
    }
};

User.updateScore = async (userId, newScore) => {
    try {
        const user = await User.findByPk(userId);
        if (!user) throw new Error('Usuário não encontrado');
        user.score = newScore;
        return await user.save();
    } catch (error) {
        throw new Error('Erro ao atualizar pontuação: ' + error.message);
    }
};

User.deleteUser = async (userId) => {
    try {
        const user = await User.findByPk(userId);
        if (!user) throw new Error('Usuário não encontrado');
        return await user.destroy();
    } catch (error) {
        throw new Error('Erro ao deletar usuário: ' + error.message);
    }
};

User.getAllUsers = async () => {
    try {
        return await User.findAll();
    } catch (error) {
        throw new Error('Erro ao buscar usuários: ' + error.message);
    }
};

module.exports = User; 