from armado_menu import *
from claseInstitucion import *
import os
from claseTramite import *
import random
from popularInstitucion import ITBA
from claseCarrera import *
from validadorNota import *
import matplotlib.pyplot as plt
from validadorInputs import *
from validadorLegajo import *
from validadorDNI import *
from validadorSexo import *
from validadorFecha import *
from validadorAula import *
from validadorDia import *
from validadorHorario import *
from validadorEmailExistente import *


def clear(): return os.system('cls')


class Persona:
    def __init__(self, nombre_apellido, dni, sexo = None, fecha_nac = None):
        self.dni = dni
        self.nombre_apellido = nombre_apellido
        self.sexo = sexo
        self.fecha_nac = fecha_nac


class Alumno(Persona):

    def menu_registro_alumno(institucion: Institucion):
        x = "o"
        legajo_ingresado = validadorLegajoAlumnos(institucion)
        clear()
        for alumno in institucion.alumnos:
            if alumno.legajo == legajo_ingresado:
                if alumno.sexo == "F":
                    x = "a"
                return armado_menu(f"Bienvenid{x} {alumno.nombre_apellido}", ["Inscripcion a materia", "Desinscripción a materia", "Iniciar Tramite", "Estadisticas", "Volver"], [lambda: alumno.displayMateriasDisponibles(), lambda: alumno.desinscribirMateria(), lambda: alumno.iniciarTramite(ITBA), lambda: alumno.estadisticasAlumno()])

    def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, estado_alumno="Activo", carrera=None, fecha_baja=None):
        super().__init__(nombre_apellido, dni, sexo, fecha_nac)
        self.legajo = legajo
        self.materias_aprobadas = []
        self.materias_en_curso = []
        self.fecha_ingreso = fecha_ingreso
        self.carrera = carrera
        self.fecha_baja = fecha_baja
        self.creditos_aprobados = 0
        self.historial_academico = {}
        self.estado_alumno = estado_alumno
        self.tramites_abiertos = []
        self.tramites_resueltos = []

    def __str__(self):
        return self.nombre_apellido

    def iniciarTramite(self, institucion):
        id_tramite = 0

        if len(institucion.historial_tramites) != 0:
            id_tramite = institucion.historial_tramites[-1].id + 1
        tipo_de_tramite = input(
            "Ingrese el motivo del tramite o 'exit' si no quiere iniciar tramite: ")
        if tipo_de_tramite == 'exit':
            return print("No se inició tramite")
        else:
            cantidad_administrativos = len(institucion.administrativos)
            i_random = random.randint(0, cantidad_administrativos - 1)
            administrativo_asignado = institucion.administrativos[i_random]
            nuevo_tramite = Tramite(
                id_tramite, self, administrativo_asignado, tipo_de_tramite, "24/4/2023")
            administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
            institucion.tramites_abiertos.append(nuevo_tramite)
            institucion.historial_tramites.append(nuevo_tramite)
            self.tramites_abiertos.append(nuevo_tramite)
            return print("Ya iniciaste el tramite")

    def inscribirMateria(self, materia):
        contador = 0
        flag = True

        print(
            f"\t\t\nComisiones disponibles para incripcion en {materia.nombre}\n")
        if len(materia.comisiones) != 0:
            while flag:
                for comisiones in materia.comisiones:
                    contador += 1
                    print(
                        f"{contador}. {comisiones.codigo_comision}: {comisiones.dia_y_horario}")

                print(f"{contador + 1}. Volver")

                opcion_elegida = validador(contador + 1)
                clear()

                if opcion_elegida == contador + 1:
                    flag = False
                else:
                    comision = materia.comisiones[opcion_elegida - 1]
                    comision.alumnos.append(self)

                    materia.alumnos.append(comision.alumnos[-1])
                    self.materias_en_curso.append(materia)
                    clear()
                    flag = False
                    print(
                        f"Te has inscripto correctamente a la comision {comision.codigo_comision} de la materia {materia.nombre}")

        else:
            print("La materia no posee comisiones por el momento")

    def displayMateriasDisponibles(self):
        materias_disponibles = []
        c1 = 0
        c2 = 0
        flag = True

        print(
            f"\t\t\nMaterias disponibles para incripcion de {self.nombre_apellido}\n")
        for materia in self.carrera.materias:
            if len(materia.correlativas) != 0:
                for corre in materia.correlativas:
                    if corre in self.materias_aprobadas:
                        c1 += 1  # sirve para verificar si es igual a la cantidad de correlativas que tiene la materia, eso implicaría que tiene todas las correlativas aprobadas
                if c1 == len(materia.correlativas) and materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
                    materias_disponibles.append(materia)
            elif materia not in self.materias_aprobadas and materia not in self.materias_en_curso:
                materias_disponibles.append(materia)

        while flag:
            for materia in materias_disponibles:
                c2 += 1
                print(f"{c2}. {materia.codigo_materia} {materia.nombre}")

            print(f"{c2 + 1}. Volver")
            opcion_elegida = validador(c2 + 1)
            clear()
            if opcion_elegida == c2 + 1:
                flag = False
            else:
                self.inscribirMateria(materias_disponibles[opcion_elegida - 1])
                flag = False

    def desinscribirMateria(self):
        contador = 0
        flag = True
        print("Materias en las que está inscripto\n")
        if len(self.materias_en_curso) != 0:
            while flag:
                for materia in self.materias_en_curso:
                    contador += 1
                    print(f"{contador}. {materia.codigo_materia} {materia.nombre}")

                print(f"{contador + 1}. Volver")

                opcion_elegida = validador(contador + 1)
                clear()

                if opcion_elegida == contador + 1:
                    flag = False
                else:
                    materia_elegida = self.materias_en_curso[opcion_elegida - 1]
                    clear()
                    flag = False
                    self.materias_en_curso.remove(materia_elegida)
                    materia_elegida.alumnos.remove(self)
                    for comision in materia_elegida.comisiones:
                        if self in comision.alumnos:
                            comision.alumnos.remove(self)
                    print(
                        f"Ya no se encuentra inscripto en {materia_elegida.nombre}")

        else:
            print("No se encuentra anotado en ninguna materia")

    def estadisticasAlumno(self):
        armado_menu("ESTADISTICAS DEL ALUMNO", [
                    'Ver el promedio de la carrera', "Volver"], [lambda: self.verPromedioCarrera()])

    def verPromedioCarrera(self):
        suma = 0
        cantidad_notas = 0
        promedio = 0

        for nota in self.historial_academico.values():
            suma += nota
            cantidad_notas += 1

        if cantidad_notas != 0:
            promedio = suma / cantidad_notas
            return print(f"Promedio lineal de la carrera: {promedio}")

        else:
            print(f"{self.nombre_apellido} no tiene notas cargadas por el momento")


