def depositar(saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("VALOR DE DEPÓSITO INVÁLIDO")
        return saldo, extrato
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("SALDO INSUFICIENTE.")
    elif valor > limite:
        print("VALOR DE SAQUE EXCEDE O LIMITE")
    elif numero_saques >= limite_saques:
        print("NÚMERO DE SAQUES EXCEDIDO...")
        print("Tente novamente amanhã")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("VALOR DE SAQUE INVÁLIDO")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO DA CONTA ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (apenas números): ")
    

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Tente novamente.")
        return
    

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
            return

    endereco = input("Digite o endereço no formato: logradouro, nro - bairro - cidade/sigla estado: ")
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")


def criar_conta(contas, usuarios):
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado. Cadastre um usuário antes de criar uma conta.")
        return
    
    numero_conta = len(contas) + 1
    
    agencia = "0001"
    

    print("Usuários disponíveis:")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario['nome']} (CPF: {usuario['cpf']})")

    try:
        usuario_index = int(input("Selecione o número do usuário para vincular a conta: ")) - 1
        if usuario_index < 0 or usuario_index >= len(usuarios):
            print("Usuário inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return


    usuario_selecionado = usuarios[usuario_index]
    

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_selecionado
    }

    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}, Usuário: {usuario_selecionado['nome']}")

def listar_contas(contas):
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\nLista de contas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")
    print()

def main():

    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova conta
    [l] Listar contas
    [u] Novo usúario
    [q] Sair

    => """
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    

    while True:

        comando = input(menu)
        if comando == "d":
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif comando == "s":
            valor = float(input("Informe o valor de saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif comando == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif comando == "u":
            criar_usuario(usuarios)
        
        elif comando == 'n':
            criar_conta(contas, usuarios)

        elif comando == 'l':
            listar_contas(contas)

        elif comando == "q":
            print("OPERAÇÃO ENCERRADA.")
            break

        else:
            print("OPÇÃO INVÁLIDA, POR FAVOR SELECIONE UMA OPÇÃO VÁLIDA.")

main()
