nomes = []
precos = []
prioridades = []
comprados = []
numeracoes = []

def adicionar():
    # FIXME: colocar validação
    nome = input("Digite o nome do jogo: ").title()
    preco = float(input("Digite o preco do jogo: "))
    prioridade = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
    if prioridade < 1 or prioridade > 3:
        print("Valor inválido, tente novamente")
        return adicionar()
    match prioridade:
        case 1:
            prioridade = "Baixa"
        case 2:
            prioridade = "Média"
        case 3:
            prioridade = "Alta"

    nomes.append(nome)
    precos.append(preco)
    prioridades.append(prioridade)
    comprados.append(False)
    numeracoes.append(len(nomes))
    print("Jogo adicionado com sucesso!")

def listar():
    if nomes: 
        for i in range(len(nomes)):
            print(f"{numeracoes[i]} - Nome: {nomes[i]}" + f" | Preço:  R${precos[i]}" + f" | Prioridade:  {prioridades[i]}" + f" | Já foi comprado? {comprados[i]}")
    else:
        print("Lista vazia, tente novamente.")

def atualizar():
    numeracao = int(input("Qual o item que deseja atualizar? "))
    nome2 = input("Digite o nome do jogo: ").title()
    preco2 = float(input("Digite o preco do jogo: "))
    prioridade2 = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
    comprados2 = input("O item já foi comprado? [s/n]: ").strip().lower()
    if prioridade2 < 1 or prioridade2 > 3:
        print("Valor inválido, tente novamente")
        return adicionar()
        
    match prioridade2:
        case 1:
            prioridade2 = "Baixa"
        case 2:
            prioridade2 = "Média"
        case 3:
            prioridade2 = "Alta"

    for i in range(len(numeracoes)):
        if numeracoes[i] == numeracao:
            nomes[i] = nome2
            precos[i] = preco2
            prioridades[i] = prioridade2
            comprados[i] = comprados2 == "s"
            break

def remover():
    numeracao = int(input("Qual o item que deseja remover? ")) 
    confirmacao = input(f"Tem certeza que deseja remover o item {numeracao}? [s/n]: ").strip().lower()
    if confirmacao == "n":
        print("Operação cancelada.")
        return remover()
    else:
        for i in range(len(numeracoes)):
            if numeracoes[i] == numeracao:
                nomes.remove(nomes[i])
                precos.remove(precos[i])
                prioridades.remove(prioridades[i])
                comprados.remove(comprados[i])
                numeracoes.remove(numeracoes[i])
                break
    print("Item removido com sucesso!")


def sair():
    while True:
        print("Saindo...")
        break

def menu():
    print("=" * 20)
    print("Lista de desejos")
    print()
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Atualizar lista")
    print("4. Remover item")
    print("5. Limpar lista")
    print("0. Sair")
    print("=" * 20)


def main():
    while True:
         menu()

         # TODO: colocar validação de entrada
         op = int(input("Escolha uma opção: "))
         if op < 0 or op > 5:
              print("Opção inválida. Tente novamente.")

         match op:
            case 1:
                adicionar()

            case 2:
                listar()
                    
            case 3:
                atualizar()

            case 4:
                remover()

            case 5:
                pass
            
            case 0:
                sair()
            
if __name__ == "__main__":
    main()
