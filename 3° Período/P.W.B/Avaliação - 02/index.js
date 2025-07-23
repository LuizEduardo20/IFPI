const express = require('express')
const session = require('express-session')
const pgSession = require('connect-pg-simple')(session);
const pool = require('./db/postgres.js');
const app = express()
const port = 3000

// roteamentos
const router = require('./routes/router')
const operacoesRouter = require('./routes/operacoes.router')
const usuarioRouter = require('./routes/usuario.router')

/* Importa o express-ejs-layouts para o EJS que permite usar layouts
 para reaproveitamento de templates em views EJS */
const expressLayouts = require('express-ejs-layouts')

/* Definie o local onde estão localizadas as views do projeto */
app.set('views', 'views')
/* Define o template engine que será utilizado para renderizar as views */
// O EJS é um template engine que permite criar views dinâmicas utilizando JavaScript
app.set('view engine', 'ejs')

/* Define o layout de reaproveitamento de templates padrão que 
será utilizado para renderizar as views */
app.use(expressLayouts);

/* Define o local onde estão localizados os arquivos estáticos do projeto */
app.use(express.static('public'))

/*
body-parser é Middleware para fazer o parse do corpo da requisição antes de utilizarmos o req.body
O express.urlencoded() faz o parse do corpo da requisição para o formato URL-encoded.
O valor falso para extended indica que o body-parser vai aceitar somente strings e arrays, enquanto
o valor verdadeiro indica que o body-parser vai aceitar objetos aninhados ou qualquer outro tipo.
*/
app.use(express.urlencoded({ extended: false }))

// Configuração de sessões do usuário
app.use(session({
    store: new pgSession({
        pool: pool,
        tableName: 'session'
    }),
    secret: process.env.SESSION_SECRET || 'iMoney-secret-key',
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: false,
        maxAge: 24 * 60 * 60 * 1000,
        httpOnly: true
    }
}))

app.use((req, res, next) => {
    res.locals.usuario = req.session.usuario
    next()
})

app.use('/', router)
app.use('/operacoes', operacoesRouter)
app.use('/usuario', usuarioRouter)

app.listen(port, () => {
    console.log(`iMoney app listening on http://localhost:${port}`)
})