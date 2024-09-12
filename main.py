from utilss import reset_color, green_color, blue_color
from utilss import BorrarPantalla, gotoxy
from CrudAsignatura import CrudAsignatura
from CrudEstudiante import CrudEstudiante
from CrudNivel import CrudNivel
from CrudPeriodo import CrudPeriodo
from CrudProfesor import CrudProfesor
from CrudNota import CrudNota
from CrudTemaTesis import CrudTemaTesis
from Componets import Menu
import time

opc = ''
while opc != '8':
    BorrarPantalla()
    menu_main = Menu("Menu Principal", ["Gestion de Periodos", "Gestion de Nivel", "Gestion de Asignaturas", "Gestion de Profesores", "Gestion de Estudiantes", "Gestion de Tesis", "Gestion de Notas", "Salir"], color=green_color, color_numeros=blue_color)
    opc = menu_main.menu()
    if opc == '1':
        opc1 = ''
        while opc1 != '8':
            BorrarPantalla()
            menu_periodo = Menu("Menu Periodo", ["Registrar Periodo", "Eliminar Periodo", "Actualizar Periodo", "Mostrar Periodos", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc1 = menu_periodo.menu()
            crud = CrudPeriodo()
            if opc1 == '1':
                crud.create()
            elif opc1 == '2':
                crud.delete()
            elif opc1 == '3':
                crud.update()
            elif opc1 == '4':
                crud.consult()
            elif opc1 == '5':
                print("Regresando al menu principal")
    elif opc == '2':
        opc2 = ''
        while opc2 != '8':
            BorrarPantalla()
            menu_nivel = Menu("Menu Nivel", ["Registrar Nivel", "Eliminar Nivel", "Actualizar Nivel", "Mostrar Niveles", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc2 = menu_nivel.menu()
            crud = CrudNivel()
            if opc2 == '1':
                crud.create()
            elif opc2 == '2':
                crud.delete()
            elif opc2 == '3':
                crud.update()
            elif opc2 == '4':
                crud.consult()
            elif opc2 == '5':
                print("Regresando al menu principal")
    elif opc == '3':
        opc3 = ''
        while opc3 != '8':
            BorrarPantalla()
            menu_asignatura = Menu("Menu Asignatura", ["Registrar Asignatura", "Eliminar Asignatura", "Actualizar Asignatura", "Mostrar Asignaturas", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc3 = menu_asignatura.menu()
            crud = CrudAsignatura()
            if opc3 == '1':
                crud.create()
            elif opc3 == '2':
                crud.delete()
            elif opc3 == '3':
                crud.update()
            elif opc3 == '4':
                crud.consult()
            elif opc3 == '5':
                print("Regresando al menu principal")
    elif opc == '4':
        opc4 = ''
        while opc4 != '8':
            BorrarPantalla()
            menu_profesor = Menu("Menu Profesor", ["Registrar Profesor", "Eliminar Profesor", "Actualizar Profesor", "Mostrar Profesores", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc4 = menu_profesor.menu()
            crud = CrudProfesor()
            if opc4 == '1':
                crud.create()
            elif opc4 == '2':
                crud.delete()
            elif opc4 == '3':
                crud.update()
            elif opc4 == '4':
                crud.consult()
            elif opc4 == '5':
                print("Regresando al menu principal")
    elif opc == '5':
        opc5 = ''
        while opc5 != '9':
            BorrarPantalla()
            menu_estudiante = Menu("Menu Estudiante", ["Registrar Estudiante", "Eliminar Estudiante", "Actualizar Estudiante", "Consultar Estudiantes", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc5 = menu_estudiante.menu()
            crud = CrudEstudiante()
            if opc5 == '1':
                crud.create()
            elif opc5 == '2':
                crud.delete()
            elif opc5 == '3':
                crud.update()
            elif opc5 == '4':
                crud.consult()
            elif opc5 == '5':
                print("Regresando al menu principal")
    elif opc == '6':
        opc2 = ''
        while opc2 != '8':
            BorrarPantalla()
            menu_Tesis = Menu("Menu Tema de tesis", ["Registrar Tesis", "Eliminar Tesis", "Actualizar Tesis", "Mostrar Tesis", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc2 = menu_Tesis.menu()
            crud = CrudTemaTesis()
            if opc6 == '1':
                crud.create()
            elif opc6 == '2':
                crud.delete()
            elif opc6 == '3':
                crud.update()
            elif opc6 == '4':
                crud.consult()
            elif opc6 == '5':
                print("Regresando al menu principal")
    elif opc == '7':
        opc7 = ''
        while opc7 != '8':
            BorrarPantalla()
            menu_nota = Menu("Menu Nota", ["Registrar Nota", "Eliminar Nota", "Actualizar Nota", "Mostrar Notas", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc7 = menu_nota.menu()
            crud = CrudNota()
            if opc7 == '1':
                crud.create()
            elif opc7 == '2':
                crud.delete()
            elif opc7 == '3':
                crud.update()
            elif opc7 == '4':
                crud.consult()
            elif opc7 == '5':
                print("Regresando al menu principal")
    # elif opc == '7':
    #     opc6 = ''
    #     while opc6 != '5':
    #         BorrarPantalla()
    #         menu_nota = Menu("Menu Nota", ["Registrar ", "Eliminar ", "Actualizar ", "Mostrar ", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
    #         opc6 = menu_nota.menu()
    #         crud = CrudNota()
    #         if opc6 == '1':
    #             crud.create()
    #         elif opc6 == '2':
    #             crud.delete()
    #         elif opc6 == '3':
    #             crud.update()
    #         elif opc6 == '4':
    #             crud.consult()
    #         elif opc6 == '5':
    #             print("Regresando al menu principal")
    print("Regresando al menu principal")
BorrarPantalla()
input("Gracias por usar el sistema, presione una tecla para salir...")
BorrarPantalla()
