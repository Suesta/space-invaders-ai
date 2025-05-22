import random

class Heart:
    def __init__(self, x=None, y=None, lifetime=None, bg_x=0, bg_y=0):
        self.ample = 15
        self.altura = 15
        self.bg_x = bg_x
        self.bg_y = bg_y
        self.x = x if x is not None else random.randint(bg_x, bg_x + 1000 - self.ample)
        self.y = y if y is not None else random.randint(bg_y, bg_y + 50 - self.altura)  # Parte superior del tablero
        self.lifetime = lifetime if lifetime is not None else random.randint(80, 140)  # Tiempo de vida aleatorio entre 4 y 7 segundos

    def pinta(self, w):
        # Dibujar un corazón con forma de corazón y de color azul
        points = [
            self.x + self.ample / 2, self.y + self.altura,  # Punto inferior
            self.x + self.ample, self.y + self.altura / 2,  # Punto derecho
            self.x + self.ample * 3/4, self.y,  # Punto superior derecho
            self.x + self.ample / 2, self.y + self.altura / 4,  # Punto medio superior
            self.x + self.ample / 4, self.y,  # Punto superior izquierdo
            self.x, self.y + self.altura / 2  # Punto izquierdo
        ]
        w.create_polygon(points, fill="red", outline="red")

    def xoc_bala(self, bala):
        # Ajustar el área de impacto para mejorar la detección de colisiones
        margen = 2  # Margen para ajustar el área de impacto
        return (self.x - margen < bala.x < self.x + self.ample + margen) and (self.y - margen < bala.y < self.y + self.altura + margen)

    def decrementar_vida(self):
        self.lifetime -= 1
        return self.lifetime <= 0