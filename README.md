# Sistema de Estética Automotiva

API REST para gerenciamento de clientes, veículos e serviços de uma empresa de estética automotiva.

O projeto encontra-se em desenvolvimento ativo e atualmente possui o módulo de Clientes implementado e o módulo de Veículos em construção.

Este projeto está sendo construído como uma solução real para um pequeno negócio e também como projeto de portfólio, com foco em arquitetura organizada, boas práticas de desenvolvimento, testes automatizados e escalabilidade.

## Status do Projeto

Em desenvolvimento

### Concluído

- CRUD completo de Clientes
- Relacionamento Cliente → Veículo
- Cadastro de Veículos
- Migrações com Alembic
- Testes automatizados iniciais
- Documentação automática com Swagger

### Em andamento

- CRUD completo de Veículos

## Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* Alembic
* SQLite
* Pydantic
* Pytest
* Git e GitHub

## Competências Demonstradas

* Desenvolvimento de APIs REST
* Arquitetura em camadas
* Modelagem de banco de dados relacional
* Relacionamentos entre entidades
* Migrações de banco com Alembic
* Validação de dados com Pydantic
* Testes automatizados com Pytest
* Tratamento de erros e exceções
* Boas práticas de organização de código
* Controle de versão com Git

## Funcionalidades Implementadas

### Clientes

* Cadastro de clientes
* Listagem de clientes
* Busca de cliente por ID
* Busca de clientes por nome
* Atualização de clientes
* Exclusão de clientes
* Tratamento de erros HTTP (404)

### Veículos

* Cadastro de veículos
* Associação de veículos a clientes
* Validação de cliente existente
* Validação de placa única
* Retorno das informações básicas do proprietário vinculadas ao veículo

## Próximas Implementações

### Veículos

* Listagem de veículos
* Busca de veículo por ID
* Atualização de veículos
* Exclusão de veículos

### Serviços

* Cadastro de serviços realizados
* Histórico de serviços por cliente
* Histórico de serviços por veículo

### Gestão

* Agendamento de serviços
* Relatórios operacionais
* Dashboard gerencial
* Autenticação de usuários

## Estrutura Atual do Projeto

```text
Sistema-Estetica-Automotiva
│
├── backend
│   ├── app
│   │   ├── core
│   │   ├── database
│   │   ├── models
│   │   ├── routes
│   │   ├── schemas
│   │   ├── services
│   │   └── utils
│   │
│   ├── alembic
│   ├── tests
│   ├── main.py
│   └── requirements.txt
│
├── docs
└── frontend
```

### Banco de Dados

O projeto utiliza SQLite para desenvolvimento local.

O banco de dados não é versionado no repositório e será criado localmente através das migrações do Alembic.

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/guialves987/Sistema-Estetica-Automotiva.git
```

### 2. Acessar a pasta backend

```bash
cd backend
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```powershell
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Executar migrações

```bash
alembic upgrade head
```

### 7. Iniciar a aplicação

```bash
uvicorn main:app --reload
```

## Documentação da API

Após iniciar o servidor:

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

## Testes Automatizados

O projeto utiliza **Pytest** e **FastAPI TestClient** para validação dos endpoints da API.

Atualmente os testes implementados cobrem os seguintes cenários:

* **Endpoint raiz**: verifica se a API está disponível e respondendo corretamente.
* **Criação de cliente**: valida o cadastro de um cliente e a estrutura da resposta retornada.
* **Listagem de clientes**: verifica se a API retorna uma lista de clientes.
* **Busca de cliente inexistente**: valida o retorno HTTP 404 para identificadores não encontrados.
* **Atualização de cliente inexistente**: verifica o tratamento adequado para tentativas de atualização de registros inexistentes.
* **Exclusão de cliente inexistente**: valida o retorno HTTP 404 ao tentar remover um cliente que não existe.

Para executar os testes:

```PowerShell
pytest
```

A cobertura de testes será expandida conforme a evolução dos módulos de Clientes, Veículos e Serviços.


## Autor

Guilherme Alves

- GitHub: https://github.com/guialves987
- LinkedIn: https://www.linkedin.com/in/guialvesads/
