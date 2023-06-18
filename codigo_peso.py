def converte_gramas(peso):
   return peso*1000 

peso= (float(input("Insira o peso em kilos: ")))
peso_gramas = converte_gramas(peso)
print ("o peso final do usuário em gramas é: ", peso_gramas)