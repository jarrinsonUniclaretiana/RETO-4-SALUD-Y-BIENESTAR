# Módulo para calcular el IMC

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)

print(f"Su IMC es: {resultado:.2f}")