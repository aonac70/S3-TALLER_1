from utilss import green_color, blue_color, purple_color, gotoxy, BorrarPantalla, linea
from Componets import Menu
from ClsJson import JsonFile
from Asignatura import Asignatura
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudAsignatura(Icrud):
    json_file_niveles = JsonFile(f"{path}/data/niveles.json")
    json_file = JsonFile(f"{path}/data/asignaturas.json")
    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(20, 2)
        print("Registro de Asignaturas")
        linea(80, green_color)

        Asignaturas = self.json_file.read()

        if Asignaturas:
            next_id = max(n['id'] for n in Asignaturas) + 1
        else:
            next_id = 1

        descripcion = input(f"{blue_color}Ingrese el nombre de la asignatura: {purple_color}")

        descripcion_existente = self.json_file.find('descripcion', descripcion)

        if len(descripcion_existente) > 0:
            print(f"{purple_color}La asignatura ya existe")
            time.sleep(2)
            return
        else:
            niveles = self.json_file_niveles.read()
            
            if niveles:
                for nivel in niveles:
                    if nivel["active"]:
                        print(f"{blue_color}ID: {nivel['id']} Nivel: {nivel['nivel']}") 
                
                id_nivel = int(input(f"{blue_color}Ingrese el ID del nivel: {purple_color}"))
                
                nivel_existente = self.json_file_niveles.find('id', id_nivel)
                
                if len(nivel_existente) > 0:
                    n_asignatura = Asignatura(next_id, descripcion, nivel_existente[0])
                    Asignaturas.append(n_asignatura.getJson())
                    self.json_file.save(Asignaturas)
                    print(f"{purple_color}Asignatura guardada correctamente")
                    time.sleep(2)
                else:
                    print(f"{purple_color}El nivel no existe")
                    time.sleep(2)
            else:
                print(f"{purple_color}No hay niveles registrados")
                time.sleep(2)
        
    def update(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(20,2);print("Actualizar Asignatura")
        linea(80,green_color)
        
        menu = Menu("Menu Asignatura", ["Actualizar Descripcion", "Actualizar Nivel", "Volver"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            id = int(input(f"{blue_color}Ingrese el ID de la asignatura a actualizar: {purple_color}"))
            
            Asignaturas = self.json_file.read()
            
            asignatura_encontrada = False
            for asignatura in Asignaturas:
                if asignatura["id"] == id and asignatura["active"]:
                    asignatura_encontrada = True
                    print(f"{blue_color}Asignatura encontrada: {purple_color}{asignatura['descripcion']}")
                    nueva_descripcion = input(f"{blue_color}Ingrese la nueva descripcion de la asignatura: {purple_color}")
                    
                    duplicado = self.json_file.find('descripcion', nueva_descripcion)
                    
                    if len(duplicado) > 0:
                        print(f"{purple_color}La asignatura ya existe")
                        time.sleep(2)
                        return
                    
                    confirmacion = input(f"{blue_color}¿Está seguro de actualizar la asignatura? s/n: {purple_color}")
                    if confirmacion.lower() == 's':
                        asignatura["descripcion"] = nueva_descripcion
                        self.json_file.save(Asignaturas)
                        print(f"{purple_color}Asignatura actualizada correctamente")
                        time.sleep(2)
                    else:
                        print(f"{purple_color}No se actualizó la asignatura")
                        time.sleep(2)
                    break
            
            if not asignatura_encontrada:
                print(f"{purple_color}La asignatura no existe o no está activa")
                time.sleep(2)
        elif opc == '2':
            id = int(input(f"{blue_color}Ingrese el ID de la asignatura a actualizar: {purple_color}"))
            
            Asignaturas = self.json_file.read()
            
            asignatura_encontrada = False
            for asignatura in Asignaturas:
                if asignatura["id"] == id and asignatura["active"]:
                    asignatura_encontrada = True
                    print(f"{blue_color}Asignatura encontrada: {purple_color}{asignatura['descripcion']}")
                    
                    niveles = self.json_file_niveles.read()
                    for nivel in niveles:
                        if nivel["active"]:
                            print(f"{blue_color}ID: {nivel['id']} Nivel: {nivel['nivel']}")
                    
                    id_nivel = int(input(f"{blue_color}Ingrese el ID del nivel: {purple_color}"))
                    
                    nivel_existente = self.json_file_niveles.find('id', id_nivel)
                    
                    if len(nivel_existente) > 0:
                        asignatura["nivel"] = nivel_existente[0]
                        self.json_file.save(Asignaturas)
                        print(f"{purple_color}Asignatura actualizada correctamente")
                        time.sleep(2)
                    else:
                        print(f"{purple_color}El nivel no existe")
                        time.sleep(2)
                    break
            
            if not asignatura_encontrada:
                print(f"{purple_color}La asignatura no existe o no está activa")
                time.sleep(2)
        elif opc == '3':
            print(f"{purple_color}Regresando al menu principal")
            time.sleep(2)
            return
        
    def delete(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(30,2);print(f"{purple_color}Eliminar Asignatura")
        linea(80,green_color)
        
        id = int(input(f"{blue_color}Ingrese el ID de la asignatura a eliminar: {purple_color}"))
        
        Asignaturas = self.json_file.read()
        linea(80,green_color)
        asignatura_encontrada = False
        for asignatura in Asignaturas:
            if asignatura["id"] == id and asignatura["active"]:
                asignatura_encontrada = True
                print(f"{blue_color}Asignatura encontrada:\n{blue_color}ID: {purple_color}{asignatura['id']}\n{blue_color}Descripcion: {purple_color}{asignatura['descripcion']}\n{blue_color}Nivel: {purple_color}{asignatura['nivel']['nivel']}")
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar la asignatura? s/n: {purple_color}")
                if confirmacion.lower() == 's':
                    asignatura["active"] = False
                    self.json_file.save(Asignaturas)
                    linea(80,green_color)
                    print(f"{purple_color}Asignatura eliminada correctamente")
                    linea(80,green_color)
                    time.sleep(2)
                else:
                    linea(80,green_color)
                    print(f"{purple_color}No se eliminó la asignatura")
                    linea(80,green_color)
                    time.sleep(2)
                break
        
        if not asignatura_encontrada:
            linea(80,green_color)
            print(f"{purple_color}La asignatura no existe o no está activa")
            linea(80,green_color)
            time.sleep(2)

    def consult(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(30,2);print(f"{purple_color}Consultar Asignaturas")
        linea(80,green_color)
        
        Asignaturas = self.json_file.read()
        
        menu = Menu("Menu Asignatura", ["Mostrar Todas", "Mostrar por ID", "Volver al menu principal"], color=purple_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            linea(80,green_color)
            print(f"{purple_color}Mostrar Todas las Asignaturas")
            linea(80,green_color)
            for asignatura in Asignaturas:
                if asignatura["active"]:
                    print(f"{blue_color}ID: {purple_color}{asignatura['id']}\n{blue_color}Descripcion: {purple_color}{asignatura['descripcion']}\n{blue_color}Nivel: {purple_color}{asignatura['nivel']['nivel']}\n")
            time.sleep(5)
        elif opc == '2':
            print(f"{purple_color}Mostrar asignatura por ID")

            id = int(input(f"{blue_color}Ingrese el ID de la asignatura a mostrar: {purple_color}"))
            asignatura_encontrada = False
            for asignatura in Asignaturas:
                if asignatura["id"] == id and asignatura["active"]:
                    asignatura_encontrada = True
                    print(f"{blue_color}Asignatura encontrada:\n{blue_color}ID: {purple_color}{asignatura['id']}\n{blue_color}Descripcion: {purple_color}{asignatura['descripcion']}\n{blue_color}Nivel: {purple_color}{asignatura['nivel']['nivel']}")
                    break
            if not asignatura_encontrada:
                print(f"{purple_color}La asignatura no existe o no está activa")
            time.sleep(5)
        elif opc == '3':
            print(f"{purple_color}Regresando al menu principal")
            time.sleep(2)
            return
        