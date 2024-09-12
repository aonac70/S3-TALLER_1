from datetime import datetime
class Tesis:
    def __init__(self, id, descripcion, tesis, active=True):
        self.__id = id
        self.descripcion = descripcion
        self.tesis = tesis
        self.active = active
    
    def __str__(self):
        return f'id: {self.__id}, descripcion: {self.descripcion}, {self.tesis}, active: {self.active}'
    
    def getJson(self):
        return {
            'id': self.__id,
            'descripcion': self.descripcion,
            'tesis': self.tesis,
            'active': self.active
        }
    
    
if __name__=='__main__':
    Tesis = Tesis(1,'Primero')
    print(Tesis)
    Tesis = Tesis(1,'Proyecto', Tesis)
    print(Tesis)
    print(Tesis.getJson())


    