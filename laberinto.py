class Juego:
    def __init__(self):
        self.laberinto = None

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, lado2):
        puerta = Puerta(lado1, lado2)
        return puerta

    def fabricarHabitacion(self, id):
        habitacion = Habitacion(id)
        habitacion.norte = self.fabricarPared()
        habitacion.este = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        return habitacion

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarLaberinto2HabitacionesFM(self):  #factory method
        self.laberinto = self.fabricarLaberinto()
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        return self.laberinto

    def fabricarLaberinto2Habitaciones(self):
        self.laberinto = Laberinto()
        hab1 = Habitacion(1)
        hab2 = Habitacion(2)
        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        puerta = Puerta(hab1, hab2)
        hab1.sur = puerta
        hab2.norte = puerta
        return self.laberinto


class juegoBomba(Juego):  #subclase Juego
    def fabricarPared(self):
        return ParedBomba()


class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass


class Contenedor(ElementoMapa):  #subclase ElementoMapa
    def __init__(self):
        self.hijos = []

    def agregarHijo(self, hijo):
        self.hijos.append(hijo)

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)


class Laberinto(Contenedor):    #subclase Contenedor
    def __init__(self):
        self.habitaciones = []

    def agregarHabitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def entrar(self):
        self.habitaciones[0].entrar()


class Habitacion(Contenedor):   #subclase Contenedor
    def __init__(self, id):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.id = id

    def entrar(self):
        print("Estás en habitación ", self.id)


class Hoja(ElementoMapa):   #subclase ElementoMapa
    def accept(self, visitor):
        visitor.visitHoja(self)

class Decorator(Hoja): #subclase Hoja
    def __init__(self, component):
        self.component = component


class Puerta(ElementoMapa):     #subclase ElementoMapa
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self):
        if self.abierta:
            print("Puerta abierta")
            self.lado2.entrar()
        else:
            print("Puerta cerrada")


class Pared(ElementoMapa):  #subclase ElementoMapa
    def __init__(self):
        pass  # Las paredes no necesitan atributos adicionales

    def entrar(self):
        print("Te has chocado con una pared")


class ParedBomba(Pared):    #subclase Pared
    def __init__(self):
        self.activa = False

    def entrar(self):
        if self.activa:
            print("La bomba ha explotado!")
        else:
            return super().entrar()


game = Juego()
game.fabricarLaberinto2Habitaciones()
game.laberinto.entrar()

game = Juego()
game.fabricarLaberinto2HabitacionesFM()

game = juegoBomba()
game.fabricarLaberinto2HabitacionesFM()
game.laberinto.entrar()
