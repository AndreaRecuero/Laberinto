import unittest
from laberinto import Laberinto
from juego import Juego


class TestJuego(unittest.TestCase):

    def test_fabricarHabitacion_devuelve_hab_con_paredes(self):
        juego = Juego()
        habitacion = juego.fabricarHabitacion(1)
        self.assertIsNotNone(habitacion.norte)
        self.assertIsNotNone(habitacion.sur)
        self.assertIsNotNone(habitacion.este)
        self.assertIsNotNone(habitacion.oeste)

    def test_fabricarHabitacion_devuelve_habitacion_con_id_correcto(self):
        juego = Juego()
        habitacion = juego.fabricarHabitacion(5)
        self.assertEqual(habitacion.id, 5)

    def test_fabricarHabitacion_devuelve_diferentes_habitaciones(self):
        juego = Juego()
        hab1 = juego.fabricarHabitacion(1)
        hab2 = juego.fabricarHabitacion(2)
        self.assertNotEqual(hab1, hab2)