from utilss import green_color, blue_color, purple_color, gotoxy, BorrarPantalla, linea
from Componets import Menu
from ClsJson import JsonFile
from Profesor import Profesor
from Estudiante import Estudiante
from Asignatura import Asignatura
from Periodo import Periodo
from Nota import Nota, DetalleNota
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudNota(Icrud):
    json_file = JsonFile(f"{path}/data/asignaturas.json")
    json_file_estudiantes = JsonFile(f"{path}/data/estudiantes.json")
    json_file_periodos = JsonFile(f"{path}/data/periodos.json")
    json_file_notas = JsonFile(f"{path}/data/notas.json")
    json_file_profesores = JsonFile(f"{path}/data/profesores.json")
    
    def create(self):
        BorrarPantalla()   
        linea(80, green_color)
        gotoxy(27, 2), print(f"{blue_color}Registro de Notas")
        linea(80, green_color)

        notas = self.json_file_notas.read()
        next_id = max(n['id'] for n in notas) + 1 if notas else 1

        gotoxy(1, 4), print(f"{blue_color}Nota ID:{green_color}{next_id} ")
        gotoxy(40, 4), print(f"{blue_color}Fecha:{green_color}{time.strftime('%d-%m-%Y')}")
        gotoxy(1, 5), print(f"{blue_color}profesor:{green_color} ")
        gotoxy(1, 6), print(f"{blue_color}asignatura: {green_color} ")
        gotoxy(40, 6), print(f"{blue_color}Periodo: ")
        
        gotoxy(11, 5)
        dni_profesor = input(f"{green_color}")
        profesor_data = self.json_file_profesores.find('dni', dni_profesor)
        
        if profesor_data:
            profesor_dict = profesor_data[0]
            if profesor_dict["active"]:
                gotoxy(11, 5)
                print(f"{green_color}{profesor_dict['nombre']} {profesor_dict['apellido']}")
            else:
                gotoxy(11, 5)
                print(f"{green_color}El profesor no está activo")
                time.sleep(1)
                return
        else:
            gotoxy(15, 5)
            print(f"{green_color}El profesor no existe")
            time.sleep(1)
            return
        
        gotoxy(13, 6)
        id_asignatura = int(input(f"{green_color}"))
        asignatura_data = self.json_file.find('id', id_asignatura)
        
        if asignatura_data:
            asignatura_dict = asignatura_data[0]
            if asignatura_dict["active"]:
                gotoxy(13, 6)
                print(f"{green_color}{asignatura_dict['descripcion']}")
            else:
                gotoxy(13, 6)
                print(f"{green_color}La asignatura no está activa")
                time.sleep(2)
                return
        else:
            gotoxy(16, 6)
            print(f"{green_color}La asignatura no existe")
            time.sleep(2)
            return
        
        gotoxy(49, 6)
        id_periodo = int(input(f"{green_color}"))
        periodo_data = self.json_file_periodos.find('id', id_periodo)
        
        if periodo_data:
            periodo_dict = periodo_data[0]
            if periodo_dict["active"]:
                gotoxy(49, 6), print(f"{green_color}{periodo_dict['periodo']}")
            else:
                gotoxy(49, 6), print(f"{green_color}El periodo no está activo")
                time.sleep(2)
                return
        else:
            gotoxy(49,6), print(f"{green_color}El periodo no existe")
            time.sleep(2)
            return
        
        nota = Nota(next_id, periodo_dict, profesor_dict, asignatura_dict)
        
        linea(80, green_color)
        gotoxy(27, 8)
        print(f"{blue_color}Detalle de Notas")
        linea(80, green_color)
        gotoxy(1, 10), print(f"{blue_color}DNI")
        gotoxy(15, 10), print(f"{blue_color}Estudiante")
        gotoxy(40, 10), print(f"{blue_color}Nota 1")
        gotoxy(50, 10), print(f"{blue_color}Nota 2")
        gotoxy(60, 10), print(f"{blue_color}Recuperación")
        gotoxy(75, 10), print(f"{blue_color}Promedio")
        gotoxy(85, 10), print(f"{blue_color}Observación")

        fila = 12
        while True:
            gotoxy(1, fila)
            dni_estudiante = input(f"{green_color}")
            estudiante_data = self.json_file_estudiantes.find('dni', dni_estudiante)
            
            if estudiante_data:
                estudiante_dict = estudiante_data[0]
                if estudiante_dict["active"]:
                    gotoxy(15, fila), print(f"{purple_color}{estudiante_dict['nombre']} {estudiante_dict['apellido']}")
                else:
                    gotoxy(15, fila), print(f"{purple_color}El estudiante no está activo")
                    time.sleep(2)
                    continue
            else:
                gotoxy(15, fila), print(f"{purple_color}El estudiante no existe")
                time.sleep(2)
                continue
            
            gotoxy(40, fila)
            nota1 = float(input())
            gotoxy(50, fila)
            nota2 = float(input())
            gotoxy(60, fila)
            recuperacion_input = input()

            recuperacion = float(recuperacion_input) if recuperacion_input else None

            detalle_nota = DetalleNota(next_id, estudiante_dict, nota1, nota2, recuperacion)
            nota.detalle_notas.append(detalle_nota)

            promedio = (nota1 + nota2) / 2
            if recuperacion is not None:
                promedio = max(promedio, recuperacion)

            observacion = "Aprobado" if promedio >= 70 else "Reprobado"
            recuperacion_texto = f"{recuperacion:.2f}" if recuperacion is not None else "N/A"

            gotoxy(1, fila)
            print(f"{dni_estudiante:<13} {estudiante_dict['nombre'] + ' ' + estudiante_dict['apellido']:<25} {nota1:<8.2f} {nota2:<8.2f} {recuperacion_texto:<12} {promedio:<8.2f} {observacion:<10}")
            fila += 1
            
            gotoxy(1, fila + 2)  
            continuar = input(f"{blue_color}¿Desea ingresar notas para otro estudiante? (S/N): {purple_color}")
            if continuar.lower() != 's':
                break
            gotoxy(1, fila + 2)
            print(" " * 80) 
            
        print(f"(Notas registradas exitosamente)")
        time.sleep(2)
        print(" " * 80) 
        notas = self.json_file_notas.read()
        notas.append(nota.getJson())
        self.json_file_notas.save(notas)
        
    def update(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(27, 2), print(f"{blue_color}Actualizar Notas")
        linea(80, green_color)

        notas = self.json_file_notas.read()
        
        gotoxy(1, 4), print(f"{blue_color}Ingrese el ID de la nota a actualizar: {green_color}")
        nota_id = int(input())

        nota_data = next((n for n in notas if n['id'] == nota_id), None)
        
        if nota_data:
            gotoxy(1, 6), print(f"{blue_color}Profesor: {green_color}{nota_data['profesor']['nombre']} {nota_data['profesor']['apellido']}")
            gotoxy(1, 7), print(f"{blue_color}Asignatura: {green_color}{nota_data['asignatura']['descripcion']}")
            gotoxy(1, 8), print(f"{blue_color}Periodo: {green_color}{nota_data['periodo']['periodo']}")
            linea(80, green_color)
            
            gotoxy(1, 10), print(f"{blue_color}DNI")
            gotoxy(15, 10), print(f"{blue_color}Estudiante")
            gotoxy(40, 10), print(f"{blue_color}Nota 1")
            gotoxy(50, 10), print(f"{blue_color}Nota 2")
            gotoxy(60, 10), print(f"{blue_color}Recuperación")
            gotoxy(75, 10), print(f"{blue_color}Promedio")
            gotoxy(85, 10), print(f"{blue_color}Observación")
            linea(80, green_color)
            
            fila = 12
            for detalle in nota_data['detalle_notas']:
                gotoxy(1, fila), print(f"{green_color}{detalle['estudiante']['dni']}")
                gotoxy(15, fila), print(f"{green_color}{detalle['estudiante']['nombre']} {detalle['estudiante']['apellido']}")
                gotoxy(40, fila), print(f"{green_color}{detalle['nota1']}")
                gotoxy(50, fila), print(f"{green_color}{detalle['nota2']}")
                gotoxy(60, fila), print(f"{green_color}{detalle['recuperacion'] if detalle['recuperacion'] else 'N/A'}")

                gotoxy(40, fila), print(f"{blue_color}")
                nueva_nota1 = float(input("Nueva Nota 1 (dejar vacío para no cambiar): ") or detalle['nota1'])
                gotoxy(50, fila), print(f"{blue_color}")
                nueva_nota2 = float(input("Nueva Nota 2 (dejar vacío para no cambiar): ") or detalle['nota2'])
                gotoxy(60, fila), print(f"{blue_color}")
                nueva_recuperacion = input("Nueva Recuperación (dejar vacío para no cambiar): ")
                nueva_recuperacion = float(nueva_recuperacion) if nueva_recuperacion else detalle['recuperacion']

                detalle['nota1'] = nueva_nota1
                detalle['nota2'] = nueva_nota2
                detalle['recuperacion'] = nueva_recuperacion

                promedio = (nueva_nota1 + nueva_nota2) / 2
                if nueva_recuperacion is not None:
                    promedio = max(promedio, nueva_recuperacion)

                detalle['promedio'] = promedio
                detalle['observacion'] = "Aprobado" if promedio >= 70 else "Reprobado"

                gotoxy(40, fila), print(f"{green_color}{nueva_nota1:<8.2f}")
                gotoxy(50, fila), print(f"{green_color}{nueva_nota2:<8.2f}")
                gotoxy(60, fila), print(f"{green_color}{nueva_recuperacion if nueva_recuperacion else 'N/A':<12}")
                gotoxy(75, fila), print(f"{green_color}{promedio:<8.2f}")
                gotoxy(85, fila), print(f"{green_color}{detalle['observacion']:<10}")

                fila += 2

            self.json_file_notas.save(notas)
            gotoxy(1, fila + 2), print(f"{blue_color}Nota actualizada exitosamente")
            time.sleep(2)
        else:
            gotoxy(1, 6), print(f"{green_color}La nota con ID {nota_id} no existe.")
            time.sleep(2)

    def delete(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(27, 2), print(f"{blue_color}Eliminar Nota")
        linea(80, green_color)

        notas = self.json_file_notas.read()

        if not notas:
            gotoxy(1, 4), print(f"{green_color}No hay notas registradas.")
            time.sleep(2)
            return

        gotoxy(1, 4), print(f"{blue_color}Ingrese el ID de la nota a eliminar: {green_color}")
        nota_id = int(input())

        nota_data = next((n for n in notas if n['id'] == nota_id), None)

        if nota_data:
            gotoxy(1, 6), print(f"{blue_color}ID Nota: {green_color}{nota_data['id']}")
            gotoxy(1, 7), print(f"{blue_color}Fecha: {green_color}{nota_data['fecha_creacion']}")
            gotoxy(1, 8), print(f"{blue_color}Profesor: {green_color}{nota_data['profesor']['nombre']} {nota_data['profesor']['apellido']}")
            gotoxy(1, 9), print(f"{blue_color}Asignatura: {green_color}{nota_data['asignatura']['descripcion']}")
            gotoxy(1, 10), print(f"{blue_color}Periodo: {green_color}{nota_data['periodo']['periodo']}")
            linea(80, green_color)

            gotoxy(1, 12), print(f"{blue_color}DNI")
            gotoxy(15, 12), print(f"{blue_color}Estudiante")
            gotoxy(40, 12), print(f"{blue_color}Nota 1")
            gotoxy(50, 12), print(f"{blue_color}Nota 2")
            gotoxy(60, 12), print(f"{blue_color}Recuperación")
            gotoxy(75, 12), print(f"{blue_color}Promedio")
            gotoxy(85, 12), print(f"{blue_color}Observación")

            fila = 14
            for detalle in nota_data['detalle_notas']:
                recuperacion_texto = f"{detalle['recuperacion']:.2f}" if detalle['recuperacion'] else "N/A"
                
                gotoxy(1, fila), print(f"{green_color}{detalle['estudiante']['dni']}")
                gotoxy(15, fila), print(f"{green_color}{detalle['estudiante']['nombre']} {detalle['estudiante']['apellido']}")
                gotoxy(40, fila), print(f"{green_color}{detalle['nota1']:<8.2f}")
                gotoxy(50, fila), print(f"{green_color}{detalle['nota2']:<8.2f}")
                gotoxy(60, fila), print(f"{green_color}{recuperacion_texto:<12}")
                gotoxy(75, fila), print(f"{green_color}{detalle['promedio']:<8.2f}")
                gotoxy(85, fila), print(f"{green_color}{detalle['observacion']:<10}")
                linea(80, green_color)

                fila += 2
            
            gotoxy(1, fila + 2), print(f"{blue_color}¿Está seguro que desea eliminar esta nota? (S/N): {green_color}")
            confirmacion = input().lower()

            if confirmacion == 's':
                notas = [n for n in notas if n['id'] != nota_id]
                self.json_file_notas.save(notas)
                gotoxy(1, fila + 4), print(f"{green_color}Nota eliminada exitosamente.")
            else:
                gotoxy(1, fila + 4), print(f"{green_color}Operación cancelada.")
        else:
            gotoxy(1, 6), print(f"{green_color}La nota con ID {nota_id} no existe.")
        
        time.sleep(2)

    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(27, 2), print(f"{blue_color}Consulta de Notas")
        linea(80, green_color)

        notas = self.json_file_notas.read()
        
        if not notas:
            gotoxy(1, 4), print(f"{green_color}No hay notas registradas.")
            time.sleep(2)
            return
        
        gotoxy(1, 4), print(f"{blue_color}Ingrese el ID de la nota a consultar: {green_color}")
        nota_id = int(input())

        nota_data = next((n for n in notas if n['id'] == nota_id), None)

        if nota_data:
            gotoxy(1, 6), print(f"{blue_color}ID Nota: {green_color}{nota_data['id']}")
            gotoxy(1, 7), print(f"{blue_color}Fecha: {green_color}{nota_data['fecha_creacion']}")
            gotoxy(1, 8), print(f"{blue_color}Profesor: {green_color}{nota_data['profesor']['nombre']} {nota_data['profesor']['apellido']}")
            gotoxy(1, 9), print(f"{blue_color}Asignatura: {green_color}{nota_data['asignatura']['descripcion']}")
            gotoxy(1, 10), print(f"{blue_color}Periodo: {green_color}{nota_data['periodo']['periodo']}")
            linea(80, green_color)

            gotoxy(1, 12), print(f"{blue_color}DNI")
            gotoxy(15, 12), print(f"{blue_color}Estudiante")
            gotoxy(40, 12), print(f"{blue_color}Nota 1")
            gotoxy(50, 12), print(f"{blue_color}Nota 2")
            gotoxy(60, 12), print(f"{blue_color}Recuperación")
            gotoxy(75, 12), print(f"{blue_color}Promedio")
            gotoxy(85, 12), print(f"{blue_color}Observación")

            fila = 14
            for detalle in nota_data['detalle_notas']:
                recuperacion_texto = f"{detalle['recuperacion']:.2f}" if detalle['recuperacion'] else "N/A"
                
                gotoxy(1, fila), print(f"{green_color}{detalle['estudiante']['dni']}")
                gotoxy(15, fila), print(f"{green_color}{detalle['estudiante']['nombre']} {detalle['estudiante']['apellido']}")
                gotoxy(40, fila), print(f"{green_color}{detalle['nota1']:<8.2f}")
                gotoxy(50, fila), print(f"{green_color}{detalle['nota2']:<8.2f}")
                gotoxy(60, fila), print(f"{green_color}{recuperacion_texto:<12}")
                gotoxy(75, fila), print(f"{green_color}{detalle['promedio']:<8.2f}")
                gotoxy(85, fila), print(f"{green_color}{detalle['observacion']:<10}")

                fila += 2
            gotoxy(1, fila + 2), print(f"{blue_color}Presione cualquier tecla para volver al menú principal...")
            input()
        else:
            gotoxy(1, 6), print(f"{green_color}La nota con ID {nota_id} no existe.")
            time.sleep(2)
