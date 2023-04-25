#Calculo de ano bissexto ou não.
ano = int(input('Digite o Ano para verificar se é ou não Bissexto: '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(str(ano) + ' é bissexto')
else:
    print(str(ano) + ' não é bissexto')