nomes = []
precos = []
prioridades = []
comprados = []

def adicionar():
    # FIXME: colocar validação
    nome = input("Digite o nome do jogo: ")
    preco = float(input("Digite o preco do jogo: "))
    prioridade = (input("Qual a prioridade da compra? [Baixa / Média / Alta] ")) .strip()

    nomes.append(nome)
    precos.append(preco)
    prioridades.append(prioridade)
    comprados.append(False)


def listar():
    if nomes: 
        for i in range(len(nomes)):
            print(f"Nome: {nomes[i]}" + f" - Preço:  {precos[i]}" + f" - Prioridade:  {prioridade[i]}")




def menu():
    print("=" * 20)
    print("Lista de desejos")
    print()
    print("1. Adicionar item")
    print("2. Ver lista")
    print("3. Remover item")
    print("4. Limpar lista")
    print("5. atualizar lista")
    print("0. Sair")
    print("=" * 20)


def main():
    while True:
        menu()

        # TODO: colocar validação de entrada
        op = int(input("Escolha uma opção: "))
        if op < 0 or op > 4:
            print("Opção inválida. Tente novamente.")

        match op:
            case 1:
                adicionar()

            case 2:
              listar()
                
            case 3:
                pass 

            case 4:
                confirmaçao_4 = input(
                    "Deseja limpar a lista? (s/n): ").lower() .strip()
                if confirmaçao_4 == "s":
                    print("Lista limpa com sucesso!")
                else:
                    print("Limpeza cancelada.")

                if jogos:
                    jogos.clear()
                    print("Lista limpa com sucesso!")
                else:
                    print("A lista de desejos já está vazia.")

            case 0:
                while True:
                    print("Saindo...")
                    break


if __name__ == "__main__":
    main()
