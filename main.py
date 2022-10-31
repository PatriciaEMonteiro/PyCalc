print("\n CALCULADORA \n\n")

from operacoes import soma, subtracao, multiplicacao, divisao

resultado = 0.0

print("Qual Operação deseja Realizar?")
operacao = input(" + Soma; - Subtração; * Multiplicação; / Divisão ")

#Função para receber numeros listados pelo usuario
def recebeDados ():
    print("\nQuais números deseja calcular?")
    numeros_lista = input("Informe os numeros a serem somados: (Separados por virgula) ")
    return numeros_lista.split(",")

# Chamada das funções
if operacao == '+' :
    numeros = recebeDados()
    soma(numeros)

elif operacao == '-' :
    numeros = recebeDados()
    subtracao(numeros)

elif operacao == '*' :
    numeros = recebeDados()
    multiplicacao(numeros)

elif operacao == '/':
    numeros = recebeDados()
    divisao(numeros)

else:
    print("Error!")
