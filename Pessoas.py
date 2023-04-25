#programa que recebe a idade, peso e altura de N pessoas
#A média das idades das N pessoas;
#A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 m
#A porcentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m
n = int(input('Digite quantas pessoas deseja cadastrar: '))
y = 0  #quantidade de pessoas acima de 90kg e menores que 150cm
z = 0  #quantidade de pessoas entre 10 a 30 anos e acima de 190cm
idadesCadastradas = 0  #quantidade de idades cadastradas
for i in range(n):
    idade = int(input('Digite a idade: '))
    idadesCadastradas = idadesCadastradas + idade
    peso = float(input('Digite o peso: '))
    altura = int(input('Digite a altura: '))
    if peso >= 90 and altura <= 150:
        y = y + 1
    elif idade >= 10 and idade <= 30 and altura >= 190:
        z = z + 1
    print('~'*20)

media = idadesCadastradas/n
porcentagem = (z * 100)//n

print('A média das idades cadastradas é: ' + str(media))
print('A porcentagem de pessoas entre 10 a 30 anos, maiores que 1.90m é: ' + str(porcentagem) + '%')
print('Tem-se ' + str(y) + ' pessoa(s) acima de 90kg e abaixo de 1.50m')
