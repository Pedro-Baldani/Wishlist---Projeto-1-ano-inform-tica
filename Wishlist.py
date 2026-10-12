nomes = []
precos = []
prioridades = []
comprados = []
numeracao = []

def adicionar():
    # FIXME: colocar validação
    nome = input("Digite o nome do jogo: ") .title()
    preco = float(input("Digite o preco do jogo: "))
    prioridade = (input("Qual a prioridade da compra? [Baixa / Média / Alta] ")) .title() .strip()

    nomes.append(nome)
    precos.append(preco)
    prioridades.append(prioridade)
    comprados.append(False)
    for i in range(len(nomes)):
        numeracao.append(i + 1) #conserta félix


def listar():
    if nomes: 
        for i in range(len(nomes)):
            print(f"{numeracao[i]} - Nome: {nomes[i]}" + f" - Preço:  {precos[i]}" + f" - Prioridade:  {prioridades[i]}" + f" - Já foi comprado? {comprados[i]}")

def atualizar():
    numeracao = print(input("Qual o item que deseja atualizar? "))
    nome = input("Digite o nome do jogo: ") .title()
    preco = float(input("Digite o preco do jogo: "))
    prioridade = (input("Qual a prioridade da compra? [Baixa / Média / Alta] ")) .title() .strip()

    nomes.append(nome)
    precos.append(preco)
    prioridades.append(prioridade)
    comprados.append(False)

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
                pass

            case 5:
                pass
            
            case 0:
                sair()
            
if __name__ == "__main__":
    main()
