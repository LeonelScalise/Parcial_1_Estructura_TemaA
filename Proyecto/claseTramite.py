from clasePersona import *
class Tramite():
    def __init__(self, id, alumno, administrativo, tipo_de_tramite, fecha_de_inicio, profesor = None, estado="Pendiente", comision=None):
        self.id = id
        self.alumno = alumno
        self.administrativo = administrativo
        self.tipo_de_tramite = tipo_de_tramite
        self.fecha_de_inicio = fecha_de_inicio
        self.estado = estado
        self.profesor = profesor
        self.comision = comision
    
    def __str__(self):
        return "{} es un tramite del tipo: {}, creado por {} y el administrativo encargado es {}".format(self.id,self.tipo_de_tramite,self.alumno,self.administrativo)
import random
if __name__ == "__main__":
    l=["Hola"]
    print(len(l))
    i_random=random.randint(0,len(l)-1)
    print(l[i_random])