class Empleado:
    def __init__(self, id, nombre, edad, salario):
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.salario=salario

    def tostring(self):
        return print(f"Nombre: ", self.nombre)