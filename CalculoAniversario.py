diaNiver = int(input('Digite o dia do seu aniversario: '))
mesNiver = int(input('Digite o mes do seu aniversario: '))
print('Digite a data de hoje.')
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))

x = mesNiver - mes
y = diaNiver - dia
total = x*30 + y
if total > 1:
    print('Faltam ' + str(total) + ' dia(s) para o seu aniversario!')
elif total == 0:
    print('Hoje é o seu aniversario, parabens! O proximo é daqui ' + str(-total + 360)+ ' dias.')
else:
    print('Já se passaram ' + str((-total)) + ' dia(s) do seu aniversario. O proximo é daqui ' + str(-total + 360)+ ' dias.')