class Profesor(Persona):
    def menu_registro_profesor(institucion: Institucion):
        x = "o"
        legajo_ingresado = validadorLegajoAdminyProf(institucion, 'profesor')
        clear()
        for prof in institucion.profesores:
            if prof.legajo == legajo_ingresado:
                if prof.sexo == "F":
                    x = "a"
                return armado_menu(f"Bienvenid{x} {prof.nombre_apellido}", ["Subir nota final", "Iniciar Tramite", "Volver"], [lambda: prof.displayMateriasActivas(), lambda: prof.iniciarTramite(ITBA)])

    def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso, fecha_baja=None):
        super().__init__(nombre_apellido, dni, sexo, fecha_nac)
        self.legajo = legajo
        self.fecha_ingreso = fecha_ingreso
        self.fecha_baja = fecha_baja
        self.comisiones_a_cargo = []
        self.tramites_abiertos = []
        self.tramites_resueltos = []

    def iniciarTramite(self, institucion):
        id_tramite = 0

        if len(institucion.historial_tramites) != 0:
            id_tramite = institucion.historial_tramites[-1].id + 1
        tipo_de_tramite = input(
            "Ingrese el motivo del tramite o 'exit' si no quiere iniciar tramite: ")
        if tipo_de_tramite == 'exit':
            return print("No se inició tramite")
        else:
            cantidad_administrativos = len(institucion.administrativos)
            i_random = random.randint(0, cantidad_administrativos - 1)
            administrativo_asignado = institucion.administrativos[i_random]
            nuevo_tramite = Tramite(
                id_tramite, None, administrativo_asignado, tipo_de_tramite, "24/4/2023", self)
            administrativo_asignado.tramites_abiertos.append(nuevo_tramite)
            institucion.tramites_abiertos.append(nuevo_tramite)
            institucion.historial_tramites.append(nuevo_tramite)
            self.tramites_abiertos.append(nuevo_tramite)
            return print("Ya iniciaste el tramite")

    def subirNotaFinal(self, materia):
        comisiones_a_cargo = []
        contador = 0
        flag = True
        print("Seleccione la comision a la que desea subir la nota final:\n")
        for comision in materia.comisiones:
            if self == comision.profesor:
                comisiones_a_cargo.append(comision)
        while flag:
            for comision in comisiones_a_cargo:
                contador += 1
                print(
                    f"{contador}. Comision {comision.codigo_comision} de {materia.nombre}")

            print(f"{contador + 1}. Volver")

            opcion_elegida1 = validador(contador + 1)
            clear()

            if opcion_elegida1 == contador + 1:
                flag = False
                comision_elegida = None
            else:
                comision_elegida = comisiones_a_cargo[opcion_elegida1 - 1]
                clear()
                flag = False

        if comision_elegida is not None:
            contador = 0
            flag = True
            print("Seleccione el alumno al que desea subir la nota final:\n")
            if len(comision_elegida.alumnos) != 0:
                while flag:
                    for alumno in comision_elegida.alumnos:
                        contador += 1
                        print(f"{contador}. {alumno.nombre_apellido}")

                    print(f"{contador + 1}. Volver")

                    opcion_elegida2 = validador(contador + 1)
                    clear()

                    if opcion_elegida2 == contador + 1:
                        flag = False
                    else:
                        clear()
                        alumno_elegido = comision_elegida.alumnos[opcion_elegida2 - 1]
                        Nota_final = validadorNota()
                        alumno_elegido.historial_academico[materia.nombre] = Nota_final
                        flag = False
                        if Nota_final >= 4:
                            alumno_elegido.materias_aprobadas.append(materia)
                            alumno_elegido.materias_en_curso.remove(materia)
                            materia.alumnos.remove(alumno_elegido)
                            comision_elegida.alumnos.remove(alumno_elegido)
                            alumno_elegido.creditos_aprobados += materia.creditos
                            print(
                                f"La nota final se cargó correctamente. {alumno_elegido} aprobó {materia.nombre}")
                        else:
                            print(
                                f"La nota final se cargó correctamente. {alumno_elegido} no aprobó {materia.nombre}")
            else:
                print("No hay alumnos en esta comision")

    def displayMateriasActivas(self):
        contador = 0
        materias_activas = []
        flag = True
        print("Materias a las que está inscripto\n")
        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                if self in materia.profesores:
                    materias_activas.append(materia)
        while flag:
            for materia in materias_activas:
                contador += 1
                print(f"{contador}. {materia.codigo_materia} {materia.nombre}")

            print(f"{contador + 1}. Volver")

            opcion_elegida = validador(contador + 1)
            clear()

            if opcion_elegida == contador + 1:
                flag = False
            else:
                clear()
                flag = False
                self.subirNotaFinal(materias_activas[opcion_elegida - 1])


