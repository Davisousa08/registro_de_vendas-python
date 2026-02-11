
 # registrar vendas
 # registrar gastos
 # validar entrada
 # calcular resultado
 # exibir relatório
 # salvar dados
vendas = []

while True:
    entrada = input("Digite o valor da venda (ou 'finalizar'): ")

    if entrada == "finalizar":
        break

    vendas.append(float(entrada))

total = sum(vendas)
print("Total do dia:", total)
