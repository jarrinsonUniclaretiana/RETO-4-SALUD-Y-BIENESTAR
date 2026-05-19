# =========================
# MÓDULO A - CALCULAR IMC
# =========================
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# =========================
# MÓDULO B - CALCULAR TMB
# =========================
def calcular_tmb(peso, altura_cm, edad, sexo):
    if sexo.lower() == "h":
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura_cm) - (5.7 * edad)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura_cm) - (4.3 * edad)

    return tmb


# =====================================
# MÓDULO C - CLASIFICAR SEGÚN EL IMC
# =====================================
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


# =========================
# PROGRAMA PRINCIPAL
# =========================
print("===== SISTEMA DE SALUD =====")

nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (H/M): ")

# Llamar módulo IMC
imc = calcular_imc(peso, altura)

# Llamar módulo TMB
altura_cm = altura * 100
tmb = calcular_tmb(peso, altura_cm, edad, sexo)

# Llamar módulo clasificación
clasificacion = clasificar_imc(imc)

# Mostrar resultados
print("\n===== RESULTADOS =====")
print("Nombre:", nombre)
print(f"IMC: {imc:.2f}")
print("Clasificación:", clasificacion)
print(f"TMB: {tmb:.2f} calorías/día")