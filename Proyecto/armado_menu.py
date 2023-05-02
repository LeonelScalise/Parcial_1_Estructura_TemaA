from validadorInputs import *
import os
clear = lambda : os.system('cls') #para limpiar la terminal cada vez que se elija una opcion y aparezca lo nuevo

def armado_menu(nombre_menu, lista_opciones, lista_funciones): #arma los menus de todos, le entran como argumento el nombre que queres que tenga el menu, una lista de el texto que queres que haya en cada opcion, y la lista donde van a estar las funciones propias de cada menu (los metodos dentro de las clases)
    inicio_while = True
    while inicio_while: #arranca loop para crear las opciones
        cont_opciones = 0
        lista_numeros = []
        print(f'\n\t\t{nombre_menu}\n') #aparece el nombre del menu que pusiste
        for texto in lista_opciones: #agarra uno por uno el texto de cada opcion
            cont_opciones += 1 #comienza por la opcion 1
            lista_numeros.append(cont_opciones)
            print(f'{cont_opciones}. {texto}') #imprime 1. "el texto que pusiste que va en la opcion 1"
        opcion_elegida = validador(cont_opciones) #se fija que la opcion elegida sea valida
        clear() #limpia la terminal luego de elegida la opcion

        for numero in lista_numeros:
            if opcion_elegida == cont_opciones:
                inicio_while = False #si elige la ultima opcion, eligio "Salir" porque siempre esta como ultima opcion
            elif opcion_elegida == numero:
                lista_funciones[numero - 1]()
    
        # aca cuando cambias de usuario en iniciar sesion, lista_numeros tiene mas elementos entonces se bugea --> a chequear --> ya lo arregle

