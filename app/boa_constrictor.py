from app.animal_exotico import Animal_Exotico

class Boa_constrictor(Animal_Exotico):
    def __init__(self, nombre:str, peso:float, edad:int, pais_origen:str, impuesto:float)->None:
        super().__init__(nombre, peso, edad, pais_origen, impuesto)
        self._ratones_comidos = 0
    
    def hacer_sonido(self)->str:
        return "¡Tsss!"
    
    def comer_ratones(self, ratones: int) -> None:
        if ratones == 10:
            raise ValueError("Demasiados Ratones!")
        self._ratones_comidos += ratones
    
    def total_ratones(self)-> int:
        return self._ratones_comidos