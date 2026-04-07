import os
os.system("cls")
#Função sem retorno.

def somar(n1, n2):
    soma = n1 + n2
    print(f"Soma: {soma}")

#Exemplo de uso da função
n1= int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

# Chamando a função
# Enviando parâmetros
somar(n1, n2)

