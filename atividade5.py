import os
os.system("cls")

def informacao(numero):
    if numero < 0:
        print("Número Negativo")
    else:
        print("Número Positivo")

numero = int(input("Digite um número: "))
informacao(numero)
