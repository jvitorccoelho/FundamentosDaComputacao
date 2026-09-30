valorRenda = float(input("Informe seu rendimento total para o período de avaliação: \n"))

periodo = int(input("Informe quantos gastos você deseja efetuar: \n"))
valorTotalGastos = float(0)

for i in range(1, periodo+1):
    valorGasto = float(input("Informe o valor do %iº gasto\n" % i))
    valorTotalGastos = valorTotalGastos + valorGasto
    print("Informado o valor %.2f. Total de gastos: %.2f\n" % (valorGasto, valorTotalGastos))

valorSaldo = valorRenda - valorTotalGastos

print("Seu rendimento total foi: %.2f. \n Seus gastos totalizaram: %.2f\n Seu saldo final é: %.2f" % (valorRenda, valorTotalGastos, valorSaldo))





""" valorTotalRenda = =
mes = 1
while (mes != 12):
    valorTotalRenda =+ input("Informe a renda do mes %i",mes)
    valorTotalGasto =+ input("Informe o gasto do mes %i", mes)
    mes =+ 1

# Definição de "Input de Gastos"
descricaoGasto = str(input("Descrição do gasto: "))
valorGasto = float(input("Valor do gasto: "))

# Definição de "Informe de renda mensal"
mesReferenciaRenda = int(input("Informe o mês de referência: "))
valorRendaMes = float(input("Informe o valor recebido no mês: "))
descricaoRenda = str(input("Qual a origem do valor recebido: "))

# Armazenamento acumulado
valorTotalGastos = float(0) #declaração inicial
valorTotalGastos += valorGasto
valorTotalRenda = float(0)
valorTotalRenda += valorRendaMes
valorSaldo = valorTotalRenda - valorTotalGastos
varSituacaoFinanceira = if valorSaldo >= 0:
    "Superávit"
else
    "Déficit" """
