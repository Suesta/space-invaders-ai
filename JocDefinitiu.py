import time
import keyboard
import random
from PIL import Image, ImageTk
from tkinter import Tk, Canvas
from enemic import Enemic # type: ignore
from nau import Nau # type: ignore
from bala import Bala # type: ignore
from heart import Heart # type: ignore

tk = Tk()
canvas_width = 1540
canvas_height = 790
w = Canvas(tk, width=canvas_width, height=canvas_height, bg="black")
w.pack()

# Cargar la imagen de fondo
bg_img_path = "fondo1.png"
bg_img = Image.open(bg_img_path)
bg_img = bg_img.resize((1000, 650), Image.Resampling.LANCZOS)  # Redimensionar la imagen de fondo
bg_img_tk = ImageTk.PhotoImage(bg_img)

# Coordenadas para centrar la imagen de fondo
bg_x = (canvas_width - 1000) // 2
bg_y = (canvas_height - 650) // 2

# Cargar la imagen localmente y quitar el fondo
img_path = "nauImag.png"
img = Image.open(img_path)
img = img.resize((40, 50), Image.Resampling.LANCZOS)  # Redimensionar la imagen
nau_img = ImageTk.PhotoImage(img)

enemics = []
hearts = []

nau = Nau(bg_x + 500 - 20, bg_y + 550, 40, 50, 15, 3, img=nau_img, bg_x=bg_x, bg_y=bg_y)
vidas_extra = 0  # Contador de vidas adicionales obtenidas de los corazones
vidas_extra_obtenidas = False  # Variable para rastrear si se han obtenido las 3 vidas adicionales

def generar_enemics(niv):
    enemics1 = []
    if niv == 0:
        enemics1 = [
            Enemic(bg_x + 50, bg_y + 50, 28, 18, 4.5, 2, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 50, bg_y + 100, 35, 20, 3, 1, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 550, bg_y + 120, 35, 20, -3, 1, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 750, bg_y + 150, 35, 20, -3, 1, bg_x=bg_x, bg_y=bg_y)
        ]
        w.create_text(bg_x + 500, bg_y + 325, text="NIVEL 1", font=("Arial", 30), fill="green")
    elif niv == 1:
        enemics1 = [
            Enemic(bg_x + 150, bg_y + 50, 26, 16, 6, 3, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 50, bg_y + 90, 28, 18, -4.5, 2, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 550, bg_y + 130, 28, 18, 4.5, 2, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 750, bg_y + 170, 28, 18, -4.5, 2, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 550, bg_y + 180, 28, 18, 4.5, 2, bg_x=bg_x, bg_y=bg_y)
        ]
        w.create_text(bg_x + 500, bg_y + 325, text="NIVEL 2", font=("Arial", 30), fill="yellow")
    elif niv == 2:
        enemics1 = [
            Enemic(bg_x + 50, bg_y + 40, 26, 16, 7, 4, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 450, bg_y + 80, 26, 16, -6, 3, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 250, bg_y + 100, 26, 16, 6, 3, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 250, bg_y + 120, 26, 16, -6, 3, bg_x=bg_x, bg_y=bg_y),
        ]
        w.create_text(bg_x + 500, bg_y + 325, text="NIVEL 3", font=("Arial", 30), fill="red")
    elif niv == 3:
        enemics1 = [
            Enemic(bg_x + 50, bg_y + 40, 26, 16, 7, 4, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 450, bg_y + 80, 26, 16, -7, 4, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 250, bg_y + 120, 26, 16, -6, 3, bg_x=bg_x, bg_y=bg_y),
        ]
        w.create_text(bg_x + 500, bg_y + 325, text="NIVEL 4", font=("Arial", 30), fill="purple")
    elif niv == 4:
        enemics1 = [
            Enemic(bg_x + 50, bg_y + 40, 28, 18, 9, 5, bg_x=bg_x, bg_y=bg_y),
            Enemic(bg_x + 250, bg_y + 80, 26, 16, -7, 4, bg_x=bg_x, bg_y=bg_y),
        ]
        w.create_text(bg_x + 500, bg_y + 325, text="NIVEL 5", font=("Arial", 30), fill="white")
    else:
        w.create_text(bg_x + 500, bg_y + 325, text="¡¡VICTORIA!!", font=("Arial", 30), fill="blue")
        w.update()
        time.sleep(2)
        exit()
    
    w.update()
    time.sleep(2)
    return enemics1

niv = 0
enemics = generar_enemics(niv)

balas = []
balas_e = []

