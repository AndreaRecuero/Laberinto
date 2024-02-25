import unittest
from laberinto import Juego, Laberinto, Habitacion, Puerta

class TestJuegoLaberinto(unittest.TestCase):

    def test_crear_laberinto(self):
        juego = Juego()
        laberinto = juego.fabricarLaberinto2HabitacionesFM()
        
        self.assertIsInstance(laberinto, Laberinto)
        
        habitaciones = laberinto.habitaciones
        self.assertEqual(len(habitaciones), 2)
        
        hab1, hab2 = habitaciones
        
        self.assertIsInstance(hab1, Habitacion)
        self.assertIsInstance(hab2, Habitacion)
        
        #  paredes y puertas
        self.assertIsNotNone(hab1.norte)
        self.assertIsNotNone(hab1.sur)
        self.assertIsNotNone(hab1.este)
        self.assertIsNotNone(hab1.oeste)
        
        self.assertIsNotNone(hab2.norte)
        self.assertIsNotNone(hab2.sur)
        self.assertIsNotNone(hab2.este)
        self.assertIsNotNone(hab2.oeste)
        
        # Verificar que las paredes sean distintas instancias
        self.assertIsNot(hab1.norte, hab2.norte)
        self.assertIsNot(hab1.sur, hab2.sur)
        
        # verifica que al sur de hab1 hay un objeto de tipo puerta
        self.assertIsInstance(hab1.sur, Puerta)


if __name__ == '__main__':
    unittest.main()