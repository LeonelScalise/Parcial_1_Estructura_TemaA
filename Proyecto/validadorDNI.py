from popularInstitucion import *


def validadorDNI():
    inicio = True
    while inicio:
        try:
            DNI = int(input("\nIngrese el DNI: "))
            if len(str(DNI)) != 8:
                raise Exception("\nEl DNI debe tener 8 digitos.\n")
            for alumno in ITBA.alumnos:
                if alumno.dni == DNI:
                    raise Exception("\nEl DNI ya existe, intentalo nuevamente.")
            else:
                inicio = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
            print(e)

    return DNI


def validadorDNIInvitado():
    inicio = True
    while inicio:
        try:
            DNI = int(input("\nIngrese el DNI: "))
            if len(str(DNI)) != 8:
                raise Exception("\nEl DNI debe tener 8 digitos.\n")
            elif DNI not in ITBA.dni_invitados:
                ITBA.dni_invitados.append(DNI)
                ITBA.DniMail.append([])
                inicio = False
            else:
                inicio = False
        except ValueError:
            print('\nEl dato introducido no corresponde al valor esperado.\n')
        except Exception as e:
            print(e)

    return DNI
