# bicho.pyclass Bicho:
import time

class Bicho:
    def __init__(self, modo):
        self.modo = modo
        self.poder = 2
        self.vidas = 10
        self.posicion = None
        self.juego=0
    
    def __str__(self):
        template='Bicho-{0.modo}{0.juego}'
        return template.format(self)
    
    def esAgresivo(self):
        return self.modo.esAgresivo()

    def esPerezoso(self):
        return self.modo.esPerezoso()
    
    def actua(self):
        self.modo.actua(self)
    
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    def irANorte(self):
        self.posicion.irANorte(self)
    def irAEste(self):
        self.posicion.irAEste(self)
    def irASur(self):
        self.posicion.irASur(self)
    def irAOeste(self):
        self.posicion.irAOeste(self)
    def empezar(self):
        self.actua()
    def parar(self):
        print(self , " ha parado")
        exit(0)

class Modo:
    def __init__(self):
        pass
    def __str__(self):    
        pass
    def esAgresivo(self):
        return False
    def esPerezoso(self):
        return False
    def actua(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
    def caminar(self, bicho):
        bicho.caminarAleatorio()
    def dormir(self, bicho):
        print(bicho,"  está durmiendo")
        time.sleep(3)

class Agresivo(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "Agresivo"
    
    def esAgresivo(self):
        return True

    def print(self):
        print("Bicho Agresivo")

class Perezoso(Modo):
    def __init__(self):
        super().__init__()
    
    def __str__(self):    
        return "Perezoso"
    
    def print(self):
        print("Bicho Perezoso")

    def esPerezoso(self):
        return True