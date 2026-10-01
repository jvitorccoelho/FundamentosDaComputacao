# Inicialização das listas para armazenar os dados
listaRendas = []
listaDescricoesRendas = []
listaDescricoesGastos = []
listaValoresGastos = []
listaCategoriasGastos = []

opcaoMenu = 0

# Loop para manter o programa sempre aguardando um comando
while opcaoMenu != 6:
    print("\n" + "-"*30)
    print(" SISTEMA DE REGISTROS DE GASTOS")
    print("-"*30)
    print("1- Informar renda mensal")
    print("2- Cadastrar gasto")
    print("3- Consultar gastos")
    print("4- Consultar situação financeira")
    print("5- Ver estatísticas")
    print("6- Sair")
    
    # Captura da opção de escolha (menu: inteiro)
    opcaoMenu = int(input("\nEscolha uma opção: "))
    
    # Condicional match/case para o menu principal
    match opcaoMenu:
        case 1:
            # Captura da Renda (Descrição: string / Renda: float)
            descricaoRenda = input("Origem da renda: ")
            valorRendaInput = float(input("Informe o valor da renda: R$ "))
            # Registro da Renda nas listas
            listaDescricoesRendas.append(descricaoRenda)
            listaRendas.append(valorRendaInput)
            print("Renda cadastrada com sucesso!")
            
        case 2:
            # Captura do Gasto (Descrição: string / Gasto: float / Categoria: String)
            descricaoGasto = input("Descrição do gasto: ")
            valorGastoInput = float(input("Valor do gasto: R$ "))
            
            print("\nCategorias disponíveis:")
            print("1 - Alimentação")
            print("2 - Transporte")
            print("3 - Lazer")
            print("4 - Saúde")
            print("5 - Outros")
            opcaoCategoria = int(input("Escolha a categoria (1 a 5): "))
            
            # Estrutura if/else para definir a categoria
            categoriaGasto = ""
            if opcaoCategoria == 1:
                categoriaGasto = "Alimentação"
            elif opcaoCategoria == 2:
                categoriaGasto = "Transporte"
            elif opcaoCategoria == 3:
                categoriaGasto = "Lazer"
            elif opcaoCategoria == 4:
                categoriaGasto = "Saúde"
            else:
                categoriaGasto = "Outros"
                
            # Registro do Gasto nas listas
            listaDescricoesGastos.append(descricaoGasto)
            listaValoresGastos.append(valorGastoInput)
            listaCategoriasGastos.append(categoriaGasto)
            print("Gasto cadastrado com sucesso!")
            
        case 3:
            print("\n--- LISTA DE GASTOS ---")
            # Validando se a lista está vazia
            if len(listaValoresGastos) == 0:
                print("Nenhum gasto cadastrado até o momento.")
            else:
                # Laço para percorrer as listas referente aos gastos
                for i in range(len(listaValoresGastos)):
                    print(f"{i+1}º - {listaDescricoesGastos[i]} | {listaCategoriasGastos[i]} | R$ {listaValoresGastos[i]:.2f}")
                    
        case 4:
            # Percorrendo a lista de Rendas e Gastos para retornar os totais com laço FOR
            totalTotalRendas = 0.0
            for valorRenda in listaRendas:
                totalTotalRendas = totalTotalRendas + valorRenda
                
            valorTotalGastos = 0.0
            for valorGasto in listaValoresGastos:
                valorTotalGastos = valorTotalGastos + valorGasto
                
            saldoFinal = totalTotalRendas - valorTotalGastos
            
            print("\n--- SITUAÇÃO FINANCEIRA ---")
            print(f"Renda Total Mensal: R$ {totalTotalRendas:.2f}")
            print(f"Gastos Totais:      R$ {valorTotalGastos:.2f}")
            print(f"Saldo Final:        R$ {saldoFinal:.2f}")
            
            # Condicional para avaliar o status da conta
            if saldoFinal > 0:
                print("Situação: Você está no azul! Dentro do orçamento.")
            elif saldoFinal == 0:
                print("Situação: Saldo zerado. Atenção máxima!")
            else:
                print("Situação: Você está no vermelho! O orçamento foi ultrapassado.")
                
        case 5:
            print("\n--- ESTATÍSTICAS BÁSICAS ---")
            print(f"Quantidade de rendas registradas: {len(listaRendas)}")
            print(f"Quantidade de gastos registrados: {len(listaValoresGastos)}")
            
            if len(listaValoresGastos) > 0:
                # Loop para encontrar o maior gasto
                maiorGasto = listaValoresGastos[0]
                indiceMaior = 0
                
                for i in range(1, len(listaValoresGastos)):
                    if listaValoresGastos[i] > maiorGasto:
                        maiorGasto = listaValoresGastos[i]
                        indiceMaior = i
                        
                descricaoGastoMaior = listaDescricoesGastos[indiceMaior]
                print(f"Seu maior gasto foi com '{descricaoGastoMaior}' no valor de R$ {maiorGasto:.2f}.")
                
        case 6:
            print(f"Encerrando o programa...")
            
        case _:
            print("Opção inválida! Por favor, digite um número entre 1 e 6.")
