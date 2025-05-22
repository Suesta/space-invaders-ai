class Nau:
    def __init__(self, x, y, ample, altura, v=1, hp=3, img=None, bg_x=0, bg_y=0):
        self.x, self.y, self.ample, self.altura = x, y, ample, altura
        self.v = v
        self.hp = hp
        self.img = img  # Añadir soporte para imágenes
        self.last_shot_time = 0  # Tiempo del último disparo
        self.bg_x = bg_x
        self.bg_y = bg_y

    def moure(self, direccio_x, direccio_y):
        self.x += direccio_x * self.v
        self.y += direccio_y * self.v
        if self.x < self.bg_x:
            self.x = self.bg_x
        elif self.x + self.ample > self.bg_x + 1000:  # Márgenes de la pantalla
            self.x = self.bg_x + 1000 - self.ample
        if self.y < self.bg_y + 325:  # Limitar a la mitad inferior de la pantalla
            self.y = self.bg_y + 325
        elif self.y + self.altura > self.bg_y + 650:  # Márgenes de la pantalla
            self.y = self.bg_y + 650 - self.altura

    def pinta(self, w):
        if self.img:
            w.create_image(self.x, self.y, anchor="nw", image=self.img)
        else:
            w.create_rectangle(self.x, self.y, self.x + self.ample, self.y + self.altura, fill="blue")
            x_medio = self.x + self.ample / 2
            w.create_line(x_medio, self.y, x_medio, self.y - self.ample / 3, width=10, fill="blue")