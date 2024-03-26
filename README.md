# Maze Game 2024
Proyecto del laberinto del curso 23-24

Prompt Inicial:
```
Escribe un programa en Python con los siguientes objetos: Laberinto, Pared, Puerta y Habitación.
El objeto Laberinto tiene una colección de objetos Habitación.
El objeto Habitación tiene cuatro lados (norte, este, oeste, sur), inicialmente cada lado es un objeto Pared.
El objeto Puerta tiene dos lados que podrían ser objetos Habitación.
El objeto Laberinto tiene una operación añadirHabitación con un objeto Habitación como parámetro.

```
Prompt del Decorator:
```
Incluye una nueva clase llamada Decorator. Esta nueva clase es una subclase de ElementoMapa.
```	
Prompt del Composite:
```	
Se aplica el patrón de diseño Composite a esta solución: ElementoMapa es la clase Component, Contenedor es una subclase de ElementoMapa y Habitación es una subclase de la clase Contenedor.
Una nueva clase Hoja es una subclase de ElementoMapa.
La clase Decorator ahora es una subclase de Hoja.
```
Prompt para crear un laberinto de 4 habitaciones y 4 bichos
```
Duplica la función crearLaberinto2habFM en Juego. Cambia el nombre del método duplicado a crear4hab2BichosFM, que creará 4 habitaciones. La Habitación 1 se conecta con la Habitación 2 mediante una Puerta en el sur de la Habitación 1. La Habitación 1 se conecta con la Habitación 3 por el este de la Habitación 1. La Habitación 3 se conecta con la Habitación 4 por el sur de la Habitación 3. La Habitación 2 se conecta con la Habitación 4 por el este de la Habitación 3. También incluye 4 instancias de bichos (clase Bicho), dos en modo agresivo y dos perezosos. Los bichos agresivos estarán en las habitaciones 1 y 3. Los bichos perezosos estarán en las habitaciones 2 y 4.
```
Prompt para corregir el resultado:
```
Utiliza los métodos existentes en Juego para crear bichos agresivos y perezosos.
```
