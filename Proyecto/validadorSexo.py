def validadorSexo():
    inicio = True
    while inicio:
        try:
            sexo = input("\nIngrese el sexo (M/F): ")
            if sexo not in ["M", "F"]:
                raise Exception("\nEl sexo debe ser 'M' o 'F'.\n")
            else:
                inicio = False
        except ValueError:
                print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e: 
                print(e)
    
    return sexo