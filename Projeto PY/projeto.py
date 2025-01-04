import json
import uuid

ARQUIVO_DADOS = "inventario.json"

# Carrega os dados do inventário
def carregar_dados():
    try:
        with open(ARQUIVO_DADOS, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Salva os dados do inventário
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

# Adicionar Produto
def adicionar_produto(inventario):
    nome = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade em Estoque: "))
    preco = float(input("Preço: "))
    produto = {
        "id": str(uuid.uuid4()),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
    }
    inventario.append(produto)
    salvar_dados(inventario)
    print("Produto adicionado com sucesso!")

# Listar Produtos
def listar_produtos(inventario):
    if not inventario:
        print("O inventário está vazio.")
        return
    print("\nInventário:")
    print(f"{'ID':<36} {'Nome':<20} {'Categoria':<15} {'Qtd':<8} {'Preço':<8}")
    for produto in inventario:
        print(
            f"{produto['id']:<36} {produto['nome']:<20} {produto['categoria']:<15} {produto['quantidade']:<8} R${produto['preco']:<8.2f}"
        )

# Atualizar Produto
def atualizar_produto(inventario):
    id_produto = input("Digite o ID do produto a ser atualizado: ")
    produto = next((p for p in inventario if p["id"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    
    print(f"Produto encontrado: {produto['nome']} (ID: {produto['id']})")
    print("Deixe o campo em branco para manter o valor atual.")

    nome = input(f"Novo Nome (atual: {produto['nome']}): ") or produto["nome"]
    categoria = input(f"Nova Categoria (atual: {produto['categoria']}): ") or produto["categoria"]
    quantidade = input(f"Nova Quantidade (atual: {produto['quantidade']}): ") or produto["quantidade"]
    preco = input(f"Novo Preço (atual: {produto['preco']}): ") or produto["preco"]

    produto.update({
        "nome": nome,
        "categoria": categoria,
        "quantidade": int(quantidade),
        "preco": float(preco),
    })
    salvar_dados(inventario)
    print("Produto atualizado com sucesso!")

# Excluir Produto
def excluir_produto(inventario):
    id_produto = input("Digite o ID do produto a ser excluído: ")
    produto = next((p for p in inventario if p["id"] == id_produto), None)
    if not produto:
        print("Produto não encontrado.")
        return
    
    confirmar = input(f"Tem certeza que deseja excluir o produto '{produto['nome']}'? (s/n): ")
    if confirmar.lower() == "s":
        inventario.remove(produto)
        salvar_dados(inventario)
        print("Produto excluído com sucesso!")
    else:
        print("Ação cancelada.")

# Buscar Produto
def buscar_produto(inventario):
    criterio = input("Buscar por (1) ID ou (2) Nome: ")
    if criterio == "1":
        id_produto = input("Digite o ID do produto: ")
        produto = next((p for p in inventario if p["id"] == id_produto), None)
    elif criterio == "2":
        nome_produto = input("Digite parte do nome do produto: ").lower()
        produto = next((p for p in inventario if nome_produto in p["nome"].lower()), None)
    else:
        print("Critério inválido.")
        return
    
    if produto:
        print(f"\nProduto encontrado:\n"
              f"ID: {produto['id']}\n"
              f"Nome: {produto['nome']}\n"
              f"Categoria: {produto['categoria']}\n"
              f"Quantidade: {produto['quantidade']}\n"
              f"Preço: R${produto['preco']:.2f}")
    else:
        print("Produto não encontrado.")

# Menu Principal
def menu():
    inventario = carregar_dados()
    while True:
        print("\n=== AgilStore - Gestão de Inventário ===")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(inventario)
        elif opcao == "2":
            listar_produtos(inventario)
        elif opcao == "3":
            atualizar_produto(inventario)
        elif opcao == "4":
            excluir_produto(inventario)
        elif opcao == "5":
            buscar_produto(inventario)
        elif opcao == "6":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia a aplicação
if __name__ == "__main__":
    menu()
