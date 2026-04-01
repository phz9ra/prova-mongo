from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["senai_prova"]
col = db["produtos"]

def inserir_iniciais():
    if col.count_documents({}) == 0:
        produtos_iniciais = [
            {"nome": "Notebook",      "preco": 3500.00, "lucro": 20.0, "categoria": "Eletrônicos",   "quantidade": 10},
            {"nome": "Mouse",         "preco":   80.00, "lucro": 30.0, "categoria": "Periféricos",   "quantidade": 50},
            {"nome": "Teclado",       "preco":  150.00, "lucro": 25.0, "categoria": "Periféricos",   "quantidade": 30},
            {"nome": "Monitor",       "preco": 1200.00, "lucro": 18.0, "categoria": "Eletrônicos",   "quantidade": 15},
            {"nome": "Headset",       "preco":  250.00, "lucro": 22.0, "categoria": "Acessórios",    "quantidade": 20},
        ]
        col.insert_many(produtos_iniciais)
        print("5 produtos iniciais cadastrados com sucesso!\n")
    else:
        print("Banco já contém produtos. Pulando cadastro inicial.\n")

#  Listar produtos 
def listar_produtos():
    produtos = list(col.find())
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return
    print(f"\n{'ID':<26} {'Nome':<15} {'Preço':>10} {'Lucro':>7} {'Categoria':<15} {'Qtd':>5}")
    print("-" * 80)
    for p in produtos:
        print(f"{str(p['_id']):<26} {p['nome']:<15} R${p['preco']:>8.2f} {p['lucro']:>6.1f}% {p['categoria']:<15} {p['quantidade']:>5}")
    print()

#  Adicionar produto
def adicionar_produto():
    print("\n── Novo Produto ──")
    nome = input("Nome: ").strip()
    preco = float(input("Preço: R$ "))
    lucro = float(input("Lucro (%): "))
    categoria = input("Categoria: ").strip()
    quantidade = int(input("Quantidade: "))

    col.insert_one({
        "nome": nome,
        "preco": preco,
        "lucro": lucro,
        "categoria": categoria,
        "quantidade": quantidade
    })
    print(f"Produto '{nome}' cadastrado com sucesso!\n")

# Aumentar lucro dos produtos 
def aumentar_lucro():
    print("\n── Aumentar Lucro ──")
    percentual = float(input("Digite o valor em percentagem do aumento do lucro: "))

    produtos = list(col.find())
    for p in produtos:
        novo_preco = round(p["preco"] * (1 + percentual / 100), 2)
        novo_lucro = round(p["lucro"] + percentual, 2)
        col.update_one({"_id": p["_id"]}, {"$set": {"preco": novo_preco, "lucro": novo_lucro}})

    print(f"Preços e lucros de todos os produtos aumentados em {percentual}%!\n")

# Apagar produto 
def apagar_produto():
    listar_produtos()
    from bson import ObjectId
    id_str = input("Digite o ID do produto a apagar: ").strip()
    try:
        resultado = col.delete_one({"_id": ObjectId(id_str)})
        if resultado.deleted_count:
            print("Produto removido com sucesso!\n")
        else:
            print("Produto não encontrado.\n")
    except Exception:
        print("ID inválido.\n")

# Menu principal 
def menu():
    while True:
        print("═══════════════════════════════")
        print("       GESTÃO DE PRODUTOS      ")
        print("═══════════════════════════════")
        print("1. Adicionar produto")
        print("2. Aumentar lucro dos produtos")
        print("3. Apagar produto")
        print("4. Sair")
        print("───────────────────────────────")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            aumentar_lucro()
        elif opcao == "3":
            apagar_produto()
        elif opcao == "4":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Ponto de entrada 
if __name__ == "__main__":
    inserir_iniciais()
    menu()
