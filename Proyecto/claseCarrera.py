from claseMateria import *

class Carrera():
    def __init__(self,nombre, director_carrera, creditos_para_recibirse = 0):
        self.nombre = nombre
        self.creditos_para_recibirse = creditos_para_recibirse
        self.director_carrera = director_carrera
        self.materias = []
        self.alumnos_actuales = []
        self.alumnos_recibidos = []
        self.cantidad_alumnos_recibidos=0

    def agregar_materia(self, materia:Materia):

        self.materias.append(materia)
        self.creditos_para_recibirse += materia.creditos
        print("Materia agregada")


    def __str__(self):
        return "La carrera {} tiene de director a {} y necesita {} creditos para recibirse".format(self.nombre, self.director_carrera, self.creditos_para_recibirse)
