from app.huron import Huron
from app.boa_constrictor import Boa_constrictor

boa1 = Boa_constrictor("Sebastian",20, 3, "Amazonas", 1000000)
huron1 = Huron("Paco", 2, 1,"Bogota", 900000)

def probando_boa():
    print(boa1.hacer_sonido())
    print(boa1.total_ratones())
    print(boa1.comer_ratones(10))
    print(boa1.total_ratones())
    print(boa1.comer_ratones(5))
    print(boa1.total_ratones())
    print(boa1.calcular_flete())


def probando_huron():
    print(huron1.hacer_sonido())
    print(huron1.calcular_flete())

print("\nProbando las acciones de la Boa -->")
probando_boa()

print("\nProbando las acciones del Huron -->")
probando_huron()
