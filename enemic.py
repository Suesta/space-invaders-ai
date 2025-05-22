class Enemic:
    def __init__(self, x, y, ample, altura, v=1, f=1, bg_x=0, bg_y=0):
        self.x, self.y, self.ample, self.altura = x, y, ample, altura
        self.v, self.f = v, f
        self.bg_x = bg_x
        self.bg_y = bg_y

    def moure(self, balas):
        self.x += self.v
        # Cambiar de dirección si alcanza los bordes del área centrada
        if self.x <= self.bg_x or self.x + self.ample >= self.bg_x + 1000:
            self.v = -self.v

    def pinta(self, w):
        # Dibujar una nave apuntando hacia abajo con más detalles
        points = [
            self.x + self.ample / 2, self.y + self.altura * 3/8,  # Punto central inferior
            self.x + self.ample * 3/4, self.y + self.altura,  # Punto casi inferior derecho
            self.x + self.ample, self.y,  # Punto superior derecho
            self.x + self.ample * 3/4, self.y + self.altura * 3/8,  # Punto casi superior derecho
            self.x + self.ample / 2, self.y,  # Punto central superior
            self.x + self.ample * 1/4, self.y + self.altura * 3/8,  # Punto casi superior izquierdo
            self.x, self.y,  # Punto superior izquierdo
            self.x + self.ample * 1/4, self.y + self.altura  # Punto casi inferior izquierdo
        ]
        if self.f == 1:
            color = "green"
        elif self.f == 2:
            color = "orange"
        elif self.f == 3:
            color = "red"
        elif self.f == 4:
            color = "purple"
        elif self.f == 5:
            color = "black"
        else:
            color = "white"
        w.create_polygon(points, fill=color, outline="black")

    def dividir(self):
        if self.f > 1:
            nuevo_f = self.f - 1
            if nuevo_f == 1:
                nuevo_ample, nuevo_altura, nuevo_v = 35, 20, 3
            elif nuevo_f == 2:
                nuevo_ample, nuevo_altura, nuevo_v = 28, 18, 4.5
            elif nuevo_f == 3:
                nuevo_ample, nuevo_altura, nuevo_v = 26, 16, 6
            elif nuevo_f == 4:
                nuevo_ample, nuevo_altura, nuevo_v = 26, 16, 7
            else:
                nuevo_ample, nuevo_altura, nuevo_v = self.ample / 2, self.altura / 2, self.v

            # Asegurarse de que los enemigos divididos no se salgan del área centrada
            nuevo_x1 = max(self.bg_x, min(self.x, self.bg_x + 1000 - nuevo_ample))
            nuevo_x2 = max(self.bg_x, min(self.x + nuevo_ample, self.bg_x + 1000 - nuevo_ample))

            return [
                Enemic(nuevo_x1, self.y, nuevo_ample, nuevo_altura, nuevo_v, nuevo_f, bg_x=self.bg_x, bg_y=self.bg_y),
                Enemic(nuevo_x2, self.y, nuevo_ample, nuevo_altura, -nuevo_v, nuevo_f, bg_x=self.bg_x, bg_y=self.bg_y)
            ]
        return []