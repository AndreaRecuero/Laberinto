import json
from laberinto import Laberinto, Habitacion, Puerta, Pared, Bomba, Norte, Este, Sur, Oeste

class Director:
    def __init__(self):
        self.diccionario=None
        self.builder=LaberintoBuilder()

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.fabricarLaberinto()

    def leerArchivo(self, unArchivo):
        try:
            with open(unArchivo) as f:
                data = json.load(f)
                self.diccionario= data
        except FileNotFoundError:
            print(f"Archivo {unArchivo} no existe")
            return None
    
    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        
        for each in self.diccionario['laberinto']:
            self.fabricarLaberintoRecursivo(each, 'root')
            
        for each in self.diccionario['puertas']:
            n1 = each[0]
            or1 = each[1]
            n2 = each[2]
            or2 = each[3]
            self.builder.fabricarPuertaN1(n1, or1, n2, or2)
    
    def fabricarLaberintoRecursivo(self, unDic, padre):
    
        if unDic['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(unDic['num'])
            
        if unDic['tipo'] == 'bomba':
            self.builder.fabricarBombaEn(padre)
            
        if 'hijos' in unDic:
            for each in unDic['hijos']:
                self.fabricarLaberintoRecursivo(each, con)

class LaberintoBuilder:
    def __init__(self):
        self.juego = None
        self.laberinto = None
    
    def fabricarLaberinto(self):
        self.laberinto = Laberinto()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuertaLado1(self,hab1, hab2):
        puerta = Puerta(hab1, hab2)
        return puerta

    def fabricarBombaEn(self, habitacion):
        bomba=Bomba()
        habitacion.agregarHijo(bomba)
        return bomba

    def fabricarHabitacion(self, id):
        habitacion=Habitacion(id)
        habitacion.agregarOrientacion(self.fabricarNorte())
        habitacion.agregarOrientacion(self.fabricarEste())
        habitacion.agregarOrientacion(self.fabricarSur())
        habitacion.agregarOrientacion(self.fabricarOeste())
        for each in habitacion.orientaciones:
            each.ponerElementoEn(self.fabricarPared, self)
        self.laberinto.agregarHabitacion(habitacion)
        return habitacion

    def fabricarNorte(self):
        return Norte().get_instance()

    def fabricarEste(self):
        return Este.get_instance()
    
    def fabricarSur(self):
        return Sur().get_instance()
    
    def fabricarOeste(self):
        return Oeste().get_instance()
    
    def fabricarPuertaN1(self, unNum, unaOrString, otroNum, otraOrString):

        lado1 = self.laberinto.obtenerHabitacion(unNum)
        lado2 = self.laberinto.obtenerHabitacion(otroNum)
        
        or1 = getattr(self, 'fabricar' + unaOrString)()
        or2 = getattr(self, 'fabricar' + otraOrString)()
        
        pt = Puerta(lado1, lado2)
        
        lado1.ponerElementoEn(pt,or1) 
        lado2.ponerElementoEn(pt,or2)



director=Director()
director.procesar('D:\OneDrive - Universidad de Castilla-La Mancha\UCLM\Tercero\2do cuatri\Diseño de Software\VisualCodeLaberinto\laberinto2hab.json')

director.diccionario
