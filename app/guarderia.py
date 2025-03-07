from app.boa_constrictor import Boa_constrictor
from app.huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [
            Boa_constrictor("Elvira", 7, 1, "Amazonas", 1000000),
            Boa_constrictor("Nagini", 6, 2, "África", 1200000)
        ]
        self.hurones = [
            Huron("Alfredo", 5, 2, "Asia", 400000),
            Huron("Max", 4, 3, "Europa", 350000)
        ]

    def alimentar_boa(self, boa: Boa_constrictor, ratones: int) -> str:
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.comer_ratones(ratones)
            return "Éxito"
        except ValueError as e:
            return "La boa está llena"

