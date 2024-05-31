import datetime
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

while True:

    opcao = input(menu)
    

    if opcao == "d":
        valor_desejado = float(input("Informe o valor que deseja depositar: "))

        if valor_desejado > 0:
            saldo += valor_desejado
            extrato += f"Depósito: R$ {valor_desejado:.2f}\n"

            print(saldo, extrato)

    elif opcao == "s":
        numero_saques += 0
        quantidade_saque = float(input("Informe o valor que deseja sacar: "))           
            
        if quantidade_saque > saldo:

            print('Saldo não disponível.')

        elif quantidade_saque > limite:
            print("Foi excedido o limite de saque")

        elif numero_saques > LIMITE_SAQUES:
            print("você excedeu o limite de saques diários!")
        
        elif quantidade_saque > 0:

            saldo -= quantidade_saque
            extrato += f"Saque: R$ {quantidade_saque: .2f}\n"
            numero_saques += 1

        else:
            print(" Falha na operação! Tente novamente")

    elif opcao == "e":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, por favor selecione novamente a operação desejada.")