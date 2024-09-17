class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    LIMITE_SAQUES = 3
    LIMITE = 500

    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("VALOR DE DEPÓSITO INVÁLIDO")

    def sacar(self, valor):
        if valor > self.saldo:
            print("SALDO INSUFICIENTE.")
        elif valor > ContaBancaria.LIMITE:
            print("VALOR DE SAQUE EXCEDE O LIMITE")
        elif self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            print("NÚMERO DE SAQUES EXCEDIDO... Tente novamente amanhã")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("VALOR DE SAQUE INVÁLIDO")

    def exibir_extrato(self):
        print(f"\n================ EXTRATO DA CONTA {self.numero_conta} =================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==============================================")


# Funções para criar usuários e contas
def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF (apenas números): ")

    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Tente novamente.")
        return

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
            return

    endereco = input("Digite o endereço no formato: logradouro, nro - bairro - cidade/sigla estado: ")
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
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
        print(f"{i + 1}. {usuario.nome} (CPF: {usuario.cpf})")

    try:
        usuario_index = int(input("Selecione o número do usuário para vincular a conta: ")) - 1
        if usuario_index < 0 or usuario_index >= len(usuarios):
            print("Usuário inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    usuario_selecionado = usuarios[usuario_index]
    nova_conta = ContaBancaria(agencia, numero_conta, usuario_selecionado)
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}, Usuário: {usuario_selecionado.nome}")

def listar_contas(contas):
    if len(contas) == 0:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\nLista de contas:")
    for conta in contas:
        print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero_conta}, Usuário: {conta.usuario.nome}")
    print()

def selecionar_conta(contas):
    listar_contas(contas)
    if len(contas) == 0:
        return None

    try:
        conta_index = int(input("Selecione o número da conta que deseja acessar: ")) - 1
        if conta_index < 0 or conta_index >= len(contas):
            print("Conta inválida.")
            return None
        return contas[conta_index]
    except ValueError:
        print("Entrada inválida.")
        return None


# Simulação do sistema bancário
def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova conta
    [l] Listar contas
    [u] Novo usuário
    [q] Sair
    => """
    
    usuarios = []
    contas = []
    
    while True:
        comando = input(menu)
        if comando == "d":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor de depósito: "))
                conta.depositar(valor)
        
        elif comando == "s":
            conta = selecionar_conta(contas)
            if conta:
                valor = float(input("Informe o valor de saque: "))
                conta.sacar(valor)
        
        elif comando == "e":
            conta = selecionar_conta(contas)
            if conta:
                conta.exibir_extrato()
        
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

if __name__ == "__main__":
    main()
