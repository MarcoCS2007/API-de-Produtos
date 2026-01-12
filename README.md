# API de Produtos (Arquitetura MVC Manual) 🐍

Este projeto consiste em uma implementação "pura" de uma API de gerenciamento de produtos, construída do zero em Python **sem a utilização de frameworks web** (como Flask ou Django).

O objetivo principal foi o estudo aprofundado de **Arquitetura de Software**, **Design Patterns** e a lógica interna de funcionamento de uma API RESTful.

## 🚀 Funcionalidades

* **CRUD Completo:** Criação, Leitura, Atualização e Deleção de produtos.
* **Múltiplos Formatos:** Capacidade de renderizar respostas em **JSON** ou **XML** via Factory Pattern.
* **Persistência Otimizada:** Banco de dados **SQLite** gerenciado através do padrão **Singleton**.
* **Lógica de Upsert:** Endpoint inteligente que cria ou atualiza dados baseado na existência do ID.
* **Tratamento de Erros:** Respostas de erro formatadas e proteção contra falhas de execução (Database/IO).

## 🏗️ Arquitetura e Design Patterns

O sistema segue rigorosamente o padrão **MVC (Model-View-Controller)**, com aplicação de conceitos SOLID:

* **Model:** Responsável direto pelo SQL e regras de negócio.
* **View:** Responsável apenas pela formatação da saída.
* **Controller:** O orquestrador que valida dados e conecta o Model à View.
* **Singleton:** Implementado na classe `Database` para garantir uma única instância de conexão com o banco durante a execução.
* **Factory Pattern:** Implementado na `FactoryView` para instanciar dinamicamente a classe de visualização correta sem acoplar o Controller.

## 📂 Estrutura do Projeto

```bash
├── controllers
│   └── controller.py       # Lógica de controle e orquestração
├── models
│   ├── Database.py         # Conexão SQLite (Padrão Singleton)
│   ├── ModelProduto.py     # Queries SQL (DAO)
│   └── Produtos.py         # Classe POJO (Objeto Python puro)
├── views
│   └── view.py             # Contém a FactoryView e as classes ViewJSON/ViewXML
├── run.py                  # Script de entrada (Simulação de Cliente/Router)
└── README.md               # Documentação do projeto

```

## 🛠️ Como Rodar

O projeto utiliza apenas a biblioteca padrão do Python 3 (não requer `pip install`).

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/API-de-Produtos.git

```


2. Navegue até a pasta:
```bash
cd API-de-Produtos

```


3. Execute o script principal:
```bash
python run.py

```



O sistema irá gerenciar o arquivo `.db` automaticamente e executar uma bateria de testes simulando requisições.

## 🤝 Créditos e Colaboração

Este projeto foi desenvolvido com foco didático em Engenharia de Software:

**Marco (Autor):**

* Desenvolvimento da lógica *core* dos Controllers, Models e Views.
* Implementação do **Singleton** para conexão eficiente com o banco.
* Implementação do **Factory Pattern** para desacoplar as Views.
* Implementação da lógica de segurança.

**Gemini (AI Assistant - Tech Lead):**

* Code Review e sugestão de boas práticas (Clean Code).
* Auxílio na depuração de Edge Cases (erros silenciosos e falhas de conexão).
* Orientação sobre a estrutura do README e documentação técnica.

---

*Desenvolvido como parte dos estudos em Python Avançado.*
