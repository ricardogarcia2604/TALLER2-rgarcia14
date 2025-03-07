import unittest
from app.boa_constrictor import Boa_constrictor
from app.huron import Huron

class test_Hurones(unittest.TestCase):

    def setUp(self):
        self.huron1 = Huron("Alfredo", 5, 2, "Asia", 400000)
    
    def test_hacer_sonido(self):
        self.assertEqual(self.huron1.hacer_sonido(),"¡Eek Eek!")

class test_Boas(unittest.TestCase):
    def setUp(self):
        self.boa1 = Boa_constrictor("Elvira", 7, 1, "Amazonas", 1000000)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa1.hacer_sonido(),"¡Tsss!")


    def test_alimentar_boa(self):
        self.boa1.comer_ratones(3)
        self.assertEqual(self.boa1.total_ratones(), 3)


if __name__ == "__main__":
    unittest.main()
