# DevMasters Project Management API

API RESTful para gerenciamento de mini-projetos da DevMasters Inc.

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic

## Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando a API

Para iniciar o servidor, execute:
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`

## Documentação

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Listar Projetos
- **GET** `/projects`
- Parâmetros de query:
  - `skip`: Número de registros a pular (padrão: 0)
  - `limit`: Número máximo de registros (padrão: 10, máximo: 100)
  - `status`: Filtrar por status ("Planejado", "Em Andamento", "Concluído", "Cancelado")
  - `priority`: Filtrar por prioridade (1-3)

### Criar Projeto
- **POST** `/projects`
- Body:
```json
{
    "title": "Título do Projeto",
    "description": "Descrição do projeto",
    "priority": 1,
    "status": "Planejado"
}
```

### Obter Projeto
- **GET** `/projects/{project_id}`

### Atualizar Projeto
- **PUT** `/projects/{project_id}`
- Body: Mesmo formato do POST

### Deletar Projeto
- **DELETE** `/projects/{project_id}` 