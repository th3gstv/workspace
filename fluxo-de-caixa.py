fluxo_caixa = []
total = 500
print('------- Fluxo de caixa -------')
print('______________________________')
print('1. Depositar')
print('2. Sacar')
print('3. Sair')

while True:
    try:
        opcao = int(input("Digite uma opcão: "))
        if opcao == 1:
            deposito = float(input("Selecione o valor que você deseja depositar: "))
            total += deposito
            print(f'Valor depositado com sucesso! \n Saldo total: R${total:.2f}')
        elif opcao == 2:
            saque = float(input("Selecione o valor que você deseja sacar: "))
            total = total - saque
            print(f'Saque de R${saque} realizado com sucesso! \n Saldo total: R${total:.2f}')
        elif opcao == 3:
            break
        else:
            print(f'Selecione uma opção válida!')
    except ValueError:
        print('Entrada inválida. Digite um número!')