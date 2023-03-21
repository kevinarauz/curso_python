ARS = 202.91
COL = 4849.99
MEX = 18.74

def convertir_dolares_a_pesos(tasa):
    dolares = int(input("Cuantos dolares tienes: "))
    if dolares <= 0:
        raise ValueError("Los dolares debe ser mayor que cero")

    pesos = dolares * tasa
    return pesos

def opcion(opcion):
    try:
        if opcion == 1:
            print(f"Tienes {convertir_dolares_a_pesos(ARS)} pesos aregentinos")
        if opcion == 2:
            print(f"Tienes {convertir_dolares_a_pesos(COL)} pesos colombianos")
        if opcion == 3:
            print(f"Tienes {convertir_dolares_a_pesos(MEX)} pesos mexicanos")
    except ValueError as e:
        print("Error:", e)

def menuDeOpciones():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre} Bienvenido al convertidor de monedas")
    print(" 1 - Dolares estadounidenses a pesos aregentinos")
    print(" 2 - Dolares estadounidenses a pesos colombianos")
    print(" 3 - Dolares estadounidenses a pesos mexicanos")
    opciones = int(input("Cual es la opcion que deseas: "))
    return opciones

resultado = menuDeOpciones()
opcion(resultado)