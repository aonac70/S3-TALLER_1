from utilss import  green_color,blue_color, green_color 
from utilss import gotoxy, BorrarPantalla, linea
from Componets import Menu, Valida
from ClsJson import JsonFile
from Periodo import Periodo
from Icrud import Icrud
import time
import os

path, file = os.path.split(__file__) 


class CrudPeriodo(Icrud):
    json_file = JsonFile(f"{path}/data/periodos.json")

    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Registro de Periodo")
        linea(80, green_color)
        
        periodos = self.json_file.read()
        
        if periodos:
            next_id = max(p['id'] for p in periodos) + 1
        else:
            next_id = 1
        
        id_periodo = input(f"{blue_color}Ingrese el nombre del periodo: {green_color}")
        linea(80, green_color)
        periodo = self.json_file.find('periodo', id_periodo)
    
        if periodo:  # Verifica si se encontró algún resultado
            periodo = periodo[0]
            print(f"{blue_color}El periodo ya existe")
            print(f"{green_color}ID: {blue_color}{periodo['id']}\n{green_color}Periodo: {blue_color}{periodo['periodo']}")
            linea(80, green_color)
            time.sleep(2)
        else:
            linea(80, green_color)
            print(f"{green_color}Periodo registrado correctamente")
            print(f"{green_color}ID: {blue_color}{next_id}\n{green_color}Periodo: {blue_color}{id_periodo}")
            linea(80, green_color)
            n_nivel = Periodo(next_id, id_periodo)  # Corrección: usas 'id_periodo' aquí, no 'periodo'
            periodos.append(n_nivel.getJson())
            self.json_file.save(periodos)
            print(f"{green_color}Periodo guardado correctamente")
            time.sleep(2)
        
    def update(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{green_color}Actualizar Nivel")
        linea(80, green_color)
        
        id = int(Valida.validar_numeros(f"{blue_color}Ingrese el ID del periodo a actualizar: {green_color}",1 ,4, 41, 4))
        
        periodos = self.json_file.read()  
        
        linea(80, green_color)
        periodo_encontrado = False 
        for periodo in periodos:  
            if periodo["id"] == id and periodo["active"]:  
                periodo_encontrado = True
                print(f"{blue_color}Nivel encontrado: {green_color}{periodo['periodo']}")
                nuevo_nivel = input(f"{blue_color}Ingrese el nuevo nombre del periodo: {green_color}")
                
                duplicado = self.json_file.find('periodo', nuevo_nivel)
                
                if len(duplicado) > 0:
                    print(f"{green_color}El periodo ya existe")
                    time.sleep(2)
                    return
                linea(80, green_color)
                confirmacion = input(f"{blue_color}¿Está seguro de actualizar el periodo? s/n: {green_color}")
                if confirmacion.lower() == 's':
                    periodo["periodo"] = nuevo_nivel  
                    self.json_file.save(periodos)  
                    linea(80, green_color)
                    print(f"{blue_color}periodo actualizado correctamente")
                    linea(80, green_color)
                    time.sleep(2)
                else:
                    linea(80, green_color)
                    print(f"{blue_color}No se actualizó el periodo")
                    linea(80, green_color)
                    time.sleep(2)
                break  
        
        if not periodo_encontrado:
            linea(80, green_color)
            print(f"{blue_color}El periodo no existe o no está activo")
            time.sleep(2)

    def delete(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{green_color}Eliminar Periodo")
        linea(80, green_color)
        
        id = int(Valida.validar_numeros(f"{blue_color}Ingrese el ID del periodo a eliminar: {green_color}",1 ,4, 40, 4))
        
        periodos = self.json_file.read()  
        
        linea(80, green_color)
        periodo_encontrado = False
        for periodo in periodos:  
            if periodo["id"] == id and periodo["active"]:  
                periodo_encontrado = True
                print(f"{blue_color}Periodo encontrado: {green_color}{periodo['periodo']}\nFecha de creación: {blue_color}{periodo['fecha_creacion']}")
                linea(80, green_color)
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar el periodo? s/n: {green_color}")
                if confirmacion.lower() == 's':
                    periodo["active"] = False  
                    self.json_file.save(periodos)  
                    print(f"{green_color}Periodo eliminado correctamente")
                    time.sleep(2)
                else:
                    linea(80, green_color)
                    print(f"{blue_color}No se eliminó el periodo")
                    time.sleep(2)
                break  
        
        if not periodo_encontrado:
            linea(80, green_color)
            print(f"{blue_color}El periodo no existe o ya está inactivo")
            time.sleep(2)
            
    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2),print(f"{green_color}Mostrar Periodos")
        linea(80, green_color)
        
        periodos = self.json_file.read()  
        
        menu = Menu("Seleccione una opción", ["Mostrar todos los periodos", "Buscar periodo por ID", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        periodos_encontrados = False
        
        linea(80, green_color)
        if opc == '1':
            if periodos:
                print(f"{blue_color}Periodos registrados:")
                for periodo in periodos:
                    if periodo['active']:
                        print(f"{blue_color}ID: {green_color}{periodo['id']}\n{blue_color}Periodo: {green_color}{periodo['periodo']}\n")
                        linea(80, green_color)
                        periodos_encontrados = True
            else:
                linea(80, green_color)
                print(f"{green_color}No hay periodos registrados.")
            time.sleep(3)
        elif opc == '2':
            id = int(Valida.validar_numeros(f"{blue_color}Ingrese el ID del periodo a buscar: {green_color}", 1, 10, 39, 10))
            linea(80, green_color)
            for periodo in periodos:
                if periodo['id'] == id and periodo['active']:
                    print(f"{blue_color}Periodo encontrado: {green_color}{periodo['periodo']}")
                    periodos_encontrados = True
                    break
            if not periodos_encontrados:
                linea(80, green_color)
                print(f"{blue_color}No se encontró un periodo con ID {id}.")
            time.sleep(3)
        else:
            linea(80, green_color)
            print(f"{blue_color}Regresando al menú principal.")
            time.sleep(2)
            