#Um motorista de de taxi deseja calcular o rendimento de seu carro. Sabendo-se que o preço do combustível é de R$2,50
odo = int(input('Digite o numero marcado no odometro no inicio do dia: '))
odof = int(input('Digite o numero marcado no odometro no final do dia: '))
gas = int(input('Digite quantos litros foram gastos de gasolina: '))
granaPassageiros = float(input('Digite quantos reais ganhos pelos passageiros ao final do dia: '))

kmGastos = odof - odo
consumoGas = kmGastos/gas
print('O carro fez ' + str(consumoGas) + 'Km/L')

calculoGas = gas*2.5
lucro = granaPassageiros - calculoGas

if lucro <= 100:
    print('Voce precisa melhorar seu desempenho quanto aos passageiros!')
else:
    print('Voce esta tendo um otimo desempenho, com um lucro de ' + str(lucro) + 'reais.')