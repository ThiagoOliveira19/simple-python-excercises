def calcular_restante_salario(salario, conta1, conta2):
    multa = 0.02  # 2% de multa

    valor_total_contas = conta1 + conta2
    valor_multa = valor_total_contas * multa
    valor_pagar = valor_total_contas + valor_multa

    restante_salario = salario - valor_pagar

    return restante_salario

salario = float(input("Digite o salário de João: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))

restante = calcular_restante_salario(salario, conta1, conta2)

print("Restante do salário de João: R$", restante)
