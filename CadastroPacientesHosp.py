sexo = ''
peso = 0.0
nroPaciente = 0
resposta = 's'
idadeMaisVelhoComPesoMaior50 = 0
pacienteMaisVelhoComPesoMaior50 = ''
qtddMulheresMaior30Anos = 0
somaPeso = 0
qtddHomemOuIdadeMenor45Anos = 0
qtddIdosos = 0

while resposta == 's':
    print('Paciente #' + str(nroPaciente + 1))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (F/M): ')
    peso = float(input('Digite o peso: '))
    nroPaciente = nroPaciente + 1
    resposta = input('Deseja continuar cadastrando? (s/n): ')
    #o nome do paciente mais velho e com peso maior que 50 quilos.
    if peso > 50 and idade > idadeMaisVelhoComPesoMaior50:
        pacienteMaisVelhoComPesoMaior50 = nome
        idadeMaisVelhoComPesoMaior50 = idade

    #peso médio dos pacientes do sexo feminino com mais de 30 anos.
    if sexo == 'f' and idade > 30:
         qtddMulheresMaior30Anos = qtddMulheresMaior30Anos + 1
         somaPeso = somaPeso + peso
    #a quantidade de pacientes do sexo masculino ou com idade menor que 45 anos.
    if sexo == 'm' or idade < 45:
        qtddHomemOuIdadeMenor45Anos = qtddHomemOuIdadeMenor45Anos + 1

    #o percentual de pacientes (masculino ou feminino) que são idosos (mais de 59 anos).
    if idade > 59:
        qtddIdosos = qtddIdosos + 1

print('Nome do paciente mais velho com mais de 50kg: ' + pacienteMaisVelhoComPesoMaior50)

if qtddMulheresMaior30Anos > 0:
    pesoMedio = somaPeso/qtddMulheresMaior30Anos
    print('Peso médio de mulheres com mais de 30 anos: ' + str(pesoMedio))
else:
    print('Não existe mulheres com mais de 30 anos!')

print('Quantidade de homens ou idade maior que 45: ' + str(qtddHomemOuIdadeMenor45Anos))

percentual = qtddIdosos/nroPaciente
print('Percentual de idosos: ' + str(percentual))
