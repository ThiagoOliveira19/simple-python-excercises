def porcento (preco_original):
    novo_preco = preco_original *0.9
    return novo_preco

n1 = float(input("digite o valor do produto sem desconto"))

novo_preco = porcento(n1)
print ("o produto com de desconto resulta em um valor de: ", novo_preco)