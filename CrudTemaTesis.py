from utilss import green_color, blue_color, purple_color, gotoxy, BorrarPantalla, linea
from Componets import Menu
from ClsJson import JsonFile
from Tesis import Tesis
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudTemaTesis(Icrud):
    json_file = JsonFile(f"{path}/data/tesis.json")
    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(20, 2)
        print("Registro de Tesis")
        linea(80, green_color)

        tesis = self.json_file.read()

        if tesis:
            next_id = max(n['id'] for n in tesis) + 1
        else:
            next_id = 1

        descripcion = input(f"{blue_color}Ingrese el nombre de la Tesis: {purple_color}")

        descripcion_existente = self.json_file.find('descripcion', descripcion)

        if len(descripcion_existente) > 0:
            print(f"{purple_color}La tesis ya existe")
            time.sleep(2)
            return
        else:
            tesis = self.json_file_tesis.read()
            
            if Tesis:
                for Tesis in Tesis:
                    if Tesis["active"]:
                        print(f"{blue_color}ID: {Tesis['id']} Nivel: {Tesis['tesis']}") 
                
                id_tesis = int(input(f"{blue_color}Ingrese el ID de la tesis: {purple_color}"))
                
                Tesis_existente = self.json_file_tesis.find('id', id_tesis)
                
                if len(Tesis_existente) > 0:
                    n_tesis = tesis(next_id, descripcion, Tesis_existente[0])
                    tesis.append(n_tesis.getJson())
                    self.json_file.save(tesis)
                    print(f"{purple_color}Tesis guardada correctamente")
                    time.sleep(2)
                else:
                    print(f"{purple_color}La tesis no existe")
                    time.sleep(2)
            else:
                print(f"{purple_color}No hay tesis registrados")
                time.sleep(2)
        
    def update(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(20,2);print("Actualizar Asignatura")
        linea(80,green_color)
        
        menu = Menu("Menu tesis", ["Actualizar Descripcion", "Actualizar Tesis", "Volver"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            id = int(input(f"{blue_color}Ingrese el ID de la tesis a actualizar: {purple_color}"))
            
            Tesis = self.json_file.read()
            
            Tesis_encontrada = False
            for Tesis in Tesis:
                if Tesis["id"] == id and Tesis["active"]:
                    Tesis_encontrada = True
                    print(f"{blue_color}Tesis encontrada: {purple_color}{Tesis['descripcion']}")
                    nueva_descripcion = input(f"{blue_color}Ingrese la nueva descripcion de la tesis: {purple_color}")
                    
                    duplicado = self.json_file.find('descripcion', nueva_descripcion)
                    
                    if len(duplicado) > 0:
                        print(f"{purple_color}La tesis ya existe")
                        time.sleep(2)
                        return
                    
                    confirmacion = input(f"{blue_color}¿Está seguro de actualizar la tesis? s/n: {purple_color}")
                    if confirmacion.lower() == 's':
                        Tesis["descripcion"] = nueva_descripcion
                        self.json_file.save(Tesis)
                        print(f"{purple_color}Tesis actualizada correctamente")
                        time.sleep(2)
                    else:
                        print(f"{purple_color}No se actualizó la tesis")
                        time.sleep(2)
                    break
            
            if not Tesis_encontrada:
                print(f"{purple_color}La tesis no existe o no está activa")
                time.sleep(2)
        elif opc == '2':
            id = int(input(f"{blue_color}Ingrese el ID de la tesis a actualizar: {purple_color}"))
            
            Tesis = self.json_file.read()
            
            Tesis_encontrada = False
            for Tesis in Tesis:
                if Tesis["id"] == id and Tesis["active"]:
                    Tesis_encontrada = True
                    print(f"{blue_color}Tesis encontrada: {purple_color}{Tesis['descripcion']}")
                    
                    niveles = self.json_file_niveles.read()
                    for nivel in niveles:
                        if nivel["active"]:
                            print(f"{blue_color}ID: {nivel['id']} Nivel: {nivel['nivel']}")
                    
                    id_nivel = int(input(f"{blue_color}Ingrese el ID del nivel: {purple_color}"))
                    
                    nivel_existente = self.json_file_niveles.find('id', id_nivel)
                    
                    if len(nivel_existente) > 0:
                        Tesis["nivel"] = nivel_existente[0]
                        self.json_file.save(Tesis)
                        print(f"{purple_color}Tesis actualizada correctamente")
                        time.sleep(2)
                    else:
                        print(f"{purple_color}El nivel no existe")
                        time.sleep(2)
                    break
            
            if not Tesis_encontrada:
                print(f"{purple_color}La tesis no existe o no está activa")
                time.sleep(2)
        elif opc == '3':
            print(f"{purple_color}Regresando al menu principal")
            time.sleep(2)
            return
        
    def delete(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(30,2);print(f"{purple_color}Eliminar tesis")
        linea(80,green_color)
        
        id = int(input(f"{blue_color}Ingrese el ID de la tesis a eliminar: {purple_color}"))
        
        Tesis = self.json_file.read()
        linea(80,green_color)
        Tesis_encontrada = False
        for Tesis in Tesis:
            if Tesis["id"] == id and Tesis["active"]:
                Tesis_encontrada = True
                print(f"{blue_color}Tesis encontrada:\n{blue_color}ID: {purple_color}{Tesis['id']}\n{blue_color}Descripcion: {purple_color}{Tesis['descripcion']}\n{blue_color}Nivel: {purple_color}{Tesis['nivel']['nivel']}")
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar la tesis? s/n: {purple_color}")
                if confirmacion.lower() == 's':
                    Tesis["active"] = False
                    self.json_file.save(Tesis)
                    linea(80,green_color)
                    print(f"{purple_color}Tesis eliminada correctamente")
                    linea(80,green_color)
                    time.sleep(2)
                else:
                    linea(80,green_color)
                    print(f"{purple_color}No se eliminó la tesis")
                    linea(80,green_color)
                    time.sleep(2)
                break
        
        if not Tesis_encontrada:
            linea(80,green_color)
            print(f"{purple_color}La tesis no existe o no está activa")
            linea(80,green_color)
            time.sleep(2)

    def consult(self):
        BorrarPantalla()
        linea(80,green_color)
        gotoxy(30,2);print(f"{purple_color}Consultar tesis")
        linea(80,green_color)
        
        Tesis = self.json_file.read()
        
        menu = Menu("Menu tesis", ["Mostrar Todas", "Mostrar por ID", "Volver al menu principal"], color=purple_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            linea(80,green_color)
            print(f"{purple_color}Mostrar Todas las Asignaturas")
            linea(80,green_color)
            for Tesis in Tesis:
                if Tesis["active"]:
                    print(f"{blue_color}ID: {purple_color}{Tesis['id']}\n{blue_color}Descripcion: {purple_color}{Tesis['descripcion']}\n{blue_color}Nivel: {purple_color}{Tesis['nivel']['nivel']}\n")
            time.sleep(5)
        elif opc == '2':
            print(f"{purple_color}Mostrar tesis por ID")

            id = int(input(f"{blue_color}Ingrese el ID de la asignatura a mostrar: {purple_color}"))
            Tesis_encontrada = False
            for Tesis in Tesis:
                if Tesis["id"] == id and Tesis["active"]:
                    Tesis_encontrada = True
                    print(f"{blue_color}tesis encontrada:\n{blue_color}ID: {purple_color}{Tesis['id']}\n{blue_color}Descripcion: {purple_color}{Tesis['descripcion']}\n{blue_color}Nivel: {purple_color}{Tesis['nivel']['nivel']}")
                    break
            if not Tesis_encontrada:
                print(f"{purple_color}La tesis no existe o no está activa")
            time.sleep(5)
        elif opc == '3':
            print(f"{purple_color}Regresando al menu principal")
            time.sleep(2)
            return
        