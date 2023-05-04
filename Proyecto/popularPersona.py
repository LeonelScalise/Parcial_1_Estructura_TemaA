from claseInstitucion import *
from clasePersona import Alumno, Profesor, Administrativo
from popularInstitucion import ITBA
from popularCarrera import *
from claseMateria import *
from claseComision import *

ITBA.agregar_carrera(licnegocios)
ITBA.agregar_carrera(licnanalitica)
ITBA.agregar_carrera(ingindustrial)
ITBA.agregar_carrera(inginformatica)

Leo = Alumno("Leonel Scalise","43046873","M","fecha",62523,"fecha","Activo",licnegocios)
Juana = Alumno("Juana Santacreu","4112893","F","fecha",23424,"fecha","Activo",licnegocios)
Mati = Alumno("Matías Díaz Cantón","43573875","M","fecha",62473,"fecha","Activo",licnegocios)
alumno1 = Alumno("alumno1","43031873","M","fecha",62223,"fecha","Activo",licnanalitica)
alumno2 = Alumno("alumno2","4262893","F","fecha",23224,"fecha","Activo",licnanalitica)
alumno3 = Alumno("alumno3","49873875","M","fecha",62573,"fecha","Activo",ingindustrial)
alumno4 = Alumno("alumno4","43075873","M","fecha",62553,"fecha","Activo",inginformatica)
alumno5 = Alumno("alumno5","41147934","F","fecha",23554,"fecha","Activo",inginformatica)
alumno6 = Alumno("alumno6","43577375","M","fecha",67773,"fecha","Activo",inginformatica)
alumno7 = Alumno("alumno7","43045573","M","fecha",68823,"fecha","Activo",inginformatica)
alumno8 = Alumno("alumno8","4112443","F","fecha",29024,"fecha","Activo",ingindustrial)
alumno9 = Alumno("alumno9","43113875","M","fecha",60073,"fecha","Activo",licnegocios)
alumno9.historial_academico.update({"materia 1":5,"materia 2":7,"materia 3":10,"materia 4":8,"materia 5":7,"materia 6":8,"materia 7":8,"materia 8":8,"materia 9":10})


ITBA.agregar_alumno(alumno1)
ITBA.agregar_alumno(alumno2)
ITBA.agregar_alumno(alumno3)
ITBA.agregar_alumno(alumno4)
ITBA.agregar_alumno(alumno5)
ITBA.agregar_alumno(alumno6)
ITBA.agregar_alumno(alumno7)
ITBA.agregar_alumno(alumno8)
ITBA.agregar_alumno(alumno9)

Girafa = Profesor("Profe Girafale", "23123141", "M", "12/12/12", "PR10000", "11/12/12")  #(nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None, comisiones_acargo=None

ElAdmin = Administrativo("El Admin","41741232","M","fecha","AD10000","FECHA INGRESO","girafa@itba.edu.ar","contraseña")  # nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, tramites_abiertos, tramites_resueltos, fecha_baja=None

Analisis_matematico = Materia("55.22", "Analisis matematico", 3, "SDT", "Matematica")
Algebra = Materia("67.30", "Algebra", 6, "SDF", "Matematica")
Microeconomia = Materia("43.74", "Microeconomia", 6, "SDF", "Economia", [Analisis_matematico, Algebra])

comi1 = Comision("A", "201F", Girafa, {"dia":["Lunes"], "horario":["12:30-14:30"]})
comi2 = Comision("A", "202F", Girafa, {"dia":["Martes"], "horario":["12:30-14:30"]})

Analisis_matematico.comisiones.append(comi1)
Algebra.comisiones.append(comi2)

comi1.profesor = Girafa
comi2.profesor = Girafa
Analisis_matematico.profesores.append(Girafa)
Algebra.profesores.append(Girafa)

ITBA.agregar_alumno(Leo)
ITBA.agregar_alumno(Juana)
ITBA.agregar_alumno(Mati)

ITBA.agregar_profesor(Girafa)

ITBA.agregar_administrativo(ElAdmin)

licnegocios.agregar_materia(Analisis_matematico)
licnegocios.agregar_materia(Algebra)
licnegocios.agregar_materia(Microeconomia)
