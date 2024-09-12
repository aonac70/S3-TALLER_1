from datetime import datetime

#Clase Periodo
class Periodo:
    def __init__(self, id, periodo, active=True):
        self.__id = id
        self.periodo = periodo
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')

    @property
    def id(self):
        return self.__id


    def __str__(self):
        return f'id: {self.__id}, periodo: {self.periodo}, active: {self.active}, fecha_creacion: {self.fecha_creacion}'
    
    def getJson(self):
        return {
            'id': self.__id,
            'periodo': self.periodo,
            'active': self.active,
            'fecha_creacion': self.fecha_creacion
        }
if __name__=='__main__':
    periodo = Periodo(1, '2021-2022')
    print(Periodo)