class Administrativo(Persona):

    def altaAdministrativo(institucion: Institucion):

        nombre_apellido = input(
            "Ingrese el nombre y apellido del administrativo: ")
        dni = validadorDNI()
        fecha_nac = validadorFecha()
        sexo = validadorSexo()
        flag=True
        while flag:
            email=validadorEmailFormato()
            if email not in ITBA.emailsAdmins:
                ITBA.emailsAdmins.append(email)
                flag=False
            else:
                print("El email ya esta asignado a un administrativo, ingrese otro")
        contraseña=input("Ingrese una contraseña: ")

        if len(ITBA.legajos_administrativos) != 0:
            legajo_numero = int(ITBA.legajos_administrativos[-1][2:])+1
            legajo_alfa = "AD"
            legajo = legajo_alfa + str(legajo_numero)
        else:
            legajo = "AD10000"
        fecha_ingreso = datetime.strptime(
            datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        institucion.administrativos.append(Administrativo(
            nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso,email,contraseña))
        institucion.legajos_administrativos.append(legajo)
        clear()
        print(
            f'El administrativo {nombre_apellido} se ha creado correctamente')
        print(ITBA.administrativos[-1].contraseña)

    def menu_registro_administrativo(institucion: Institucion):
        inicio=True
        c=0
        while inicio:
                
            x = "o"
            if c == 0:

                legajo_ingresado = validadorLegajoAdminyProf(institucion)
                
            contra=input("Ingrese su contraseña: ")

            clear()
            for admin in institucion.administrativos:
                if admin.legajo == legajo_ingresado and admin.contraseña==contra:
                    if admin.sexo == "F":
                        x = "a"
                    return armado_menu(f"Bienvenid{x} {admin.nombre_apellido}", ["Dar de alta alumno", "Dar de baja alumno", "Dar de alta profesor", "Dar de baja profesor", "Dar de baja Administrativo", "Tramites", "Crear Comisión", "Asignar profesor a materia", "Desasignar profesor a materia", "Estadisticas","Cambiar Contraseña", "Volver"], [lambda: admin.altaAlumno(), lambda: admin.bajaAlumno(), lambda: admin.altaProfesor(), lambda: admin.bajaProfesor(), lambda: admin.bajaAdministrativo(), lambda: admin.displayTramiteActivo(), lambda:admin.crearComision(), lambda: admin.asignarProfesor(), lambda: admin.desasignarProfesor(), lambda: admin.estadisticasGenerales(),lambda : admin.actualizarContraseña()])
                elif admin.legajo == legajo_ingresado:
                    print("La contraseña es incorrecta\n")
                    print("\n1. Reintentar\n2. Volver")
                    opcion_elegida=validador(2)
                    if opcion_elegida == 2:
                        inicio=False
            c+=1

    def __init__(self, nombre_apellido, dni, sexo, fecha_nac, legajo, fecha_ingreso,email,contraseña, fecha_baja=None):
        super().__init__(nombre_apellido, dni, sexo, fecha_nac)
        self.legajo = legajo
        self.fecha_ingreso = fecha_ingreso
        # Dejamos esto por si queres hacerlo fede, si te da fiaca, borralo tranqui o dejalo para implementarlo post-entrega
        self.fecha_baja = fecha_baja
        self.tramites_abiertos = []
        self.tramites_resueltos = []
        self.email=email
        self.contraseña=contraseña

    def asignarProfesor(self):
        contador = 0
        flag1 = False
        flag2 = True
        legajo_profesor = validadorLegajoAdminyProf(ITBA, "profesor")
        materias_disponibles = []
        for profesor in ITBA.profesores:
            if profesor.legajo == legajo_profesor:
                profesor_elegido = profesor
                clear()
        print("Materias a las que se lo puede asignar\n")
        while flag2:
            for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    if len(materia.comisiones) > 0:
                        for comision in materia.comisiones:
                            if comision.profesor == None:
                                flag1 = True
                    if flag1:
                        contador += 1
                        materias_disponibles.append(materia)
                        print(
                            f"{contador}. {materia.codigo_materia} {materia.nombre}")
                        flag1 = False

            if len(materias_disponibles) == 0:
                print("Todas las materias tienen un profesor asignado")
            else:
                print(f"{contador + 1}. Volver")
                opcion_elegida1 = validador(contador + 1)
                if opcion_elegida1 == contador + 1:
                    flag2 = False
                else:
                    materia_elegida = materias_disponibles[opcion_elegida1 - 1]
                    clear()
                    flag2 = False

        print(
            f"Comisiones de {materia_elegida.nombre} a las que se lo puede asignar\n")
        contador = 0
        flag2 = True

        while flag2:
            for comision in materia_elegida.comisiones:
                if comision.profesor == None:
                    contador += 1
                    print(
                        f"{contador}. Comision {comision.codigo_comision} de {materia_elegida.nombre}")

            print(f"{contador + 1}. Volver")

            opcion_elegida2 = validador(contador + 1)
            if opcion_elegida2 == contador + 1:
                flag2 = False
            else:
                comision_elegida = materia_elegida.comisiones[opcion_elegida2 - 1]
                comision_elegida.profesor = profesor_elegido
                if profesor_elegido not in materia_elegida.profesores:
                    materia_elegida.profesores.append(profesor_elegido)
                flag2 = False

            print(
                f"Se ha asignado correctamente a {profesor_elegido.nombre_apellido} a la comision {comision_elegida.codigo_comision} de {materia_elegida.nombre}")

    def desasignarProfesor(self):
        materias_de_profesor = []
        c1 = 0
        c2 = 0
        legajo_profesor = validadorLegajoAdminyProf(ITBA, "profesor")
        for profesor in ITBA.profesores:
            if profesor.legajo == legajo_profesor:
                profesor_elegido = profesor
                clear()

        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                for profesor in materia.profesores:
                    if profesor.legajo == legajo_profesor:
                        materias_de_profesor.append(materia)

        print(
            f'¿Quiere desasignar a {profesor_elegido.nombre_apellido} de una materia o de una comisión en específico?\n\n1. Materia\n2. Comision\n')

        opcion_elegida1 = validador(2)

        if opcion_elegida1 == 1:

            if len(materias_de_profesor) == 0:
                print("El profesor no tiene materias asignadas.")
            else:

                print(
                    f'Elija materia para desasignar a {profesor_elegido.nombre_apellido}\n\n')
                for materia in materias_de_profesor:
                    c1 += 1
                    print(f'{c1}. {materia.nombre}')

                opcion_elegida2 = validador(c1)
                materia_elegida = materias_de_profesor[opcion_elegida2 - 1]

                print(
                    f'¿Seguro que quiere desasignar al profesor {profesor_elegido.nombre_apellido} de la materia {materia_elegida.nombre}?\n\n1. Sí\n2. No (Volver)\n')
                opcion_elegida3 = validador(2)
                if opcion_elegida3 == 1:
                    materia_elegida.profesores.remove(profesor_elegido)
                    for comi in materia_elegida.comisiones:
                        if comi.profesor.legajo == legajo_profesor:
                            comi.profesor = None

                print(
                    f'La materia {materia_elegida.nombre} tiene {len(materia_elegida.profesores)} profesores')

        elif opcion_elegida1 == 2:
            if len(materias_de_profesor) != 0:

                print(
                    f'¿De qué materia es la comisión de la cual quiere desasignar al profesor {profesor_elegido.nombre_apellido}?\n\n')
                for materia in materias_de_profesor:
                    c1 += 1
                    print(f'{c1}. {materia.nombre}')

                opcion_elegida4 = validador(c1)
                materia_elegida = materias_de_profesor[opcion_elegida4 - 1]
                print(f'Escoja la comisión para desasignar\n\n')
                for comi in materia_elegida.comisiones:
                    if comi.profesor != None and comi.profesor == profesor_elegido:
                        c2 += 1
                        print(f'{c2}. {comi.codigo_comision}')

                opcion_elegida5 = validador(c2)
                comision_elegida = materia_elegida.comisiones[opcion_elegida5 - 1]

                print(
                    f'¿Seguro que quiere desasignar al profesor {profesor_elegido.nombre_apellido} de la comision {comision_elegida.codigo_comision} de la materia {materia_elegida.nombre}?\n\n1. Sí\n2. No (Volver)\n')
                opcion_elegida6 = validador(2)
                if opcion_elegida6 == 1:
                    comision_elegida.profesor = None
                    chequeo_profe_en_materia = 0
                    for comi in materia_elegida.comisiones:
                        if comi.profesor == profesor_elegido:
                            chequeo_profe_en_materia += 1
                    if chequeo_profe_en_materia == 0:
                        materia_elegida.profesores.remove(profesor_elegido)

                print(
                    f'La materia {materia_elegida.nombre} tiene {len(materia_elegida.profesores)} profesores')

            else:
                print("El profesor no tiene comisiones a cargo.")

    def __str__(self):
        return "{} es administrativo y tiene el legajo {}".format(self.nombre_apellido, self.legajo)

    def tacharTramite(self, id_tram):
        for tramite in self.tramites_abiertos:
            if tramite.id == id_tram:
                # Si esta, tengo que eliminarlo de las listas que estan en Institución y la propia lista del administrativo
                ITBA.tramites_abiertos.remove(tramite)
                self.tramites_abiertos.remove(tramite)
            # Una vez que lo saco de las listas, tengo que cambiar el estado del tramite a "Resuelto"
                tramite.estado = "Resuelto"
            # Una vez que le cambio el estado, tengo que poner el tramite en la lista de tramites resueltos de la Institución y el administrativo
                ITBA.tramites_resueltos.append(tramite)
                self.tramites_resueltos.append(tramite)
                if tramite.alumno != None:
                    tramite.alumno.tramites_abiertos.remove(tramite)
                    tramite.alumno.tramites_resueltos.append(tramite)
                elif tramite.profesor != None:
                    tramite.profesor.tramites_abiertos.remove(tramite)
                    tramite.profesor.tramites_resueltos.append(tramite)

                return print("El tramite {} ha sido resuelto".format(tramite.tipo_de_tramite))
        clear()

    def resolverTramite(self, tramite):  # menu para resolver trámite
        print(
            f'¿Quiere resolver el tramite "{tramite.tipo_de_tramite}" del alumno {tramite.alumno.nombre_apellido}?')
        print("1. Resolver tramite\n2. Volver")
        rta = validador(2)
        if rta == 1:
            self.tacharTramite(tramite.id)

    def displayTramiteActivo(self):
        resolviendo_tramites = True
        while resolviendo_tramites:
            cont_opciones = 1
            for tramite in self.tramites_abiertos:  # por cada tramite activo que tiene el administrativo
                # lo muestra como opcion
                print(f'{cont_opciones}. {tramite.tipo_de_tramite}')
                cont_opciones += 1
            print(f'{cont_opciones}. Volver')
            opcion_elegida = validador(cont_opciones)
            if opcion_elegida == cont_opciones:
                resolviendo_tramites = False
            else:
                self.resolverTramite(self.tramites_abiertos[opcion_elegida-1])

    def altaAlumno(self):
        nombre = input("Ingrese el nombre del alumno: ")
        dni = validadorDNI()
        sexo = validadorSexo()
        fecha_nacimiento = validadorFecha()
        if len(ITBA.legajos_alumnos) != 0:
            legajo = ITBA.legajos_alumnos[-1] + 1
        else:
            legajo = 10000
        fecha_ingreso = datetime.strptime(
            datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        contador = 0
        flag = True
        alumno_nuevo = Alumno(
            nombre, dni, sexo, fecha_nacimiento, legajo, fecha_ingreso)
        clear()
        # Para que el administrativo anote al alumno en un objeto carrera
        print(f'\n\t\t Seleccione la carrera del alumno\n')
        while flag:
            for carrera in ITBA.carreras:
                contador += 1
                print(f"{contador}. {carrera.nombre}")

            print(f"{contador + 1}. Cancelar")

            opcion_elegida = validador(contador + 1)
            if opcion_elegida == contador + 1:
                flag = False
            else:
                alumno_nuevo.carrera = ITBA.carreras[opcion_elegida-1]
                clear()
                flag = False
                print("Se ha anotado al alumno a la carrera: ",
                      alumno_nuevo.carrera.nombre)
                ITBA.agregar_alumno(alumno_nuevo)
                alumno_nuevo.carrera.alumnos_actuales.append(alumno_nuevo)

    def altaProfesor(self):
        nombre = input("Ingrese el nombre del profesor: ")
        dni = validadorDNI()
        sexo = validadorSexo()
        fecha_nacimiento = validadorFecha()
        if len(ITBA.legajos_profesores) != 0:
            legajo_numero = int(ITBA.legajos_profesores[-1][2:]) + 1
            legajo_alfa = "PR"
            legajo = legajo_alfa + str(legajo_numero)
        else:
            legajo = "PR10000"
        fecha_ingreso = datetime.strptime(
            datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')

        profesor_nuevo = Profesor(
            nombre, dni, sexo, fecha_nacimiento, legajo, fecha_ingreso)
        ITBA.agregar_profesor(profesor_nuevo)

    def bajaAlumno(self):
        legajo_alumno = validadorLegajoAlumnos(ITBA)
        for alumno in ITBA.alumnos:
            if alumno.legajo == legajo_alumno:
                print(ITBA.alumnos)
                ITBA.alumnos.remove(alumno)
                print(ITBA.alumnos)
                print(alumno.carrera.alumnos_actuales)
                alumno.carrera.alumnos_actuales.remove(alumno)
                print(alumno.carrera.alumnos_actuales)
                alumno.fecha_baja = datetime.strptime(
                    datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')

    def bajaProfesor(self):
        flag = False
        legajo_profesor = validadorLegajoAdminyProf(ITBA, "profesor")
        clear()
        for profesor in ITBA.profesores:
            if profesor.legajo == legajo_profesor:
                profesor_elegido = profesor
                profesor_elegido.fecha_baja = datetime.strptime(
                    datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        for carrera in ITBA.carreras:
            for materia in carrera.materias:
                if len(materia.comisiones) != 0:
                    for comision in materia.comisiones:
                        if legajo_profesor == comision.profesor.legajo:
                            flag = True
                            comision.profesor = None
                            print(
                                f"Se ha dado de baja al profesor {profesor_elegido.nombre_apellido} de la Comision {comision.codigo_comision} de la Materia {materia.nombre}")

                if flag:
                    materia.profesores.remove(profesor_elegido)
                    flag = False

        ITBA.profesores.remove(profesor_elegido)

    def bajaAdministrativo(self):
        almacen_tramites = []
        legajo_admin = validadorLegajoAdminyProf(ITBA)
        if legajo_admin == self.legajo:
            print("Usted no se puede dar de baja a si mismo")
        else:
            for administrativo in ITBA.administrativos:
                if legajo_admin == administrativo.legajo:
                    if len(administrativo.tramites_abiertos) != 0:
                        if len(ITBA.administrativos)-1 == 0:
                            print(
                                f"Usted no puede dar de baja al Administrativo {administrativo.nombre_apellido} ya que no hay otro Administrativo que pueda hacer sus tramites pendientes")
                        else:
                            for tramite in administrativo.tramites_abiertos:
                                almacen_tramites.append(tramite)
                            ITBA.administrativos.remove(administrativo)
                            ITBA.legajos_administrativos.remove(legajo_admin)
                            cantidad_administrativos = len(
                                ITBA.administrativos)
                            i_random = random.randint(
                                0, cantidad_administrativos - 1)
                            administrativo_asignado = ITBA.administrativos[i_random]
                            for tramite in almacen_tramites:
                                tramite.administrativo = administrativo_asignado
                                administrativo_asignado.tramites_abiertos.append(
                                    tramite)
                            print(
                                f"El Administrativo ha sido de baja correctamente, sus tramites fueron asignados al Administrativo {administrativo_asignado.nombre_apellido}")
                    else:
                        ITBA.administrativos.remove(administrativo)
                        ITBA.legajos_administrativos.remove(legajo_admin)
                        print("El Administrativo ha sido dado de baja correctamente")

    def crearComision(self):
        contador = 0
        materias_total = []
        flag = True
        print("Materias de la institución\n")
        while flag:
            for carrera in ITBA.carreras:
                for materia in carrera.materias:
                    contador += 1
                    materias_total.append(materia)
                    print(f"{contador}. {materia.codigo_materia} {materia.nombre}")

            print(f"{contador + 1}. Volver")

            opcion_elegida = validador(contador + 1)
            if opcion_elegida == contador + 1:
                flag = False
            else:
                materia_elegida = materias_total[opcion_elegida - 1]
                clear()
                flag = False
                cod_comi = "A"
                if len(materia_elegida.comisiones) != 0:
                    cod_comi = ascii_uppercase[len(materia_elegida.comisiones)]

                print(
                    f"Creación de la comision para {materia_elegida.nombre}\n")
                aula = validadorAula()
                legajo_profesor_asignado = validadorLegajoAdminyProf(
                    ITBA, "profesor")

                for profesor in ITBA.profesores:
                    if profesor.legajo == legajo_profesor_asignado:
                        profesor_asignado = profesor

                dia = validadorDia().upper().replace(" ", "").split(",")
                horario = validadorHorario(dia).replace(" ", "").split(",")
                dia_horario = {"Dia": dia, "Horario": horario}
                clear()

                nueva_comision = Comision(
                    cod_comi, aula, profesor_asignado, dia_horario)

                materia_elegida.comisiones.append(nueva_comision)
                materia_elegida.profesores.append(profesor_asignado)

                print(
                    f"La comision {nueva_comision.codigo_comision} de {materia_elegida.nombre} fue creada correctamente ")

    def estadisticasGenerales():

        armado_menu("ESTADISTICAS GENERALES", ['Alumnos actuales por carrera', 'Rendimiento Alumno', "Volver"], [
                    lambda: Administrativo.alumnosActualesxCarrera(), lambda: Administrativo.histogramaNotasFinalesAlumno()])

    def alumnosActualesxCarrera():
        alumnos = []
        carreras = []
        for carrera in ITBA.carreras:
            c = 0
            carreras.append(carrera.nombre)
            for alumno in carrera.alumnos_actuales:
                c += 1
            alumnos.append(c)
        plt.pie(alumnos, labels=carreras, autopct='%1.1f%%')
        plt.title(label="Alumnos por Carrera")
        plt.show()

    def histogramaNotasFinalesAlumno():
        legajo_alumno = validadorLegajoAlumnos(ITBA)
        for alumno in ITBA.alumnos:
            if alumno.legajo == legajo_alumno:
                alumno_elegido = alumno

        notas = alumno_elegido.historial_academico.values()
        lista_notas = []
        notas_posibles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lista_frecuencias = []
        for nota in notas:
            lista_notas.append(nota)
        c = 0
        for nota in notas_posibles:
            for elemento in lista_notas:
                if nota == elemento:
                    c += 1
            lista_frecuencias.append(c)
            c = 0

        plt.title(f"Rendimiento del alumno {alumno_elegido.nombre_apellido}")
        plt.bar(notas_posibles, lista_frecuencias)
        plt.xticks(notas_posibles)
        plt.ylabel("Frecuencia")
        plt.show()

    def actualizarContraseña(self):
        contraseña_nueva=input("Ingrese su contraseña nueva: ")
        self.contraseña=contraseña_nueva

class Invitado(Persona):

    def __init__(self, nombre_apellido, dni, email, cantidad_de_veces_que_ingresa):
        super().__init__(nombre_apellido, dni)
        self.cantidad_de_veces_que_ingresa = cantidad_de_veces_que_ingresa
        self.email = email

    def registro_invitado(institucion:Institucion):

        f = open("Proyecto/invitados.txt", "r")
        lista_invitados = f.readlines()
        if len(lista_invitados) != 0:
            for invitado in lista_invitados:
                info_invitados = invitado.split(",")
                invitado_creado = Invitado(info_invitados[0],int(info_invitados[1]), info_invitados[2],int(info_invitados[3]))
                if invitado_creado.dni not in institucion.dni_invitados:
                    institucion.dni_invitados.append(invitado_creado.dni)
                    institucion.DniMail.append([])
                if invitado_creado not in institucion.invitados:
                    institucion.invitados.append(invitado_creado)
                    institucion.DniMail[institucion.dni_invitados.index(invitado_creado.dni)].append(invitado_creado.email)
            
            print(institucion.DniMail)


            dni = validadorDNIInvitado()
            email = validadorEmailExistente(dni)

            invitado_localizado = None

            for invitado in institucion.invitados:
                if invitado.dni == dni and invitado.email == email:
                    invitado_localizado = invitado
        
            if invitado_localizado is None:
                print("\n\t\tUSTED NUNCA HA INGRESADO\n")
                nombre_apellido = input("Por ser la primera vez, proveanos su nombre y apellido: ")
                invitado_creado = Invitado(nombre_apellido,dni,email,1)
                institucion.invitados.append(invitado_creado)

            else:
                invitado_localizado.cantidad_de_veces_que_ingresa += 1


        else:
            print("\n\t\tUSTED NUNCA HA INGRESADO\n")
            dni = validadorDNIInvitado()
            email = validadorEmailExistente(dni)
            nombre_apellido = input("Por ser la primera vez, proveanos su nombre y apellido: ")
            invitado_creado = Invitado(nombre_apellido,dni,email,1)
            ITBA.invitados.append(invitado_creado)

        f.close()
        
        print("\n\t\t MENU INVITADO \n")
        opciones = ["Ver Estadisticas", "Cerrar Sesión"]
        contador = 0
        flag = True
        while flag:
            for opcion in opciones:
                contador += 1
                print(f"{contador}. {opcion}")

            opcion_elegida = validador(contador)
            clear()
            if opcion_elegida == contador:
                Invitado.logOutInvitados(ITBA)
                flag = False
            else:
                Administrativo.estadisticasGenerales()
                contador = 0
    

    def __eq__(self, __value) -> bool:
        return self.nombre_apellido == __value.nombre_apellido and self.dni == __value.dni and self.email == __value.email

    def logOutInvitados(institucion:Institucion):

        f=open("Proyecto/invitados.txt","w")
        len_invitados=len(institucion.invitados)
        c = 1
        for invitado in institucion.invitados:
            if c != len_invitados:
                f.write(f"{invitado.nombre_apellido},{invitado.dni},{invitado.email},{invitado.cantidad_de_veces_que_ingresa}\n")
                c += 1
            else:
                f.write(f"{invitado.nombre_apellido},{invitado.dni},{invitado.email},{invitado.cantidad_de_veces_que_ingresa}")
        
        f.close()

    
    def __str__(self):
      return str(self.cantidad_de_veces_que_ingresa)
