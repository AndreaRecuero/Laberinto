import random

class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass
    
    def print(self):
        print("ElementoMapa")

    def esHabitacion(self):
        return False

class Contenedor(ElementoMapa):  #subclase ElementoMapa
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones=[]

    def agregarHijo(self, componente):
        self.hijos.append(componente)

    def eliminarHijo(self, componente):
        self.hijos.remove(componente)

    def print(self):
        print("Contenedor")
    
    def caminarAleatorio(self, alguien):
        pass

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)
    
    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def caminarAleatorio(self, alguien):        
        orientacion = self.OrientacionAleatoria()
        orientacion.caminarAleatorio(alguien)

    def OrientacionAleatoria(self):
        return random.choice(self.orientacion)
    
    def irANorte(self, alguien):
        self.norte.entrar(alguien)
    def irAEste(self, alguien):
        self.este.entrar(alguien)
    def irASur(self, alguien):
        self.sur.entrar(alguien)
    def irAOeste(self, alguien):
        self.oeste.entrar(alguien)
    def ponerEn(self, em, orientacion):
        orientacion.ponerEn(em, self)

class Laberinto(Contenedor):    #subclase Contenedor
    def __init__(self):
        super().__init__()

    def agregarHabitacion(self, habitacion):
        self.agregarHijo(habitacion)

    def entrar(self, alguien):
        self.hijos[0].entrar(alguien)

    def print(self):
        print("Laberinto")   
    
    def obtenerHabitacion(self, id):
        for habitacion in self.hijos:
            if habitacion.id == id:
                return habitacion
        return None

class Habitacion(Contenedor):   #subclase Contenedor

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None

    def entrar(self, alguien):
        print(alguien + " está en habitación ", self.id)

    def print(self):
        print("Habitación")

    def esHabitacion(self):
        return True

class Hoja(ElementoMapa):   #subclase ElementoMapa
    def __init__(self):
        super().__init__()
    
    def print(self):
        print("Hoja")

class Decorator(Hoja): #subclase Hoja
    def __init__(self):
        super().__init__()
        self.comp = None
    
    def print(self):
        print("Decorator")

class Bomba(Decorator):
    def __init__(self):
        super().__init__()
        self.activa = False

    def print(self):
        print("Bomba")

    def entrar(self, alguien):
        print(alguien + " ha entrado en una bomba")

class Pared(ElementoMapa):  #subclase ElementoMapa
    def __init__(self):
        pass  # Las paredes no necesitan atributos adicionales
    
    def print(self):
        print("Pared")

    def entrar(self, alguien):
        print(alguien + " se ha chocado con una pared")

# ParedBomba.py

class ParedBomba(Pared):    #subclase Pared
    #def __init__(self):
    #    self.activa = False

    #def entrar(self):
    #    if self.activa:
    #        print("La bomba ha explotado!")
    #    else:
    #        return super().entrar()

    def __init__(self):
        super().__init__()
        self.activa = False
    
    def print(self):
        print("ParedBomba")

# Puerta.py

class Puerta(ElementoMapa):     #subclase ElementoMapa
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self, alguien):
        if self.abierta:
            print("Puerta abierta")
            self.lado2.entrar()
        else:
            print("Puerta cerrada")
        
    def print(self):
        print("Puerta")

class Orientacion:
    def __init__(self):
        pass
    def caminar(self, alguien):
        pass
    def ponerElementoEn(self, unEm, unContenedor):
        pass

class Norte(Orientacion):
    _instance = None
    def __init__(self):
        if not Norte._instance:
            super().__init__()
            Norte._instance = self

    def ponerElementoEn(self, unEm, unContenedor):
        unContenedor.norte = unEm

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Norte()
        return cls._instance

    def print(self):
        print("Norte")
    
    def caminar(self, alguien):
        alguien.irANorte()


class Sur(Orientacion):
    _instance = None
    def __init__(self):
        if not Sur._instance:
            super().__init__()  
            Sur._instance = self

    @staticmethod 
    def get_instance():
        if not Sur._instance:
            Sur()
        return Sur._instance
    
    def print(self):
        print("Sur")
    
    def caminar(self, alguien):
        alguien.irASur()
    
    def setEMinOr(self, unEm, unContenedor):
        unContenedor.sur = unEm

class Este(Orientacion):
    _instance = None
    def __init__(self):
        raise RuntimeError('Llamar instance()')
        # if not Este._instance:
        #     super().__init__()
        #     Este._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print('Creando nueva instancia')
            cls._instance = cls.__new__(cls)
            
        return cls._instance
    
    def caminar(self, alguien):
        alguien.irAEste()
    
    def ponerElementoEn(self, unEm, unContenedor):
        unContenedor.este = unEm
    # @staticmethod
    # def get_instance():
    #     if not Este._instance:
    #         Este()
    #     return Este._instance
    
    # def print(self):
    #     print("Este")

class Oeste(Orientacion):
    _instance = None
    def __init__(self):
        if not Oeste._instance:
            super().__init__()
            Oeste._instance = self

    @staticmethod
    def get_instance():
        if not Oeste._instance:
            Oeste()
        return Oeste._instance
    
    def print(self):
        print("Oeste")
    
    def caminar(self, alguien):
        alguien.irAOeste()

    def ponerElementoEn(self, unEm, unContenedor):
        unContenedor.oeste = unEm

"""class Juego:
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


game = Juego()
game.fabricarLaberinto2Habitaciones()
game.laberinto.entrar()

game = Juego()
game.fabricarLaberinto2HabitacionesFM()

game = juegoBomba()
game.fabricarLaberinto2HabitacionesFM()
game.laberinto.entrar()"""
