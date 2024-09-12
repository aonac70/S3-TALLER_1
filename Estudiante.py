from datetime import datetime

class Estudiante:
    def __init__(self, nombre, apellido, dni,active=True):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')
    
    def __str__(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}, dni: {self.dni}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }
    

if __name__ == '__main__':
    estudiante1 = Estudiante('Juan', 'Perez', '12345678')
    estudiante2 = Estudiante('Maria', 'Gomez', '87654321')
    print(estudiante1)
    print(estudiante2)