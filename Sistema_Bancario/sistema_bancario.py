saldo = 0.0

nome = input("Digite seu nome:")

print(nome.title())

def deposito():
    global saldo
    valor = float(input("Digite o valor de depósito:"))
    if valor > 0:
        saldo += valor
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso")
    else:
        print("O valor de depósito deve ser positivo!")

def saque():
    global saldo
    saque = float(input("Digite o valor de saque:"))
    if saque > 0:
        saldo -= saque
    else:
        print("O valor de saque deve ser positivo")
    
def menu():
    while True:
        print("Menu interativo")
        print("1. Ver saldo")
        print("2. Depósito")
        print("3. Saque")
        print("4. Sair")

        opcao = input("\nEscolha uma das opções acima:")

        if opcao == '1':
            print(f"O saldo atual da conta é de: R$ {saldo}")
        elif opcao == '2':
            deposito()
        elif opcao == '3':
            saque()
        elif opcao == '4':
            print("Saindo do sistema! \n")
            break


menu()
            


        

    