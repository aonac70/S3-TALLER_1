from datetime import datetime

class Nivel:
    def __init__(self, id, nivel, active=True):
        self.id = id
        self.nivel = nivel
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')

    def __str__(self): 
        return f'id: {self.id}, nivel: {self.nivel}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def get_nivel(self):
        return f'id: {self.id} Nivel: {self.nivel} Active: {self.active} Fecha Creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'id': self.id,
            'nivel': self.nivel,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }
    

if __name__=='__main__':
    nivel = Nivel(1, 'Primero')
    print(nivel)
    print(nivel.getJson())
    print(nivel.nivel)
    
