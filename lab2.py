menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
x = 0

while True:

    comando = input(menu)
    if comando == "d":
        x = float(input("Informe o valor do depósito: "))
        if x > 0:
            saldo += x
            extrato += f"Depósito: R$ {x:.2f}\n"
        else:
            print("VALOR DE DEPÓSITO INVÁLIDO")

    elif comando == "s":
        x = float(input("Informe o valor do saque: "))
        if x > saldo:
            print("SALDO INSUFICIENTE.")
        elif x > limite:
            print("VALOR DE SAQUE EXCEDE O LIMITE")
        elif numero_saques >= LIMITE_SAQUES:
            print("NÚMERO DE SAQUES EXCEDIDO...")
            print("Tente novamente amanhã")
        elif x > 0:
            saldo -= x
            extrato += f"Saque: R$ {x:.2f}\n"
            numero_saques += 1
        else:
            print("VALOR DE SAQUE INVÁLIDO")

    elif comando == "e":
        print("\n================ EXTRATO DA CONTA ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif comando == "q":
        print("OPERAÇÃO ENCERRADA.")
        break

    else:
        print("OPÇÃO INVÁLIDA, POR FAVOR SELECIONE UMA OPÇÃO VÁLIDA.")
