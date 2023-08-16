
from empleado import Empleado

class Arbin:
    def __init__(self, dato):
        self.dato=dato
        self.izq=None
        self.der=None
    
    def mod(self, x):
        self.dato=x


class Arbol_Empleados:
    def __init__(self):
        self.raiz=None
   
    def obraiz(self):
        return self.raiz
    
    def agregar(self, Nempleado):
        if self.raiz is None:
            self.raiz=Arbin(Nempleado)
        else:
            self.agregar_recursivo(self.raiz, Nempleado)

    def agregar_recursivo(self, r, Nempleado):
        if Nempleado.edad<r.dato.edad:
            if r.izq is None:
                r.izq=Arbin(Nempleado)
            else:
                self.agregar_recursivo(r.izq, Nempleado)
        else:
            if r.der is None:
                r.der=Arbin(Nempleado)
            else:
                self.agregar_recursivo(r.der, Nempleado)
    
    def buscar(self, dato):
        if raiz is None:
            raiz = self.raiz

        if raiz.dato == dato:
            return raiz
        elif dato < raiz.dato and raiz.izq is not None:
            return self.buscar(dato, raiz.izq)
        elif dato > raiz.dato and raiz.der is not None:
            return self.buscar(dato, raiz.der)
        else:
            return None
        
   
    def imprimir_inorden(self, nodo):
        if nodo is not None:
            self.imprimir_inorden(nodo.izq)
            print(f"ID: {nodo.dato.id}, Nombre: {nodo.dato.nombre}, Edad: {nodo.dato.edad}, Salario: {nodo.dato.salario}")
            self.imprimir_inorden(nodo.der)
    
    def buscarxname(self, r,name):
        if r is not None:
            self.buscarxname(r.izq, name)
            if r.dato.nombre==name:
                print("El salario es", r.dato.salario)
            self.buscarxname(r.der, name)
            
    def buscarname(self, r,name):
        if r is not None:
            self.buscarname(r.izq, name)
            if r.dato.nombre==name:
                return True
            self.buscarname(r.der, name)

    def seeage(self, r,name):
        if r is not None:
            self.seeage(r.izq, name)
            if r.dato.nombre==name:
                print("La edad es", r.dato.edad)
            self.seeage(r.der, name)
                        

    def seeinf(self, r,name):
        if r is not None:
            self.seeinf(r.izq, name)
            if r.dato.nombre==name:
                print(f"El empleado se llama: {r.dato.nombre}, Tiene : {r.dato.edad} Y gana : {r.dato.salario}")
            self.seeinf(r.der, name)
        
    def imprimir_arbol(self):
        self.imprimir_inorden(self.raiz)
    
    may=0
    empmay = None
    def mayor(self, arbol):
        if arbol is not None:
            self.mayor(arbol.izq)
            if self.may<arbol.dato.salario:
                self.may=arbol.dato.salario
                self.empmay=arbol.dato.nombre
            self.mayor(arbol.der)
    
 
    







