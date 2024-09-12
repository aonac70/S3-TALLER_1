from utilss import reset_color, green_color, blue_color, purple_color
from utilss import gotoxy, BorrarPantalla, linea
from datetime import datetime
from Profesor import Profesor
from Asignatura import Asignatura
from Estudiante import Estudiante
from Periodo import Periodo
from Nivel import Nivel

class Nota:
    def __init__(self, id, periodo, profesor, asignatura, active=True):
        self.id = id
        self.periodo = periodo
        self.profesor = profesor
        self.asignatura = asignatura
        self.detalle_notas = []  
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')
    
    def __str__(self):
       return (f"Nota ID: {self.id}, Periodo: {self.periodo}, Profesor: {self.profesor}, "
                f"Asignatura: {self.asignatura}, Activo: {self.active}, Fecha de Creación: {self.fecha_creacion}")
       
    def add_nota(self, detalle_nota):
        self.detalle_notas.append(detalle_nota)
            
    def getJson(self):
        return {
            "id": self.id,
            "periodo": self.periodo,
            "profesor": self.profesor,
            "asignatura": self.asignatura,
            "detalle_notas": [detalle.getJson() for detalle in self.detalle_notas],
            "active": self.active,
            "fecha_creacion": self.fecha_creacion
        }
        
    def mostrar_detalle_notas(self):
        linea(80, green_color)
        print(f"( {purple_color}Universisdad Estatal de Milagro{green_color} )".center(80))
        linea(80, green_color)
        
        print(blue_color + f"Nota ID: {self.id} Fecha: {self.fecha_creacion}")
        print(f" Periodo: {self.periodo.periodo}, Profesor: {self.profesor.nombre} {self.profesor.apellido}, Asignatura: {self.asignatura.descripcion}")
        
        linea(80, green_color)
        print(f"{purple_color} Detalle de Notas".center(80))
        linea(80, green_color)
        print(f"{'Dni':<9}{'Estudiante':<33}{'Nota 1':<10}{'Nota 2':<10}{'Recuperación':<15}{'Promedio':<10}{'Observación':<15}")
        linea(80, green_color)
        
        for detalle in self.detalle_notas:
            recuperacion = detalle.recuperacion if detalle.recuperacion is not None else "N/A"
            print(f"{detalle.estudiante.dni:<9}{detalle.estudiante.nombre} {detalle.estudiante.apellido:<30}{detalle.nota1:<10}{detalle.nota2:<10}{recuperacion:<15}{detalle.promedio:<10.2f}{detalle.observacion:<15}")
        
        linea(80, green_color)

class DetalleNota:
    def __init__(self, nota_id, estudiante, nota1, nota2, recuperacion=None, observacion=None):
        self.id = nota_id  # Asignando el parámetro a self.id
        self.estudiante = estudiante  # Asignando el parámetro a self.estudiante
        self.nota1 = nota1
        self.nota2 = nota2
        self.recuperacion = recuperacion
        self.promedio = self.calcular_promedio()
        self.observacion = observacion or self.generar_observacion()
        
    def calcular_promedio(self):
        notas = [self.nota1, self.nota2]
        if self.recuperacion is not None:
            notas.append(self.recuperacion)
        return sum(notas) / len(notas)
    
    def generar_observacion(self):
        return "Aprobado" if self.promedio >= 70 else "Reprobado"
    
    def __str__(self):
        return (f"Detalle Nota ID: {self.id}, Estudiante: {self.estudiante}, Nota 1: {self.nota1}, "
                f"Nota 2: {self.nota2}, Recuperación: {self.recuperacion}, Observación: {self.observacion}")
    
    def getJson(self):
        return {
            "id": self.id,
            "estudiante": self.estudiante,
            "nota1": self.nota1,
            "nota2": self.nota2,
            "recuperacion": self.recuperacion,
            "promedio": self.promedio,
            "observacion": self.observacion
        }

if __name__ == '__main__':
    profesor = Profesor('Juan', 'Perez', '12345678')
    nivel = Nivel(1, "Primero")
    asignatura = Asignatura(1, "Matemáticas", nivel)
    periodo = Periodo(1, '2021-2022')
    estudiante = Estudiante("juan", "perez", "12345678")
    estudiante2 = Estudiante("maria", "gomez", "87654321")
    nota = Nota(1, periodo, profesor, asignatura)
    detalle_nota = DetalleNota(nota.id, estudiante, 80, 90)
    detalle_nota2 = DetalleNota(nota.id, estudiante2, 70, 60)
    nota.add_nota(detalle_nota)
    nota.add_nota(detalle_nota2)
    print(nota.getJson())
    nota.mostrar_detalle_notas()
    
    

    
