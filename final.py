# modulo_clasificacion.py

def clasificar_imc(imc):

    if imc < 18.5:
        return "Bajo peso"

    elif imc < 25:
        return "Peso normal"

    elif imc < 30:
        return "Sobrepeso"

    else:
        return "Obesidad"


# Programa principal
imc = float(input("Ingrese su IMC: "))

clasificacion = clasificar_imc(imc)

print("Clasificación:", clasificacion)