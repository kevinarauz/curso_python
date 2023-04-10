class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años")

p1 = Persona("Kevin", 20)
p1.saludar()
p1.cumplir_anos()

p2 = Persona("Ana", 21)
p2.saludar()
p2.cumplir_anos()
