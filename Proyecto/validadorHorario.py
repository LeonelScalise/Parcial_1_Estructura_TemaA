import re

def validadorHorario(lista_dias):
    repe = len(lista_dias)
    inicio = True
    patron = fr"^\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*[-]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)(\s*[,]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*[-]{{1}}\s*(([0-1]\d)|(2[0-3])|([0-9]{{1}})):([0-5]\d)\s*){{{repe-1}}}$"
    while inicio:
        try:
            horario = input("\nIngrese el/los horario/s respectivamente a los dias ingresados previamente.(Ejemplo: 10:30 - 12:40): ")
            if re.match(patron, horario) == None:
                raise Exception("\nIngrese un horario valido siguiendo el formato indicado y asegurese de tener la misma cantidad de horarios que de dias.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return horario