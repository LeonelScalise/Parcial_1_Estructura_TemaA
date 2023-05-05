from validadorEmailFormato import *
from popularCarrera import *

        
def validadorEmailExistente(dni):
    inicio = True
    while inicio:  
        
        email = validadorEmailFormato()
        matriz_sin_columna_indicada = []
        flag = True
        for elemento in ITBA.DniMail:
            matriz_sin_columna_indicada.append(elemento)
        for i in range(len(ITBA.dni_invitados)):
            if dni == ITBA.dni_invitados[i]:
                posicion_de_columna = i
                columna_indicada = ITBA.DniMail.copy()[i]
                matriz_sin_columna_indicada.remove(matriz_sin_columna_indicada[posicion_de_columna])
                if matriz_sin_columna_indicada != []:
                    for lista in matriz_sin_columna_indicada:
                        try:
                            if email in lista:
                                raise Exception(f'El email {email} esta asociado a otro DNI.')
                        except Exception as e:
                            print(e)
                            flag = False
                break
        
        if flag == False:
            continue
            
        elif email not in columna_indicada:
            ITBA.DniMail[posicion_de_columna].append(email)
            inicio = False
        elif email in columna_indicada:
            inicio = False

    return email

# lista_dni = [41321,234342,23234]

# matrizDniMail = [[],[],[]]


# matriz_sin_columna_indicada = matriz
# for i in range(len(lista_dni)):
#     if dni_ingresado == lista_dni[i]:
#         posicion_de_columna = i
#         matriz_sin_columna_indicada = matriz_sin_columna_indicada.remove(matriz_sin_columna_indicada[i])
# for fila in matriz_sin_columna_indicada:
#     for elemento in fila:
#         if email == elemento:
#             raise Exception


