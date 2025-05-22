class Bala:
    def __init__(self, x, y, v=20, vx=0, bg_x=0, bg_y=0):
        self.x, self.y, self.v = x, y, v
        self.vx = vx  # Componente horizontal de la velocidad
        self.bg_x = bg_x
        self.bg_y = bg_y

    def moure(self):
        self.y -= self.v
        self.x += self.vx  # Mover en la dirección horizontal

    def pinta(self, w):
        if self.bg_x <= self.x <= self.bg_x + 1000 and self.bg_y <= self.y <= self.bg_y + 650:
            w.create_line(self.x, self.y, self.x, self.y - 13, width=1, fill="fuchsia")

    def xoc_enemic(self, enemic):
        # Aumentar el área de impacto para enemigos rojos y lilas
        if enemic.f in [2, 4]:
            area_impacto = 10  # Aumentar el área de impacto
        else:
            area_impacto = 0

        if (enemic.x - area_impacto <= self.x <= enemic.x + enemic.ample + area_impacto and 
            enemic.y - area_impacto <= self.y <= enemic.y + enemic.altura + area_impacto):
            return True
        return False

    def xoc_nau(self, nau):
        if (nau.x <= self.x <= nau.x + nau.ample and 
            nau.y <= self.y <= nau.y + nau.altura):
            return True
        return False