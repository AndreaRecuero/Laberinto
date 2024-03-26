from laberinto import Laberinto, Habitacion, Puerta, Pared, ParedBomba, Bomba, Norte, Este, Sur, Oeste
from bicho import Bicho, Modo, Agresivo, Perezoso
from gestionHilos import GestionHilos
import time


class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []
        self.gestionHilos = GestionHilos()

    def lanzarHilos(self):
        for bicho in self.bichos:
            self.gestionHilos.agregarHilo(bicho)
        self.gestionHilos.lanzar()

    def terminarHilos(self):
        self.gestionHilos.terminar()
        self.gestionHilos.juntar()

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, hab1, hab2):
        puerta = Puerta(hab1, hab2)
        return puerta

    def fabricarHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.agregarOrientacion(self.fabricarNorte())
        habitacion.agregarOrientacion(self.fabricarEste())
        habitacion.agregarOrientacion(self.fabricarSur())
        habitacion.agregarOrientacion(self.fabricarOeste())
        habitacion.norte = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricarNorte(self):
        return Norte().get_instance()

    def fabricarEste(self):
        return Este.get_instance()

    def fabricarSur(self):
        return Sur().get_instance()

    def fabricarOeste(self):
        return Oeste().get_instance()

    def fabricarLaberinto2Habitaciones(self):
        laberinto = Laberinto()
        self.laberinto = laberinto
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta(hab1, hab2)

        hab1.sur = puerta
        hab2.norte = puerta

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def fabricarlaberinto4hab4bichostFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)

        puerta12 = self.fabricarPuerta(hab1, hab2)
        puerta13 = self.fabricarPuerta(hab1, hab3)
        puerta24 = self.fabricarPuerta(hab2, hab4)
        puerta34 = self.fabricarPuerta(hab3, hab4)

        hab1.sur = puerta12
        hab2.norte = puerta12

        hab1.este = puerta13
        hab3.oeste = puerta13

        hab2.este = puerta24
        hab4.oeste = puerta24

        hab3.sur = puerta34
        hab4.norte = puerta34

        laberinto = Laberinto()

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        laberinto.agregarHabitacion(hab3)
        laberinto.agregarHabitacion(hab4)
        self.laberinto = laberinto

        bicho1 = self.fabricarBichoAgresivo(hab1)
        bicho2 = self.fabricarBichoPerezoso(hab2)
        bicho3 = self.fabricarBichoAgresivo(hab3)
        bicho4 = self.fabricarBichoPerezoso(hab4)

        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)
        self.agregarBicho(bicho3)
        self.agregarBicho(bicho4)

        return laberinto

    def fabricarLaberinto2HabitacionesFM(self):
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)
        laberinto = Laberinto()
        self.laberinto = laberinto
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        hab1.sur = puerta
        hab2.norte = puerta

        return laberinto

    def agregarBicho(self, bicho):
        bicho.num = len(self.bichos) + 1
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho):
        self.bichos.remove(bicho)

    def fabricarBichoAgresivo(self, habitacion):
        bicho = Bicho(Agresivo())
        bicho.poder = 5
        bicho.posicion = habitacion
        return bicho

    def fabricarBichoPerezoso(self, habitacion):
        bicho = Bicho(Perezoso())
        bicho.poder = 1
        bicho.posicion = habitacion
        return bicho

    def print(self):
        print("Juego")


# BombedGame.py
class JuegoBomba(Juego):
    def fabricarPared(self):
        return ParedBomba()

    def print(self):
        print("JuegoBomba")

# juego = Juego()
# juego.fabricarLaberinto2Habitaciones()
# juego.laberinto.entrar()

# juego = Juego()
# juego.fabricarLaberinto2HabitacionesFM()

# juego = JuegoBomba()
# juego.fabricarLaberinto2HabitacionesFM()
# juego.laberinto.entrar()

# juego = Juego()
# juego.fabricarlaberinto4hab4bichosFM()
# alguien = "pepe"
# juego.laberinto.entrar(alguien)
# juego.lanzarHilos()
# time.sleep(10)
# juego.terminarHilos()