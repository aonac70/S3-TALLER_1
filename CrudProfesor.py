from utilss import  green_color,blue_color
from utilss import gotoxy, BorrarPantalla, linea
from Componets import Menu,Valida
from ClsJson import JsonFile
from Profesor import Profesor
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudProfesor(Icrud):
    json_file = JsonFile(f"{path}/data/profesores.json")
    
    def create(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(32, 2); print(f"{blue_color}Registro de Profesor")
        linea(80,green_color)
        nombre = Valida.validar_letras(f"{blue_color}Ingrese el nombre del profesor: {green_color}",1 , 4, 33, 4)
        apellido = Valida.validar_letras(f"{blue_color}Ingrese el apellido del profesor: {green_color}", 1, 5, 35, 5)
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del profesor: {green_color}", 1, 6, 30, 6))

        profesor = self.json_file.find( 'dni', dni)
        
        if profesor:
            linea(80,green_color)
            print(f"{blue_color}El profesor ya se encuentra registrado")
            print(f"{blue_color}Nombre: {green_color}{nombre}\n{blue_color}Apellido: {green_color}{apellido}\n{blue_color}DNI: {green_color}{dni}")
            linea(80,green_color)
            print(f"{green_color}regresando al menu principal")
            linea(80,green_color)
            time.sleep(4)
            return
        
        linea(80,green_color)
        print(f"{blue_color}Datos ingresados")
        print(f"{blue_color}Nombre: {green_color}{nombre}\n{blue_color}Apellido: {green_color}{apellido}\n{blue_color}DNI: {green_color}{dni}")
        linea(80,green_color)
        confirmacion = Valida.validar_letras(f"{blue_color}¿Los datos ingresados son correctos? (S/N): {green_color}" , 1, 13, 44, 13)
        
        if confirmacion.lower() == 's':
            profesor = Profesor(nombre, apellido, dni)
            profesores = self.json_file.read()
            profesores.append(profesor.getjson())
            self.json_file.save(profesores)
            
            linea(80,green_color)
            print(f"{blue_color}Profesor registrado exitosamente.")
            linea(80,green_color)
            time.sleep(3)
        else:
            linea(80,green_color)
            print(f"{blue_color}Operación cancelada.")
            linea(80,green_color)
            time.sleep(3)
            
    def delete(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(32, 2); print(f"{green_color}Eliminar profesor")
        linea(80,green_color)
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del profesor a eliminar: {green_color}", 1, 4, 42, 4))

        profesores = self.json_file.find('dni', dni)
        
        linea(80,green_color)
        if profesores: 
            profesor = profesores[0]
            print(f"{blue_color}Profesor encontrado:\nNombre: {green_color}{profesor['nombre']}\n{blue_color}Apellido: {green_color}{profesor['apellido']}\n{blue_color}DNI: {green_color}{profesor['dni']}\n Fecha de registro: {green_color}{profesor['fecha_creacion']}")
            linea(80,green_color)
            confirmacion = Valida.validar_letras(f"{blue_color}¿Está seguro que desea eliminar este profesor? (S/N): {green_color}", 1, 12, 54, 12)

            if confirmacion.lower() == 's':
                
                profesor['active'] = False

                profesores = self.json_file.read()
                
                for i, est in enumerate(profesores):
                    if est['dni'] == profesor['dni']:
                        profesores[i] = profesor  

                self.json_file.save(profesores)
                
                linea(80,green_color)
                print(f"{blue_color}profesor eliminado exitosamente.")
                linea(80,green_color)
                time.sleep(3)
            else:
                linea(80,green_color)
                print(f"{blue_color}Operación cancelada.")
                linea(80,green_color)
                time.sleep(3)
        else:
            linea(80,green_color)
            print(f"{blue_color}No se encontró un profesor con DNI {dni}.")
            linea(80,green_color)
            time.sleep(3)
             
    def update(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(32, 2); print(f"{blue_color}Actualizar Profesor")
        linea(80,green_color)
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del a actualizar: {green_color}", 1, 4, 34, 4))
        profesores = self.json_file.read()
        
                
        profesor_existente = None
        for prof in profesores:
            if prof['dni'] == dni:
                profesor_existente = prof
                break
        linea(80,green_color)    
        if profesor_existente and profesor_existente['active']:
            print(f"{blue_color}Profesor encontrado:\nNombre: {green_color}{profesor_existente['nombre']}\n{blue_color}Apellido: {green_color}{profesor_existente['apellido']}\n{blue_color}DNI: {green_color}{profesor_existente['dni']}")
            linea(80,green_color)
            
            nuevo_nombre = input(f"{blue_color}Ingrese el nuevo nombre del profesor (deje en blanco para no cambiar): {green_color}")
            nuevo_apellido = input(f"{blue_color}Ingrese el nuevo apellido del profesor (deje en blanco para no cambiar): {green_color}")

            if nuevo_nombre:
                profesor_existente['nombre'] = nuevo_nombre.capitalize()
            if nuevo_apellido:
                profesor_existente['apellido'] = nuevo_apellido.capitalize()

            self.json_file.save(profesores)
            linea(80,green_color)
            print(f"{blue_color}Profesor actualizado exitosamente.")
            linea(80,green_color)
        else:
            if not profesor_existente:
                print(f"{blue_color}No se encontró un profesor con DNI {dni}.")
                linea(80,green_color)
            else:
                print(f"{blue_color}No se puede actualizar.")
                linea(80,green_color)
        time.sleep(3)

    def consult(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(32, 2); print(f"{blue_color}Consultar Profesores")
        linea(80,green_color)

        profesores = self.json_file.read()

        profesores_activos = []
        for prof in profesores:
            if prof['active']: 
                profesores_activos.append(prof)

        menu = Menu("Seleccione una opcion", ["Listar todos los profesores registrados ", "Buscar por DNI", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()

        if opc == '1':
            if profesores_activos:
                linea(80,green_color)
                print(f"{blue_color}Profesores registrados:")
                for prof in profesores_activos:
                    print(f"{blue_color}Nombre: {green_color}{prof['nombre']}\n{blue_color}Apellido: {green_color}{prof['apellido']}\n{blue_color}DNI: {green_color}{prof['dni']}\n{blue_color}Fecha de registro: {green_color}{prof['fecha_creacion']}\n")
                linea(80,green_color)
                time.sleep(3)
            else:
                
                print(f"{green_color}No hay profesores registrados.")
                
            time.sleep(3)

        elif opc == '2':
            linea(80,green_color)   
            dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del profesor a buscar: {green_color}", 1, 10, 40, 10))
            linea(80,green_color)
            estudiante = None
            for prof in profesores_activos:
                if prof['dni'] == dni:
                    estudiante = prof
                    break      
            print(f"{blue_color}Profesor encontrado:")
            if estudiante:
                print(f"{blue_color}Nombre: {green_color}{prof['nombre']}\n{blue_color}Apellido: {green_color}{prof['apellido']}\n{blue_color}DNI: {green_color}{prof['dni']}\n{blue_color}Fecha de registro: {green_color}{prof['fecha_creacion']}\n")
                linea(80,green_color)
                time.sleep(3)
            else:
                print(f"{blue_color}No se encontró un profesor registrado con DNI {dni}.")
                linea(80,green_color)
                time.sleep(3)
                
        else:
            print(f"{green_color}Regresando al menú principal.")
            linea(80,green_color)
            time.sleep(3)
            return

      