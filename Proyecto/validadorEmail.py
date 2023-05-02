import re
import string



def validadorEmail():
    inicio = True
    patron = fr"^\s*[{{{string.ascii_lowercase}}}]+[@]{{1}}(itba){{1}}[.]{{1}}(edu){{1}}[.]{{1}}(ar){{1}}\s*$"
    while inicio:
        try:
            email = input("\nIngrese su email: ").lower()
            if re.match(patron, email) == None:
                raise Exception("\nEl formato de email no corresponde (Ejemplo: pepito@itba.edu.ar)\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return email

