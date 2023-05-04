#from persona import *
from armado_menu import *
import os
from clasePersona import *
from popularPersona import *
from validadorInputs import *
clear = lambda : os.system('cls')


def menu_principal():
    inicio = True
    while inicio:
        print("\n\t\tMENU PRINCIPAL\n\n1. Administrativo\n2. Alumno\n3. Profesor\n4. Invitado\n5. Salir")
        arranque = validador(5)
        clear()
        if arranque == 1:
            armado_menu("MENU ADMINISTRATIVO", ["Dar alta administrativo", "Iniciar sesion", "Volver"], [lambda : Administrativo.altaAdministrativo(ITBA), lambda : Administrativo.menu_registro_administrativo(ITBA)])
        elif arranque == 2:
            armado_menu("MENU ALUMNO", ["Iniciar Sesion", "Volver"], [lambda : Alumno.menu_registro_alumno(ITBA)])
        elif arranque == 3:
            armado_menu("MENU PROFESOR", ["Iniciar Sesion", "Volver"], [lambda : Profesor.menu_registro_profesor(ITBA)])
        elif arranque == 4:
            armado_menu("MENU INVITADO", ["Ingresar", "Volver"], [lambda : Invitado.registro_invitado(ITBA)])
        elif arranque == 5:
            inicio = False
                       
    
    print('Saliste del menu')


menu_principal()


  