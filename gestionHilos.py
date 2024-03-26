import threading
import time

class GestionHilos:
    def __init__(self):
        self.hilos = []

    def agregarHilo(self, hilo):
        self.hilos.append(hilo)

    def lanzar(self):
        for hilo in self.hilos:
            hilo.start()

    def juntar(self):
        for hilo in self.hilos:
            hilo.join()

    def terminar(self):
        for hilo in self.hilos:
            hilo.stop()