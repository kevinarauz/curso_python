"""
Hola
"""

# comentario individual
"""
first_name = "kevin"
last_name = "arauz"
a =3
# print(a)

y = 5
"""

# funciones
"""
def my_func():
    y = 2
    #print(y)

    def my_other_func():
        y = 3
        print(y)

    my_other_func()
    print(y)

my_func()
print(y)
"""

# condiciones

"""
if a == 1:
    print("Hola")
else:
    print(a+1)
    
"""

"""
ARS = 202.91
COL = 4849.99
MEX = 18.74

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre} Bienvenido al convertidor de monedas")

print(" 1 - Dolares estadounidenses a pesos aregentinos")
print(" 2 - Dolares estadounidenses a pesos colombianos")
print(" 3 - Dolares estadounidenses a pesos mexicanos")

opcion = int(input("Cual es la opcion que deseas: "))

if opcion == 1:
    dolares = int(input("Cuantos dolares tienes: "))
    pesos = ARS * dolares
    print(f"Tienes {pesos} pesos aregentinos")
else:
    if opcion == 2:
        dolares = int(input("Cuantos dolares tienes: "))
        pesos = COL * dolares
        print(f"Tienes {pesos} pesos colombianos")
    else:
        if opcion == 3:
            dolares = int(input("Cuantos dolares tienes: "))
            pesos = MEX * dolares
            print(f"Tienes {pesos} pesos mexicanos")
        else:
            print(f"La opcion seleccionada no existe")
"""

# refactor

ARS = 202.91
COL = 4849.99
MEX = 18.74

def convertir_dolares_a_pesos(tasa):
    dolares = int(input("Cuantos dolares tienes: "))
    pesos = dolares * tasa
    return pesos

def opcion(opcion):
    if opcion == 1:
        print(f"Tienes {convertir_dolares_a_pesos(ARS)} pesos aregentinos")
    if opcion == 2:
        print(f"Tienes {convertir_dolares_a_pesos(COL)} pesos colombianos")
    if opcion == 3:
        print(f"Tienes {convertir_dolares_a_pesos(MEX)} pesos mexicanos")

def menuDeOpciones():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre} Bienvenido al convertidor de monedas")

    print(" 1 - Dolares estadounidenses a pesos aregentinos")
    print(" 2 - Dolares estadounidenses a pesos colombianos")
    print(" 3 - Dolares estadounidenses a pesos mexicanos")

menuDeOpciones()
opcionMenu = int(input("Cual es la opcion que deseas: "))
opcion(opcionMenu)

"""
if opcion == 1:
    print(f"Tienes {convertir_dolares_a_pesos(ARS)} pesos aregentinos")
else:
    if opcion == 2:
        print(f"Tienes {convertir_dolares_a_pesos(COL)} pesos colombianos")
    else:
        if opcion == 3:
            print(f"Tienes {convertir_dolares_a_pesos(MEX)} pesos mexicanos")
        else:
            print(f"La opcion seleccionada no existe")         
"""