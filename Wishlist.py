nomes = []
precos = []
prioridades = []
comprados = []
numeracoes = []

def adicionar():
    while True:
        try:
            nome = input("Digite o nome do jogo: ").title()
            preco = float(input("Digite o preco do jogo: "))
            prioridade = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
        except ValueError:
            print("Valor inválido, tente novamente")
            print()
            continue
        break
        
    if prioridade < 1 or prioridade > 3:
        print("Valor inválido, por favor, digite um número de 1 a 3.")
        print()
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
            if comprados[i] == True:
                sim_ou_nao_comprados = "Sim"
            else:
                sim_ou_nao_comprados = "Não"
            print(f"{numeracoes[i]} - Nome: {nomes[i]}" + f" | Preço:  R${precos[i]}" + f" | Prioridade:  {prioridades[i]}" + f" | Já foi comprado? {sim_ou_nao_comprados}")
    else:
        print("Lista vazia, tente adicionar um jogo primeiro!")

def atualizar():
    if nomes:
        while True:
            try:
                numeracao = int(input("Qual o item que deseja atualizar? "))
                nome2 = input("Digite o nome do jogo: ").title()
                preco2 = float(input("Digite o preco do jogo: "))
                prioridade2 = int(input("Qual a prioridade da compra? [1: Baixa / 2: Média / 3: Alta]: "))
                comprados2 = input("O item já foi comprado? [s/n]: ").strip().lower()
            except ValueError:
                print("Valor inválido, por favor, tente novamente.")
                print()
                continue
            break

        if prioridade2 < 1 or prioridade2 > 3:
            print("Valor inválido, por favor, digite um número de 1 a 3.")
            print()
            return adicionar()
            
        match prioridade2:
            case 1:
                prioridade2 = "Baixa"
            case 2:
                prioridade2 = "Média"
            case 3:
                prioridade2 = "Alta"
        if comprados2 not in ["s", "n"]:
            print("Valor inválido, por favor, digite 's' para sim ou 'n' para não.")
            print()
            return atualizar()

        for i in range(len(numeracoes)):
            if numeracoes[i] == numeracao:
                nomes[i] = nome2
                precos[i] = preco2
                prioridades[i] = prioridade2
                comprados[i] = comprados2 == "s"
                break
    else:
        print("Lista vazia, tente adicionar um jogo primeiro!")

def remover():
    if nomes:
        while True:
            try:
                numeracao = int(input("Qual o item que deseja remover? "))
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                print()
                continue
            break
        confirmacao = input(f"Tem certeza que deseja remover o item {numeracao}? [s/n]: ").strip().lower()
        if confirmacao not in ["s", "n"]:
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
    else:
        print("Lista vazia, tente adicionar um jogo primeiro!")

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
        try: 
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número de 0 a 5.")
            return main()
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
