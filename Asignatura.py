from Nivel import Nivel
class Asignatura:
    def __init__(self, id, descripcion, nivel, active=True):
        self.__id = id
        self.descripcion = descripcion
        self.nivel = nivel
        self.active = active
    
    def __str__(self):
        return f'id: {self.__id}, descripcion: {self.descripcion}, {self.nivel}, active: {self.active}'
    
    def getJson(self):
        return {
            'id': self.__id,
            'descripcion': self.descripcion,
            'nivel': self.nivel,
            'active': self.active
        }
    
    
if __name__=='__main__':
    Nivel1 = Nivel(1,'Primero')
    print(Nivel1)
    Asignatura1 = Asignatura(1,'Matematicas', Nivel1)
    print(Asignatura1)
    print(Asignatura1.getJson())


    

