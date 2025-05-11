nome = input("Digite o seu nome: ")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

print(f'Olá {nome}, o seu IMC é {imc:.2f}')

if imc <= 18.5:
    print('Resultado: Magreza')
elif 18.5 < imc < 24.9:
    print('Resultado: Peso normal')
elif 25 <= imc < 29.9:
    print('Resultado: Sobrepeso')
else:
    print('Resultado: Obesidade')