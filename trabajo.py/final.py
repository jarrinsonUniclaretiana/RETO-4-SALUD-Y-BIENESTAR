# Módulo para calcular la TMB

def calcular_tmb(peso, altura, edad, sexo):
    if sexo.lower() == "h":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)
    
    return tmb

# Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en cm: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (H/M): ")

resultado = calcular_tmb(peso, altura, edad, sexo)

print(f"Su TMB es: {resultado:.2f} calorías/día")