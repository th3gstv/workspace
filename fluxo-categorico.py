fluxo_caixa = [
    {"tipo": "depósito", "valor": 1000.00, "categoria": "Salário"},
    {"tipo": "saque", "valor": 50.00, "categoria": "Alimentação"}
]

print("Fluxo de Caixa Categórico")
print("------------------------------")
print("[1] Depositar")
print("[2] Sacar")
print("[3] Mostrar Extrato")
print("[4] Sair")

banco = 950.00

while True:
    try:
        opcao = int(input("Selecione a opção desejada: "))

        if opcao == 1:
            valor = float(input("Digite o valor a depositar: R$"))
            categoria = input("Digite a categoria: ")
            fluxo_caixa.append({"tipo": "depósito", "valor": valor, "categoria": categoria})
            banco += valor
            print(f'Depósito de R${valor:.2f} na categoria {categoria} realizado com sucesso!\n')
            print(f'Saldo: R${banco:.2f}')

        elif opcao == 2:
            valor = float(input("Digite o valor do saque: R$"))
            categoria = input("Digite a categoria: ")
            if valor <= banco:
                fluxo_caixa.append({"tipo": "saque", "valor": valor, "categoria": categoria})
                banco = banco - valor
                print(f'Saque de R${valor:.2f} na categoria {categoria} realizado com sucesso!\n')
                print(f'Saldo: R${banco:.2f}')
            else:
                print('Saldo insuficiente para realizar o saque!\n')

        elif opcao == 3:
            for operacao in fluxo_caixa:
                tipo = operacao["tipo"]
                valor = operacao["valor"]
                categoria = operacao["categoria"]
                sinal = "+" if tipo == "depósito" else "-"
                print(f'[{sinal}] R${valor:.2f} - Categoria: {categoria}')

        elif opcao == 4:
            print(f'Até logo!')
            break
        else:
            print(f'Opção inválida!')
    except ValueError:
        print("Entrada inválida!")