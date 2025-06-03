const express = require('express');
const router = express.Router();
const jogoController = require('../controllers/jogoController');

router.get('/', jogoController.telaJogo);
router.post('/responder', jogoController.responder);
router.get('/continuar', jogoController.continuar);

module.exports = router;
