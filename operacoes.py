#Funções para calculos

def soma (numeros):
    resultado = 0.0
    for i in numeros:
        resultado = resultado + float(i)
    print("O resultado da soma é: " , str(resultado))

def subtracao(numeros):
    resultado = 0.0
    for index,value in enumerate(numeros):
        if index == 0:
            resultado = float(value)
        else:
            resultado = resultado - float(value)
    print("O resultado da subtração é: " , str(resultado))

def multiplicacao(numeros):
    resultado = 0.0
    for index, value in enumerate(numeros):
        if index == 0:
            resultado = float(value)
        else:
            resultado = resultado * float(value)
    
    print("O resultado da multiplicação é: " , str(resultado))

def divisao(numeros):
    resultado = 0.0
    if '0' in numeros:
        print("Divisão por zero inválida!")
    else:
        for index, value in enumerate(numeros):
            if index == 0:
                resultado = float(value)
            else:
                resultado= resultado / float(value)
        print("O resultado da divisão é: " , str(resultado))
