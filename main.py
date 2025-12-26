import json

def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)

def cadastrar_produto(estoque):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    estoque.append(produto)
    salvar_estoque(estoque)
    print("✅ Produto cadastrado com sucesso!")

def listar_produtos(estoque):
    if not estoque:
        print("Estoque vazio.")
        return

    for i, p in enumerate(estoque):
        print(f"{i} - {p['nome']} | Qtde: {p['quantidade']} | R$ {p['preco']:.2f}")

def remover_produto(estoque):
    listar_produtos(estoque)
    indice = int(input("Digite o índice do produto a remover: "))
    estoque.pop(indice)
    salvar_estoque(estoque)
    print("🗑 Produto removido!")

def valor_total(estoque):
    total = sum(p["quantidade"] * p["preco"] for p in estoque)
    print(f"💰 Valor total do estoque: R$ {total:.2f}")

def menu():
    estoque = carregar_estoque()

    while True:
        print("\n--- CONTROLE DE ESTOQUE ---")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Remover produto")
        print("4 - Valor total do estoque")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            valor_total(estoque)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida")

menu()

