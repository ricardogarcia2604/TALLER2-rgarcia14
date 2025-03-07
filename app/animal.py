from app.ianimal import iAnimal

class Animal(iAnimal):
    def __init__(self, nombre:str, peso:float, edad:int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad
        self._kilos_comidos = 0
        

    def comer(self, kilos:float):
        self.__kilos_comidos = kilos

    def obtener_kilos_comidos(self):
        return self.__kilos_comidos
    
    def hacer_sonido(self):
        pass

    def obtener_nombre(self):
        return self.__nombre

    def obtener_peso(self):
        return self.__peso

    def obtener_edad(self):
        return self.__edad


