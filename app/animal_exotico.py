from app.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre:str, peso:float, edad:int,pais_origen:str,impuesto:float):
        super().__init__(nombre, peso, edad)
        self._pais_origen = pais_origen
        self._impuesto = impuesto

    def calcular_flete(self)-> float:
        return self._impuesto * self._peso
    
    def hacer_sonido(self):
        pass