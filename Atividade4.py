import os
os.system("cls")

#Função com parâmetros.
def tabudada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero *i}")

# Exemplo de uso da função.
numero = int(input("Digite um numero para tabuada: "))

# Chamando a função
# Enviando parâmetros
tabudada(numero)