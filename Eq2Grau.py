#Calcular as raizes reais de uma equação do segundo grau
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

delta = (b**2 - 4*a*c)
if delta > 0:
    print('Existe 2 raizes reais.')
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print('x1: ' + str(x1))
    print('x2: ' + str(x2))
elif delta == 0:
    print('Existe 1 raiz real.')
    x = (-b / (2 * a))
    print('x: ' + str(x))
elif delta < 0:
    print('Não existe raiz.')
