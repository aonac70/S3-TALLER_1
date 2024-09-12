from datetime import datetime

class Profesor:
    def __init__(self, nombre, apellido, dni, active=True):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')
    
    def __str__(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}, dni: {self.dni}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def full_name(self):
        return f'{self.nombre} {self.apellido}'
    
    def getjson(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'dni': self.dni,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }


if __name__ == '__main__':
    profesor = Profesor('Juan', 'Perez', '12345678')
    print(profesor)
    print(profesor.full_name())
