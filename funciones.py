

#1
texto_caracter = input("Ingrese un texto: ")
print(texto_caracter)
print("Cantidad de caracteres: ",len(texto_caracter))

#2
texto = input("Ingrese un texto: ")
b = texto.count(" ")
c = len(texto)

def espacios(b, c):
    return c - b
print(espacios(b,c))

#3

def calculo(num1, num2):
    operador = input("Ingrese un operador: ")
    if operador == "+":
        resultado = int(num1) + int(num2)
    if operador == "-":
        resultado = int(num1) - int(num2)
    if operador == "*":
        resultado = int(num1) * int(num2)
    if operador == "/":
        resultado = int(num1) / int(num2)
    return resultado 

num1 = input("Ingrese un número: ")  
num2 = input("Ingrese otro número: ")     
print(calculo(num1, num2))                                                                    


