vendas = [
    {"id": 1, "cliente": "Ana", "valor": 120.50, "pagamento": "pix", "status": "aprovado"},
    {"id": 2, "cliente": "João", "valor": 89.90, "pagamento": "cartao", "status": "aprovado"},
    {"id": 3, "cliente": "Ana", "valor": 42.00, "pagamento": "dinheiro", "status": "cancelado"},
    {"id": 4, "cliente": "Carlos", "valor": 310.00, "pagamento": "cartao", "status": "aprovado"},
    {"id": 5, "cliente": "João", "valor": 55.00, "pagamento": "pix", "status": "aprovado"},
    {"id": 6, "cliente": "Ana", "valor": 75.50, "pagamento": "pix", "status": "aprovado"},
]


maior_valor = vendas[0]
for venda in vendas:
    if venda["valor"] > maior_valor["valor"]:
        maior_valor = venda

print (maior_valor["valor"])