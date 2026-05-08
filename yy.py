class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"soy {self.nombre} y tengo {self.edad} años :3")
        gente.append(self)

    def hablar(self):
        print("holi")


class Mujer(Persona):
    def __init__(self, nombre, edad, amor):
        super().__init__(nombre,edad)
        self.amor = amor

    def hablar(self):
        print("guh..")


gente = []

while True:
    nombre = input("Ingresa el nombre de tu persona: ")
    edad = int(input("Ingresa la edad: "))
    tipo = input("Es mujer? (s/n): ")
    lvlm = int(input("nivel d amor: "))

    if tipo.lower() == 's':
        Mujer(nombre, edad, lvlm)

    elif tipo.lower() == 'n':
        Persona(nombre,edad)
        
    break

print(gente)