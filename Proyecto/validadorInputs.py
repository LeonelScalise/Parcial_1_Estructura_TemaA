
def validador(cant_opciones):
    inicio = True

    while inicio: #arranca el loop
        try: #intenta pedir una respuesta
            rta = int(input('\nIngresa una opción: '))
            if rta not in list(range(1, cant_opciones + 1)):
                raise Exception("\nNo es una opción válida.\n") #si no cumple con la condición que se indica levanta un error con un mensaje
            else:
                inicio = False #frena el loop si está todo ok
        except ValueError: #si ingresan un tipo de dato incorrecto no se rompe el sistema sino que te vuelve a pedir una rta.
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
            print(e) #imprime el mensaje que vos indicaste antes
    
    return rta