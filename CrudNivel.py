from utilss import green_color, blue_color, green_color, gotoxy, BorrarPantalla, linea
from Componets import Menu, Valida
from ClsJson import JsonFile
from Nivel import Nivel
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 

class CrudNivel(Icrud):
    json_file = JsonFile(f"{path}/data/niveles.json")
    
    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{blue_color}Registro de Nivel")
        linea(80, green_color)
        
        niveles = self.json_file.read()
        
        if niveles:
            next_id = max(n['id'] for n in niveles) + 1
        else:
            next_id = 1
        
        n_nivel = Valida.validar_letras(f"{blue_color}Ingrese el nombre del nivel: {green_color}", 1, 4, 31, 4)
        
        nivel = self.json_file.find('nivel', n_nivel)
        
        if nivel: 
            nivel = nivel[0]  
            linea(80, green_color)
            print(f"{blue_color}El nivel ya existe")
            print(f"{green_color}ID: {blue_color}{nivel['id']}\n{green_color}Nivel: {blue_color}{nivel['nivel']}")
            linea(80, green_color)
            time.sleep(2)
        else:
            linea(80, green_color)
            print(f"{green_color}Nivel registrado correctamente")
            print(f"{green_color}ID: {blue_color}{next_id}\n{green_color}Nivel: {blue_color}{n_nivel}")
            nuevo_nivel = Nivel(next_id, n_nivel) 
            niveles.append(nuevo_nivel.getJson())
            self.json_file.save(niveles)
            linea(80, green_color)
            print(f"{blue_color}Nivel guardado correctamente")
            time.sleep(2)
                
    def update(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{blue_color}Actualizar Nivel")
        linea(80, green_color)
        
        id = int(Valida.validar_numeros(f"{blue_color}Ingrese el ID del nivel a actualizar: {green_color}", 1, 4, 39, 4))
        
        niveles = self.json_file.read()  
        
        nivel_encontrado = False 
        for nivel in niveles:  
            if nivel["id"] == id and nivel["active"]:  
                nivel_encontrado = True
                print(f"{blue_color}Nivel encontrado: {green_color}{nivel['nivel']}")
                linea(80, green_color)
                nuevo_nivel = input(f"{blue_color}Ingrese el nuevo nombre del nivel: {green_color}")
                
                duplicado = self.json_file.find('nivel', nuevo_nivel)
                
                if len(duplicado) > 0:
                    linea(80, green_color)
                    print(f"{blue_color}El nivel ya se encuentra registrado")
                    print(f"{green_color}ID: {blue_color}{duplicado[0]['id']}\n{green_color}Nivel: {blue_color}{duplicado[0]['nivel']}")
                    time.sleep(2)
                    return
                linea(80, green_color)
                confirmacion = Valida.validar_letras(f"{blue_color}¿Está seguro de actualizar el nivel? s/n: {green_color}", 1, 9, 42, 9)
                if confirmacion.lower() == 's':
                    nivel["nivel"] = nuevo_nivel  
                    self.json_file.save(niveles) 
                    linea(80, green_color) 
                    print(f"{blue_color}Nivel actualizado correctamente")
                    time.sleep(2)
                else:
                    print(f"{blue_color}No se actualizó el nivel")
                    time.sleep(2)
                break  
        
        if not nivel_encontrado:
            print(f"{blue_color}El nivel no existe o no está activo")
            time.sleep(2)
        
    def delete(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{green_color}Eliminar Nivel")
        linea(80, green_color)
        
        id = int(Valida.validar_numeros(f"{blue_color}Ingrese el ID del nivel a eliminar: {green_color}"),1, 4, 39, 4)
        
        niveles = self.json_file.read()  
        
        nivel_encontrado = False
        for nivel in niveles:  
            if nivel["id"] == id and nivel["active"]:  
                nivel_encontrado = True
                print(f"{blue_color}Nivel encontrado: {green_color}{nivel['nivel']}")
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar el nivel? s/n: {green_color}")
                if confirmacion.lower() == 's':
                    nivel["active"] = False  
                    self.json_file.save(niveles)  
                    print(f"{green_color}Nivel eliminado correctamente")
                    time.sleep(2)
                else:
                    print(f"{green_color}No se eliminó el nivel")
                    time.sleep(2)
                break  
        
        if not nivel_encontrado:
            print(f"{green_color}El nivel no existe o ya está inactivo")
            time.sleep(2)
        
    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{green_color}Mostrar Nivel")
        linea(80, green_color)
        
        niveles = self.json_file.read()  
        
        menu = Menu("Seleccione una opción", ["Mostrar todos los Niveles", "Buscar nivel por ID", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        nivele_encontrado = False
        
        if opc == '1':
            if niveles:
                print(f"{blue_color}Niveles registrados:")
                for nivel in niveles:
                    if nivel['active']:
                        print(f"{blue_color}ID: {green_color}{nivel['id']}\n{blue_color}Nivel: {green_color}{nivel['nivel']}\n")
                        nivele_encontrado = True
            else:
                print(f"{green_color}No hay niveles registrados.")
            time.sleep(3)
        elif opc == '2':
            id = int(input(f"{blue_color}Ingrese el ID del nivel a buscar: {green_color}"))
            for nivel in niveles:
                if nivel['id'] == id and nivel['active']:
                    print(f"{blue_color}nivel encontrado: {green_color}{nivel['nivel']}")
                    nivele_encontrado = True
                    break
            if not nivele_encontrado:
                print(f"{green_color}No se encontró un nivel con ID {id}.")
            time.sleep(3)
        else:
            print(f"{green_color}Regresando al menú principal.")
            time.sleep(2)
            