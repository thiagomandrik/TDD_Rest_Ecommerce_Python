# Projeto: Aplicação de TDD no Desenvolvimento de APIs RESTful para E-commerce com Python

## Visão Geral

Este projeto tem como objetivo demonstrar, na prática, a aplicação da metodologia **Test-Driven Development (TDD)** no desenvolvimento de uma API RESTful voltada para o setor de e-commerce. O desenvolvimento foi realizado com a linguagem **Python**, utilizando o framework **FastAPI**.

O foco está em criar um backend robusto, testável e com alta cobertura de testes automatizados, seguindo os princípios de TDD: **Red → Green → Refactor**.

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** - Framework para construção da API REST
- **SQLAlchemy** - ORM para persistência de dados
- **Alembic** - Migrações de banco de dados
- **SQLite** - Banco de dados para ambiente de desenvolvimento
- **Pytest** - Framework de testes
- **pytest-cov** - Relatórios de cobertura de código
- **Docker** - Ambiente isolado

---

## Funcionalidades Implementadas

- **Gerenciamento de Usuários:**
  - Cadastro de novos usuários
  - Autenticação via JWT
  - Listagem de usuários

- **Gerenciamento de Produtos:**
  - Cadastro de produtos
  - Consulta de lista de produtos
  - Consulta de produto por ID

- **Gerenciamento de Pedidos:**
  - Criação de pedidos
  - Listagem de pedidos por usuário

---

## Fluxo de Desenvolvimento com TDD

Para cada funcionalidade:

1. **Escrever o teste que falha**
   - Exemplo: `test_create_product_returns_201`

2. **Implementar o código mínimo para passar no teste**
   - Exemplo: Criar o método `create_product` no service e o endpoint no router

3. **Refatorar mantendo os testes verdes**
   - Exemplo: Melhorar nomeação, validar entradas com Pydantic, remover código duplicado

4. **Repetir o ciclo para cada requisito funcional**


---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/thiagomandrik/TDD_Rest_Ecommerce_Python.git
```


### 2. Criar o ambiente virtual

```bash
cd TDD_Rest_Ecommerce_Python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Rodar as migrações de banco

```bash
alembic upgrade head
```

### 4. Executar a aplicação

```bash
uvicorn app.main:app --reload

ou

fastapi dev app/main.py
```

### 5. Rodar os testes

```bash
task test
```