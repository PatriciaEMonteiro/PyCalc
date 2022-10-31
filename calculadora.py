print("\n CALCULADORA \n\n")

resultado = 0.0
print("Qual Operação deseja Realizar?")
operacao = input(" + Soma; - Subtração; * Multiplicação; / Divisão ")

def recebeDados ():
    print("\nQuais números deseja calcular?")
    numeros_lista = input("Informe os numeros a serem somados: (Separados por virgula) ")
    return numeros_lista.split(",")

if operacao == '+' :
    numeros = recebeDados()

    for i in numeros:
        resultado = resultado + float(i)
    
    print("O resultado da soma é: " , str(resultado))

elif operacao == '-' :
    numeros = recebeDados()

    for index,value in enumerate(numeros):
        if index == 0:
            resultado = float(value)
        else:
            resultado = resultado - float(value)
    
    print("O resultado da subtração é: " , str(resultado))

elif operacao == '*' :
    numeros = recebeDados()

    for index, value in enumerate(numeros):
        if index == 0:
            resultado= float(value)
        else:
            resultado = resultado * float(value)
    
    print("O resultado da multiplicação é: " , str(resultado))

elif operacao == '/':
    numeros = recebeDados()

    if '0' in numeros:
        print("Divisão por zero inválida!")
    else:
        for i in numeros:
            resultado= resultado / float(i)
    
        print("O resultado da divisão é: " , str(resultado))

else:
    print("Error!")
