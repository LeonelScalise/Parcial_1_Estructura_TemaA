from claseInstitucion import *
import os
from armado_menu import *
from string import *
from validadorInputs import *

clear = lambda : os.system('cls')


def reintento():
    print("1. Reintentar\n2. Volver")
    eleccion = validador(2)
    if eleccion == 1:
        clear()
        return True
    elif eleccion == 2:
        clear()
        return False
        
    

def validadorLegajoAlumnos(institucion):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = int(input("Ingrese el numero de legajo: "))
            
            if len(str(legajoingresado)) != 5:
                raise Exception("\nEl legajo debe ser un numero de 5 digitos.\n") 
            if legajoingresado not in institucion.legajos_alumnos:
                raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
            inicio = reintento()
        except Exception as e: 
            print(e)      #imprime el mensaje que vos indicaste antes
            inicio = reintento() 
    return legajoingresado

def validadorLegajoAdminyProf(institucion, rol = 'administrativo'):
    inicio = True
    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            legajoingresado = input(f'Ingrese el numero de legajo de {rol}: ').upper()
            
            if len(legajoingresado) != 7:
                raise Exception("\nEl legajo debe ser una cadena de 7 digitos.\n")
            if rol == 'profesor':
                if legajoingresado[:2] != "PR":
                    raise Exception("\nEl legajo debe comenzar con las primeras dos letras de su rol.\n")
                if legajoingresado not in institucion.legajos_profesores:
                    raise Exception("\nEl legajo no existe, intente nuevamente.\n") 
                else:
                    inicio = False
            else:
                if legajoingresado[:2] != "AD":
                    raise Exception("\nEl legajo debe comenzar con las primeras dos letras de su rol.\n")
                if legajoingresado not in institucion.legajos_administrativos:
                    raise Exception("\nEl legajo no existe, intente nuevamente.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
                else:
                    inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
            inicio = reintento()
        except Exception as e: 
            print(e)      #imprime el mensaje que vos indicaste antes
            inicio = reintento() 
    return legajoingresado
