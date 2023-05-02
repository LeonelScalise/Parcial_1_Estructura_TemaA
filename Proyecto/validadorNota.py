def validadorNota():
    inicio = True
    while inicio:
        try:
            Nota_final = int(input("\nIngrese la nota final del alumno: "))
            if Nota_final > 10 or Nota_final < 1:
                raise Exception("\nLa nota debe ser un numero entero de 1 a 10.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return Nota_final