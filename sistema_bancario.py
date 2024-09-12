from datetime import datetime


def depositar(valor, saldo, extrato, num_transacoes):
    if valor > 0:
        saldo += valor
        data_formada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{data_formada}] Depósito: R$ {valor:.2f}\n"
        num_transacoes += 1
        print("Depósito realizado com sucesso.\n")
    else:
        print("Falha na operação! O valor informado é inválido.\n")
    return saldo, extrato, num_transacoes


def sacar(valor, saldo, extrato, num_saques, num_transacoes):
    if valor > saldo:
        print("Falha na operação! Você não tem saldo suficiente.\n")
    elif valor > LIMITE:
        print("Falha na operação! O valor do saque excede o limite.\n")
    elif valor > 0:
        saldo -= valor
        data_formada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{data_formada}] Saque: R$ {valor:.2f}\n"
        num_saques += 1
        num_transacoes += 1
        print("Saque realizado com sucesso.\n")
    else:
        print("Falha na operação! O valor informado é inválido.\n")
    return saldo, extrato, num_saques, num_transacoes


def exibir_extrato(saldo, extrato):
    print(" EXTRATO ".center(41, "="))
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("="*41)
    print()  

   
menu = """Insira o número da operação desejada.
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """


LIMITE = 500
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
saldo = 0
extrato = ""
num_saques = 0
num_transacoes = 0


while True:
    opcao = input(menu)
    print()
    
    if opcao == "1":
        if num_transacoes >= LIMITE_TRANSACOES:
            print("Falha na operação! Você excedeu o número de transações permitidas para hoje.\n")
        else:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, num_transacoes = depositar(valor, saldo, extrato, num_transacoes)
    
    elif opcao == "2":
        if num_saques >= LIMITE_SAQUES:
            print("Falha na operação! Número máximo de saques excedido.\n")
        elif num_transacoes >= LIMITE_TRANSACOES:
            print("Falha na operação! Você excedeu o número de transações permitidas para hoje.\n")
        else:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, num_saques, num_transacoes = sacar(valor, saldo, extrato, num_saques, num_transacoes)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
        
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida. Tente novamente.\n")