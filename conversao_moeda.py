def converter_para_dolar(dinheiro):
    cotacao_dolar = 1.80
    dinheiro_dolar = dinheiro / cotacao_dolar
    return dinheiro_dolar

def converter_para_marco(dinheiro):
    cotacao_marco = 2.00
    dinheiro_marco = dinheiro / cotacao_marco
    return dinheiro_marco

def converter_para_libra(dinheiro):
    cotacao_libra = 1.57
    dinheiro_libra = dinheiro / cotacao_libra
    return dinheiro_libra

dinheiro_reais = float(input("Digite a quantidade de dinheiro em reais: "))

dinheiro_dolar = converter_para_dolar(dinheiro_reais)
dinheiro_marco = converter_para_marco(dinheiro_reais)
dinheiro_libra = converter_para_libra(dinheiro_reais)

print("Valor em dólares: US$", dinheiro_dolar)
print("Valor em marco alemão: DM", dinheiro_marco)
print("Valor em libra esterlina: £", dinheiro_libra)