<div align="center">

# Gestão de Produtos — Python + MongoDB

Aplicação de terminal para gerenciamento de produtos utilizando Python e MongoDB.

![Python](https://img.shields.io/badge/Python-0D1117?style=for-the-badge&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-0D1117?style=for-the-badge&logo=mongodb&logoColor=white)

</div>

---

## `> sobre_o_projeto`

Projeto acadêmico criado para praticar operações com banco de dados **NoSQL**, utilizando MongoDB como persistência e Python como linguagem principal.

A aplicação trabalha com uma coleção de produtos contendo informações como nome, preço, margem de lucro, categoria e quantidade em estoque.

## `> funcionalidades`

- Inserção automática de produtos iniciais
- Cadastro de novos produtos
- Listagem dos itens armazenados
- Atualização de preço e lucro em lote
- Exclusão de produtos por ID
- Persistência em MongoDB

## `> stack`

- **Python**
- **MongoDB**
- **PyMongo**

## `> executando_localmente`

1. Certifique-se de que o MongoDB esteja rodando em:

```text
mongodb://localhost:27017/
```

2. Instale a dependência:

```bash
pip install pymongo
```

3. Execute:

```bash
python produtos.py
```

O projeto cria e utiliza o banco `senai_prova` e a coleção `produtos`.

## `> objetivo`

Praticar modelagem documental, operações CRUD e manipulação de dados em MongoDB com Python.

---

<div align="center">

Desenvolvido por **Pedro Henrique** · [@phz9ra](https://github.com/phz9ra)

</div>
