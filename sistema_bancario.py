from datetime import date

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"[{date.today()}] Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.\n")
    else:
        print("Falha na operação! O valor informado é inválido.\n")
    return saldo, extrato
        
def sacar(valor, saldo, extrato, num_saques):
    if valor > saldo:
        print("Falha na operação! Você não tem saldo suficiente.\n")
    elif valor > LIMITE:
        print("Falha na operação! O valor do saque excede o limite.\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"[{date.today()}] Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("Saque realizado com sucesso.\n")
    else:
        print("Falha na operação! O valor informado é inválido.\n")
    return saldo, extrato, num_saques

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
saldo = 0
extrato = ""
num_saques = 0

while True:
    opcao = input(menu)
    print()
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)
    
    elif opcao == "2":
        if num_saques >= LIMITE_SAQUES:
            print("Falha na operação! Número máximo de saques excedido.\n")
        else:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, num_saques = sacar(valor, saldo, extrato, num_saques)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
        
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida. Tente novamente.\n")