while True:
    w.delete("all")

    # Dibujar la imagen de fondo centrada
    w.create_image(bg_x, bg_y, anchor="nw", image=bg_img_tk)

    # MARGENES centrados
    w.create_rectangle(bg_x, bg_y, bg_x + 1000, bg_y + 650, outline="blue", width=5)


    # PAUSA
    if keyboard.is_pressed("p"):
        w.create_text(bg_x + 500, bg_y + 325, text="PAUSA", font=("Arial", 30), fill="blue")  # Mostrar mensaje en pantalla
        w.create_text(bg_x + 500, bg_y + 15, text="'p' para seguir jugando", font=("Arial", 20), fill="blue")
        w.update()
        while True:
            time.sleep(0.1)
            if keyboard.is_pressed("p"):  # Salir del bucle si se presiona "p" otra vez
                break

    # SUBIR NIVEL + GENERAR ENEMIGOS
    if not enemics:  # Si no quedan enemigos
        niv += 1
        nau.hp += 1
        nau.x, nau.y = bg_x + 500 - nau.ample / 2, bg_y + 550
        balas.clear()
        balas_e.clear()
        hearts.clear()
        vidas_extra = 0  # Reiniciar el contador de vidas adicionales
        vidas_extra_obtenidas = False  # Reiniciar el rastreador de vidas adicionales
        enemics = generar_enemics(niv)

    # Generar corazones aleatorios si no hay ninguno en pantalla y no se han obtenido las 3 vidas adicionales
    if not hearts and not vidas_extra_obtenidas and random.random() < 0.01:  # Probabilidad de generar un corazón
        hearts.append(Heart(bg_x=bg_x, bg_y=bg_y))

    pausa_text = w.create_text(bg_x + 500, bg_y + 15, text="'p' para pausa", font=("Arial", 15), fill="blue")

    # aplicar moviments als nostres elements

    if keyboard.is_pressed("left arrow"):
        nau.moure(-1, 0)
    if keyboard.is_pressed("right arrow"):
        nau.moure(1, 0)
    if keyboard.is_pressed("up arrow"):
        nau.moure(0, -1)
    if keyboard.is_pressed("down arrow"):
        nau.moure(0, 1)
    vida_text = w.create_text(bg_x + 850, bg_y + 20, text="VIDAS: " + str(nau.hp), font=("Arial", 20), fill="red")

    # Limitar la cadencia de disparo de nau
    current_time = time.time()
    if keyboard.is_pressed("space") and current_time - nau.last_shot_time > 1:  #segundos entre disparos
        balas.append(Bala(nau.x + nau.ample / 2, nau.y, bg_x=bg_x, bg_y=bg_y))
        nau.last_shot_time = current_time

    for b in balas:
        b.moure()
        for e in enemics:
            if b.xoc_enemic(e):
                nuevos_enemics = e.dividir()
                enemics.extend(nuevos_enemics)
                enemics.remove(e)
                balas.remove(b)
                break
        for h in hearts:
            if h.xoc_bala(b):
                if vidas_extra < 3:  # Limitar las vidas adicionales obtenidas de los corazones a 3
                    nau.hp += 1
                    vidas_extra += 1
                    if vidas_extra == 3:
                        vidas_extra_obtenidas = True
                hearts.remove(h)
                balas.remove(b)
                break

    for e in enemics:
        e.moure(balas)
        # Lógica de disparo de los enemigos
        if random.random() < 0.1:
            if e.f == 4 or e.f == 5:
                dx, dy = nau.x + nau.ample / 2 - (e.x + e.ample / 2), nau.y - (e.y + e.altura)
                distancia = (dx ** 2 + dy ** 2) ** 0.5
                vx, vy = dx / distancia * 30, dy / distancia * 30  # Velocidad de la bala
                balas_e.append(Bala(e.x + e.ample / 2, e.y + e.altura, v=-vy, vx=vx, bg_x=bg_x, bg_y=bg_y))
            else:
                balas_e.append(Bala(e.x + e.ample / 2, e.y + e.altura, v=-30, bg_x=bg_x, bg_y=bg_y))

    for b in balas_e:
        b.moure()
        if b.xoc_nau(nau):
            nau.hp -= 1
            balas_e.remove(b)  # Elimina la bala
            w.itemconfig(vida_text, text="VIDAS: " + str(nau.hp))
            if nau.hp <= 0:
                w.create_text(bg_x + 500, bg_y + 325, text="GAME OVER", font=("Arial", 30), fill="red")  # Mostrar mensaje en pantalla
                w.update()
                time.sleep(2)  # Pausa para mostrar el mensaje
                exit()

    # Decrementar el tiempo de vida de los corazones y eliminarlos si es necesario
    for h in hearts[:]:
        if h.decrementar_vida():
            hearts.remove(h)

    # pintar elements
    nau.pinta(w)
    for e in enemics:
        e.pinta(w)
    for b in balas:
        b.pinta(w)
    for b in balas_e:
        b.pinta(w)
    for h in hearts:
        h.pinta(w)
    w.update()

    # pausa
    time.sleep(50 / 1000)  # pausa durant els segons especificats