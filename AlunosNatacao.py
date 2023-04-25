opcao = -1
listaNome = []
listaIdade = []
listaSexo = []
listaMensalidade = []

while opcao != 0:
    print('----- MENU -----')
    print('0 - Sair')
    print('1 - Cadastrar Aluno(a)')
    print('2 - Listar')
    print('3 - Percentual de alunos que pagam mensalidade > R$ 150,00 e < R$ 250,00')
    print('4 - Atualizar Mensalidade')
    print('5 - Média das mensalidades das mulheres < de 30 anos')
    print('6 - o valor da menor mensalidade paga por alunos (sexo masculino) '
          '  com idade maior que 65 anos ou com idade menor que 28 anos')
    print('7 - o nome da aluna (sexo feminino) que paga a maior mensalidade')
    print('8 - Faturamento ao final do mês')
    opcao = int(input('Digite a opção: '))
    if opcao == 0:
        print('Saindo...')

    elif opcao == 1:
        nome = input('Digite o nome: ')
        nomeJaExiste = False
        for i in range(len(listaNome)):
            if nome.upper() == listaNome[i].upper():
                nomeJaExiste = True
                break
        if nomeJaExiste == False:
            idade = int(input('Digite a idade: '))
            sexo = input('Digite o sexo f/m: ')
            mensalidade = float(input('Digite a mensalidade: '))
            listaNome.append(nome)
            listaIdade.append(idade)
            listaSexo.append(sexo)
            listaMensalidade.append(mensalidade)
        else:
            print('Nome já cadastrado!')

    elif opcao == 2:
        if len(listaNome) > 0:
            for i in range(len(listaNome)):
                print(' --- ALUNO #' + str(i+1) + ' ---')
                print('Nome: ' + listaNome[i])
                print('Idade : ' + str(listaIdade[i]))
                print('Sexo: ' + listaSexo[i])
                print('Mensalidade: ' + str(listaMensalidade[i]))
        else:
            print('Nenhum aluno cadastrado. *ERROR*')

    elif opcao == 3:
        if len(listaMensalidade) > 0:
            qtddEntre150e250 = 0
            for i in range(len(listaMensalidade)):
                if listaMensalidade[i] > 150 and listaMensalidade[i] < 250:
                    qtddEntre150e250 = qtddEntre150e250 + 1
            percentual = qtddEntre150e250/len(listaMensalidade)
            print('Percentual: ' + str(percentual*100))
        else:
            print('Cadastro se encontra vazio.')

    elif opcao == 4:
        if len(listaNome) > 0:
            nome = input('Digite o nome que deseja atualizar a mensalidade: ')
            attMensalidade = False
            for i in range(len(listaNome)):
                if nome.upper() == listaNome[i].upper():
                    novaMensalidade = float(input('Digite o novo valor da mensalidade: '))
                    listaMensalidade[i] = novaMensalidade
                    attMensalidade = True
                    break
            if attMensalidade == True:
                print('Atualizado com sucesso!')
            else:
                print('Cadastro não localizado!')
        else:
            print('Nenhum aluno cadastrado.')

    elif opcao == 5: #Média das mensalidades das mulheres < de 30 anos
        if len(listaSexo) > 0:
            qtdd = 0
            total = 0
            for i in range(len(listaSexo)):
                if listaSexo[i] == 'f' and listaIdade[i] <= 30:
                    qtdd = qtdd + 1
                    total = total + listaMensalidade[i]
            if qtdd > 0:
                valorMedio = total/qtdd
                print('Valor médio: ' + str(valorMedio))
            else:
                print('Não existe mulher nesse perfil.')
                print('Valor médio: 0.0')
        else:
            print('Nenhum cadastro localizado.')

    elif opcao == 6:
        if len(listaSexo) > 0:
            menorMensalidade = 999999
            for i in range(len(listaMensalidade)):
                if listaSexo[i] == 'm' and (listaIdade[i] < 28 or listaIdade[i] > 65):
                    if listaMensalidade[i] < menorMensalidade:
                        menorMensalidade = listaMensalidade[i]
            if menorMensalidade != 999999:
                print('O menor valor pago de mensalidade é: ' + str(menorMensalidade))
            else:
                print('Não há cadastros com o perfil dessa opção.')
        else:
            print('Nenhum cadastro localizado.')
    #o nome da aluna (sexo feminino) que paga a maior mensalidade
    elif opcao == 7:
        if len(listaSexo) > 0:
            maiorMensalidade = -1
            nomeMaiorMensalidade = ''
            for i in range(len(listaMensalidade)):
                if listaSexo[i] == 'f' and listaMensalidade[i] > maiorMensalidade:
                    maiorMensalidade = listaMensalidade[i]
                    nomeMaiorMensalidade = listaNome[i]
            if maiorMensalidade != -1:
                print('A aluna que paga a maior mensalidade é: ' + str(nomeMaiorMensalidade))
            else:
                print('Não há cadastros com o perfil dessa opção.')
        else:
            print('Nenhum cadastro localizado.')

    elif opcao == 8:
        if len(listaMensalidade) > 0:
            faturamentoTotal = 0
            for i in range(len(listaMensalidade)):
                faturamentoTotal = faturamentoTotal + listaMensalidade[i]
            print('Faturamento Total: ' + str(faturamentoTotal))
        else:
            print('Nenhum cadastro localizado.')
