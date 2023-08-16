from Arbol import Arbol_Empleados
from empleado import Empleado

Arbol=Arbol_Empleados()

menu= '''
Elije una opcion
1.Agregar empleado
2.Ver salario del empleado
3.Ver edad del empleado
4.Ver informacion del empleado completa
5.Ver arbol
6.Ver empleado con mayor salario
7.Salir
'''  

Arbol.agregar(Empleado(123,"Juan", 30, 50000))
Arbol.agregar(Empleado(345,"María", 25, 65000))
Arbol.agregar(Empleado(567, "Carlos", 28, 55000))
Arbol.agregar(Empleado(789,"Laura", 22, 48000))
Arbol.agregar(Empleado(1463,"Pedro", 30, 50000))
Arbol.agregar(Empleado(3351,"Rosa", 23, 60000))
Arbol.agregar(Empleado(521, "Daniel", 28, 55000))
Arbol.agregar(Empleado(781,"Leidis", 19, 48000))
op = 0
while op != 8 and op>=0 and op <=7:
    op=int(input(menu))
    if op==1:
        id=int(input("Digite el identificador del empleado: "))
        name = input("Escirba el nombre del empleado: ")
        age = int(input("Escriba la edad del empleado: "))
        salario = int(input("Escriba el salario del empleado: "))
        Arbol.agregar(Empleado(id, name, age, salario))
    elif op==2:
        nam= input("Escriba el nombre del empleado: ")
        Arbol.buscarxname(Arbol.obraiz(), nam)
    elif op==3:
        na1= input("Escriba el nombre del empleado: ")
        Arbol.seeage(Arbol.obraiz(), na1)
        
    elif op==4:
        na2= input("Escriba el nombre del empleado")
        Arbol.seeinf(Arbol.obraiz(), na2)
    
    elif op==5:
        Arbol.imprimir_arbol()
    
    elif op==6:
        Arbol.mayor(Arbol.raiz)
        print(f"El empleado con mayor salario es: {Arbol.empmay} con un salario de: {Arbol.may}")