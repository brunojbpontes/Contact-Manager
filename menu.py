contatos = []
numeros = []
quantidade_contatos = 0

def adicionarContatos():
    global quantidade_contatos
    while True:
        nome = input("Digite o nome do contato a ser adicionado: ")
        numero = input("Digite o número dessa pessoa: ")
        contatos.append(nome)
        numeros.append(numero)
        quantidade_contatos += 1
        resposta = input("Deseja adicionar outro contato? (sim/não): ")
        if resposta != 'sim':
            break

def listarContatos():
    if quantidade_contatos == 0:
        print("Nenhum contato adicionado.")
    else:
        for i in range(quantidade_contatos):
            print(f"Pessoa {i + 1}:\nNome: {contatos[i]}\nNúmero: {numeros[i]}")

def removerContatos():
    global quantidade_contatos
    if quantidade_contatos == 0:
        print("Nenhum contato para remover.")
        return
    listarContatos()
    try:
        index = int(input("Digite o número da pessoa a ser removida (começando de 1): ")) - 1
        if 0 <= index < quantidade_contatos:
            del contatos[index]
            del numeros[index]
            quantidade_contatos -= 1
            print("Contato removido com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def editarContatos():
    if quantidade_contatos == 0:
        print("Nenhum contato para editar.")
        return
    listarContatos()
    try:
        index = int(input("Digite o número do contato que deseja editar (começando de 1): ")) - 1
        if 0 <= index < quantidade_contatos:
            novo_nome = input("Digite o novo nome do contato: ")
            novo_numero = input("Digite o novo número desse contato: ")
            contatos[index] = novo_nome
            numeros[index] = novo_numero
            print("Contato editado com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

while True:
    print("\n'GERENCIADOR DE CONTATOS'\n")
    print("1. Adicionar Contatos")
    print("2. Listar Contatos")
    print("3. Deletar Contatos")
    print("4. Editar Contatos")
    print("5. Sair")
    try:
        opcao = int(input("Opção: "))
        if opcao == 1:
            adicionarContatos()
        elif opcao == 2:
            listarContatos()
        elif opcao == 3:
            removerContatos()
        elif opcao == 4:
            editarContatos()
        elif opcao == 5:
            break
        else:
            print("Opção inválida. Por favor, escolha um número entre 1 e 5.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
