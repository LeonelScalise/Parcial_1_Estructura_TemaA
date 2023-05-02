class Comision:
    def __init__(self, codigo_comision, aula, profesor, dia_y_horario = {}):
        self.codigo_comision = codigo_comision
        self.aula = aula
        self.profesor = profesor
        self.dia_y_horario = dia_y_horario
        self.alumnos = []