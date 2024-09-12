from utilss import  green_color,blue_color
from utilss import gotoxy, BorrarPantalla, linea
from Componets import Menu, Valida
from Estudiante import Estudiante
from ClsJson import JsonFile
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudEstudiante(Icrud):
    json_file = JsonFile(f"{path}/data/estudiantes.json") 
    
    def create(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(27, 2); print(f"{blue_color}Registro de Estudiantes")
        linea(80,green_color)
        
        nombre = Valida.validar_letras(f"{blue_color}Ingrese el nombre del estudiante: {green_color}", 1, 4, 35, 4)
        apellido = Valida.validar_letras(f"{blue_color}Ingrese el apellido del estudiante: {green_color}", 1, 5, 37, 5)
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del estudiante: {green_color}", 1, 6, 32, 6))
        
        estudiante = self.json_file.find('dni', dni)
        if estudiante:
            linea(80,green_color)
            print(f"{blue_color}El estudiante ya se encuentra registrado")
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
            estudiante = Estudiante(nombre, apellido, dni)
            estudiantes = self.json_file.read()
            estudiantes.append(estudiante.getJson())
            self.json_file.save(estudiantes)
            
            linea(80,green_color)
            print(f"{blue_color}Estudiante registrado exitosamente.")
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
        gotoxy(32, 2); print(f"{blue_color}Eliminar Estudiante")
        linea(80,green_color)
        
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del estudiante a eliminar: {green_color}", 1, 4, 43, 4))

        estudiantes = self.json_file.find('dni', dni)

        if estudiantes: 
            estudiante = estudiantes[0]
            linea(80,green_color)
            print(f"{blue_color}Estudiante encontrado")
            print(f"{blue_color}Nombre: {green_color}{estudiante['nombre']}\n{blue_color}Apellido: {green_color}{estudiante['apellido']}\n{blue_color}DNI: {green_color}{estudiante['dni']}")  
            linea(80,green_color)          
            confirmacion = Valida.validar_letras(f"{blue_color}¿Está seguro que desea eliminar este estudiante? (S/N): {green_color}" , 1, 11, 57, 11)

            if confirmacion.lower() == 's':
                estudiante['active'] = False
                estudiantes = self.json_file.read()
                
                for i, est in enumerate(estudiantes):
                    if est['dni'] == estudiante['dni']:
                        estudiantes[i] = estudiante  
                        
                self.json_file.save(estudiantes)
                linea(80,green_color)
                print(f"{blue_color}Estudiante eliminado exitosamente.")
                linea(80,green_color)
                time.sleep(3)
            else:
                linea(80,green_color)  
                print(f"{blue_color}Operación cancelada.")
                linea(80,green_color)
                time.sleep(3)
        else: 
            linea(80,green_color)  
            print(f"{green_color}No se encontró un estudiante con DNI {dni}.")
            linea(80,green_color)
            time.sleep(3)
             
    def update(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(32, 2); print(f"{blue_color}Actualizar Estudiante")
        linea(80,green_color)
        dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del estudiante a actualizar: {green_color}", 1, 4, 45, 4))
        estudiantes = self.json_file.read()
        
        estudiante_existente = None
        for est in estudiantes:
            if est['dni'] == dni and est['active']:
                estudiante_existente = est
                break
        
        if estudiante_existente:
            linea(80,green_color)
            print(f"{blue_color}Estudiante encontrado:\nNombre: {green_color}{estudiante_existente['nombre']}\n{blue_color}Apellido: {green_color}{estudiante_existente['apellido']}\n{blue_color}DNI: {green_color}{estudiante_existente['dni']}")
            linea(80,green_color)
            
            nuevo_nombre = input(f"{blue_color}Ingrese el nuevo nombre del estudiante (deje en blanco para no cambiar): {green_color}")
            nuevo_apellido = input(f"{blue_color}Ingrese el nuevo apellido del estudiante (deje en blanco para no cambiar): {green_color}")

            if nuevo_nombre:
                estudiante_existente['nombre'] = nuevo_nombre.capitalize()
            if nuevo_apellido:
                estudiante_existente['apellido'] = nuevo_apellido.capitalize()

            self.json_file.save(estudiantes)
            
            linea(80,green_color)
            print(f"{green_color}Estudiante actualizado exitosamente.")
            linea(80,green_color)
        else:
            linea(80,green_color)
            print(f"{green_color}No se encontró un estudiante activo con DNI {dni}.")
            linea(80,green_color)
        time.sleep(3)

    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{blue_color}Consultar Estudiantes")
        linea(80, green_color)

        estudiantes = self.json_file.read()

        menu = Menu("Seleccione una opción", ["Listar todos los estudiantes registrados", "Buscar por DNI", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()

        if opc == '1':
            if estudiantes:
                print(f"{blue_color}Estudiantes registrados:")
                for est in estudiantes:
                    if est["active"]: 
                        print(f"{blue_color}Nombre: {green_color}{est['nombre']}\n"
                            f"{blue_color}Apellido: {green_color}{est['apellido']}\n"
                            f"{blue_color}DNI: {green_color}{est['dni']}\n"
                            f"{blue_color}Fecha de registro: {green_color}{est['fecha_creacion']}\n")
                time.sleep(3)
            else:
                print(f"{green_color}No hay estudiantes registrados.")
                linea(80,green_color)
                time.sleep(3)

        elif opc == '2':
            linea(80,green_color)
            dni = str(Valida.validar_dni(f"{blue_color}Ingrese el DNI del estudiante a buscar: {green_color}", 1, 10, 41, 10))
            estudiante = self.json_file.find('dni', dni)
            if estudiante and estudiante[0]["active"]:
                estudiante = estudiante[0]
                linea(80,green_color)
                print(f"{blue_color}Estudiante encontrado:")
                print(f"{blue_color}Nombre: {green_color}{estudiante['nombre']}\n"
                    f"{blue_color}Apellido: {green_color}{estudiante['apellido']}\n"
                    f"{blue_color}DNI: {green_color}{estudiante['dni']}\n"
                    f"{blue_color}Fecha de registro: {green_color}{estudiante['fecha_creacion']}\n")
                time.sleep(3)
            else:
                linea(80,green_color)
                print(f"{green_color}No se encontró un estudiante registrado con DNI {dni}.")
                linea(80,green_color)
                time.sleep(3)
                
        else:
            linea(80,green_color)
            print(f"{green_color}Regresando al menú principal.")
            linea(80,green_color)
            time.sleep(3)
            return