# Sistema de Gerenciamento de Clientes com Python e SQLite

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)


Sistema CRUD (Create, Read, Update, Delete) para gerenciamento de clientes desenvolvido em Python com SQLite, demonstrando boas práticas de Python DB API.

## 🚀 Funcionalidades

- ✅ **Criar** novos clientes
- ✅ **Listar** todos os clientes
- ✅ **Buscar** clientes por ID, nome ou email
- ✅ **Atualizar** informações de clientes
- ✅ **Excluir** clientes
- ✅ **Inserção em lote** de múltiplos clientes
- ✅ **Prevenção contra SQL Injection**
- ✅ **Tratamento de erros** com rollback

## 📋 Tecnologias Utilizadas

- **Python 3.8+**
- **SQLite3**
- **Pathlib** para manipulação de caminhos
- **DB-API 2.0** (Padrão Python para bancos de dados)

## 🛠️ Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- Git


```bash
# Clone o repositório
git clone https://github.com/AAkwk/sistema-clientes-sqlite-python-simples.git

# Acesse o diretório
cd sistema-clientes-sqlite-python-simples

# Execute o script
python cliente_manager.py
```
## 📦 Estrutura do Projeto

```
sistema-clientes-sqlite-python-simples/
│
├── cliente_manager.py # 🏠 Arquivo principal
├── meu_banco.sqlite # 💾 Banco de dados (auto-criado)
└── README.md # 📖 Este arquivo
```
💡 Como Usar
Exemplo Básico
```python
# Criar tabela (executar uma vez)
criar_tabela(conexao, cursor)

# Adicionar cliente
inserir_cliente(conexao, cursor, "Maria Silva", "maria@email.com")

# Listar todos
consultar_clientes(cursor)

# Buscar por nome
consultar_cliente_por_nome(cursor, "Maria")
```

## Buscas Disponíveis

```python
consultar_cliente_por_id(cursor, 1)      # 🔍 Por ID
consultar_cliente_por_nome(cursor, "Jo") # 🔍 Por nome (parcial)
consultar_clientes_por_email(cursor, "@gmail") # 🔍 Por email
```
## 🛡️ Segurança Implementada
### ✅ Proteção Anti SQL Injection
```python
# FORMA CORRETA (usando placeholders)
cursor.execute("SELECT * FROM clientes WHERE id=?", (id_cliente,))

# FORMA INCORRETA (vulnerável)
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
```

## ✅ Tratamento de Erros
```python
try:
    # Operações de banco
    conexao.commit()
except Exception as e:
    print("Erro:", e)
    conexao.rollback()  # 🔄 Desfaz em caso de erro
```

## 🗃️ Estrutura da Tabela
|Coluna|	Tipo|Descrição|
|------|-------|--------|
|id|	INTEGER PRIMARY KEY AUTOINCREMENT|	Chave única - auto incrementada|
|nome|	VARCHAR(100)|	Nome completo|
|email|	VARCHAR(150)|	E-mail|


## 🎯 Para Quem é Este Projeto
- 👶 Iniciantes em Python: Código simples e comentado

- 🎓 Estudantes: Excelente para aprender DB-API

- 💼 Candidatos a vagas Júnior: Demonstra conhecimentos básicos

- 🚀 Devs que querem um CRUD rápido

## 📚 O Que Você Aprende Com Este Código
- Conexão com Banco SQLite

- Operações CRUD completas

- Prevenção de SQL Injection

- Tratamento de exceções

- Padrão DB-API do Python



