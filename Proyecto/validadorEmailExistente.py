from validadorEmailFormato import *
from popularCarrera import *


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
        

inicio = True
while inicio:  
    email = validadorEmailFormato()
    matriz_sin_columna_indicada = ITBA.DniEmail
    columna_indicada = []
    for i in range(len(ITBA.dni_ingresados)):
        if ITBA.dni_ingresados == ITBA.dni_ingresados[i]:
            posicion_de_columna = i
            matriz_sin_columna_indicada.remove(matriz_sin_columna_indicada[posicion_de_columna])
            for elemento in ITBA.DniEmail[posicion_de_columna]:
                columna_indicada.append(elemento)
    for fila in matriz_sin_columna_indicada:
        for elemento in fila:
            if email == elemento:
                raise Exception(f'El email {email} esta asociado a otro DNI.')
    if email not in columna_indicada:
        ITBA.DniEmail[posicion_de_columna].append(email)




