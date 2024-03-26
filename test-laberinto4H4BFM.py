import unittest
from laberinto import Habitacion
from juego import Juego


class TestJuego(unittest.TestCase):

    def test_fabricar4Hab4BichosFM(self):
        juego = Juego()
        juego.fabricarlaberinto4hab4bichostFM()

        # Check number of rooms
        self.assertEqual(len(juego.laberinto.hijos), 4)
        self.assertEqual(len(juego.bichos), 4)

        # Check connections between rooms
        hab1 = juego.laberinto.obtenerHabitacion(1)
        hab2 = juego.laberinto.obtenerHabitacion(2)
        hab3 = juego.laberinto.obtenerHabitacion(3)
        hab4 = juego.laberinto.obtenerHabitacion(4)

        self.assertIs(hab1.sur, hab2.norte)
        self.assertIs(hab1.este, hab3.oeste)
        self.assertIs(hab2.este, hab4.oeste)
        self.assertIs(hab3.sur, hab4.norte)

        # Check beast positions
        self.assertTrue(juego.bichos[0].posicion.esHabitacion)
        self.assertTrue(juego.bichos[1].posicion.esHabitacion)
        self.assertTrue(juego.bichos[2].posicion.esHabitacion)
        self.assertTrue(juego.bichos[3].posicion.esHabitacion)

        self.assertIs(juego.bichos[0].posicion, hab1)
        self.assertIs(juego.bichos[1].posicion, hab2)
        self.assertIs(juego.bichos[2].posicion, hab3)
        self.assertIs(juego.bichos[3].posicion, hab4)

        self.assertTrue(juego.bichos[0].esAgresivo())
        self.assertTrue(juego.bichos[1].esPerezoso())
        self.assertTrue(juego.bichos[2].esAgresivo())
        self.assertTrue(juego.bichos[3].esPerezoso())


if __name__ == '__main__':
    unittest.main()