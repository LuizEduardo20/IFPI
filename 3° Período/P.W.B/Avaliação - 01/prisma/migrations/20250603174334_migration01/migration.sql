-- CreateTable
CREATE TABLE "Pergunta" (
    "id" SERIAL NOT NULL,
    "pergunta" TEXT NOT NULL,
    "alternativaA" TEXT NOT NULL,
    "alternativaB" TEXT NOT NULL,
    "alternativaC" TEXT NOT NULL,
    "respostaCorreta" TEXT NOT NULL,

    CONSTRAINT "Pergunta_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Resposta" (
    "id" SERIAL NOT NULL,
    "perguntaId" INTEGER NOT NULL,
    "respostaDada" TEXT NOT NULL,
    "correta" BOOLEAN NOT NULL,
    "dataHora" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "perguntaTexto" TEXT NOT NULL,
    "alternativaATexto" TEXT NOT NULL,
    "alternativaBTexto" TEXT NOT NULL,
    "alternativaCTexto" TEXT NOT NULL,

    CONSTRAINT "Resposta_pkey" PRIMARY KEY ("id")
);
