#leia o preço de um produto e a forma de pagamento
#1)Se o pagamento for a vista será concedido desconto de 10%
#2)Se o pagamento for em até 3 parcelas o valor pago será o valor do produto dividido por 3
#3)Caso o usuário pague em 4 ou mais parcelas o valor final de cada parcela será o valor
#do produto com acréscimo de n% no qual n é o número de parcelas.
produtoPreco = float(input('Digite o preço do produto: '))
print('1 - Á vista')
print('2 - Parcelado')
formaPagamento = int(input('Escolha uma forma de pagamento: '))

if formaPagamento == 1:
    valorDescontado = produtoPreco*0.1
    novoValor = produtoPreco*0.9
    print('Valor original:     R$', produtoPreco)
    print('Desconto ganho:     R$', valorDescontado)
    print('Valor com desconto: R$', novoValor)
elif formaPagamento == 2:
    print('Parcelamos em até 3x sem juros.')
    qtddParcelas = int(input('Digite quantas parcelas deseja: '))
    if qtddParcelas == 1:
        print('Não é possível parcelar em 1x. Pague à vista!')
    elif qtddParcelas <= 3 and qtddParcelas != 1:
        valorParcelado = produtoPreco/qtddParcelas
        print('Valor original:  R$', produtoPreco)
        print('Valor parcelado: R$', valorParcelado)
    elif qtddParcelas >= 4:
        juros = qtddParcelas/100 * produtoPreco
        valorComJuros = produtoPreco + juros
        valorSerPago = valorComJuros/qtddParcelas
        print('Valor original:               R$', produtoPreco)
        print('Valor com juros:              R$', valorComJuros)
        print('Valor parcelado com os juros: R$', valorSerPago)