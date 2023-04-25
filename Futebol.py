resposta = 's'
jogador = 0
nome = ''
idade = 0
peso = 0.0
time = ''
nroJogadores = 0
jogadoresCorinthians = 0
mediaPeso = 0
idadeJogadoresCorinthians = 0
qtddJogadoresMenores20Anos = 0
mediaIdadeJogadoresCorinthians = 0
idadeMaisNovo = 80
nomeJogadorMaisNovo = ''
qtddJogadoresSantosComIdadeMaior20ouPesoMenorIgual65 = 0

while resposta == 's':
    print('Jogador #' + str(nroJogadores + 1))
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    time = input('Digite o time: ')
    nroJogadores = nroJogadores + 1
    resposta = input('Deseja continuar cadastrando? (s/n): ')
    #o percentual de jogadores que tem menos de 20 anos
    if idade < 20:
        qtddJogadoresMenores20Anos = qtddJogadoresMenores20Anos + 1

#o nome do jogador mais novo e com peso maior que 70 quilos.
if peso > 70 and idade < idadeMaisNovo:
    idadeMaisNovo = idade
    nomeJogadorMaisNovo = nome
    print('O nome do jogador mais novo, com peso > 70kg: ' + str(nomeJogadorMaisNovo))

#a quantidade de jogadores do “santos” com idade maior que 20 ou com peso menor ou igual a 65 quilos
if time == 'santos' and (idade > 20 or peso <= 65):
    qtddJogadoresSantosComIdadeMaior20ouPesoMenorIgual65 = qtddJogadoresSantosComIdadeMaior20ouPesoMenorIgual65 + 1
    print('Qtdd de jogadores do Santos com idade>20 ou peso<=65: ' + str(qtddJogadoresSantosComIdadeMaior20ouPesoMenorIgual65))
else:
    print('Não existe jogadores do santos com idade>20 ou peso<=65 cadastrados!')

#média de idade dos jogadores do “corinthians” com mais de 80 quilos.
if peso > 80 and time == 'corinthians':
    jogadoresCorinthians = jogadoresCorinthians + 1
    idadeJogadoresCorinthians = idadeJogadoresCorinthians + idade
    mediaIdadeJogadoresCorinthians = idadeJogadoresCorinthians/jogadoresCorinthians
    print('Idade média dos jogadores do corinthians com peso > 80kg: ' + str(mediaIdadeJogadoresCorinthians))
else:
    print('Não existe jogadores do Corinthians com mais de 80kg cadastrados!')

percentual = qtddJogadoresMenores20Anos/nroJogadores
print('Percentual de jogadores < 20 anos: ' + str(percentual))