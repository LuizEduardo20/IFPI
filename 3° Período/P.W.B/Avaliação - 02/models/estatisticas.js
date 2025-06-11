const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Estatistica = sequelize.define('Estatistica', {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true
    },
    userId: {
        type: DataTypes.INTEGER,
        allowNull: true // Permitindo que seja nulo para estatísticas globais
    },
    totalRespondidas: {
        type: DataTypes.INTEGER,
        defaultValue: 0
    },
    acertos: {
        type: DataTypes.INTEGER,
        defaultValue: 0
    },
    erros: {
        type: DataTypes.INTEGER,
        defaultValue: 0
    }
});

// Métodos CRUD
Estatistica.getEstatisticas = async (userId = null) => {
    try {
        const whereClause = userId ? { userId } : {};
        const stats = await Estatistica.findOne({ where: whereClause });
        if (!stats) {
            // Se não existir, cria um novo registro
            return await Estatistica.create({ userId });
        }
        return stats;
    } catch (error) {
        throw new Error('Erro ao buscar estatísticas: ' + error.message);
    }
};

Estatistica.atualizarEstatisticas = async (acertou, userId = null) => {
    try {
        const whereClause = userId ? { userId } : {};
        const stats = await Estatistica.findOne({ where: whereClause });
        if (!stats) {
            return await Estatistica.create({
                userId,
                totalRespondidas: 1,
                acertos: acertou ? 1 : 0,
                erros: acertou ? 0 : 1
            });
        }

        stats.totalRespondidas += 1;
        if (acertou) {
            stats.acertos += 1;
        } else {
            stats.erros += 1;
        }

        return await stats.save();
    } catch (error) {
        throw new Error('Erro ao atualizar estatísticas: ' + error.message);
    }
};

Estatistica.reiniciarEstatisticas = async (userId = null) => {
    try {
        const whereClause = userId ? { userId } : {};
        const stats = await Estatistica.findOne({ where: whereClause });
        if (!stats) {
            return await Estatistica.create({ userId });
        }

        stats.totalRespondidas = 0;
        stats.acertos = 0;
        stats.erros = 0;

        return await stats.save();
    } catch (error) {
        throw new Error('Erro ao reiniciar estatísticas: ' + error.message);
    }
};

// Método para obter estatísticas globais
Estatistica.getEstatisticasGlobais = async () => {
    try {
        const stats = await Estatistica.findOne({ where: { userId: null } });
        if (!stats) {
            return await Estatistica.create({ userId: null });
        }
        return stats;
    } catch (error) {
        throw new Error('Erro ao buscar estatísticas globais: ' + error.message);
    }
};

module.exports = Estatistica; 