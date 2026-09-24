import tkinter as tk
from tkinter import messagebox
import math


# =========================================================
# DATOS DE LA PIEZA
# =========================================================

# Ejemplo de pieza en forma de L
puntos_originales = [
    (0, 0),
    (4, 0),
    (4, 1),
    (1, 1),
    (1, 4),
    (0, 4)
]


# =========================================================
# VENTANA PRINCIPAL
# =========================================================

ventana = tk.Tk()

ventana.title("Transformaciones Lineales - CNC")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.configure(bg="#F4F6F8")


# =========================================================
# TÍTULO
# =========================================================

titulo = tk.Label(
    ventana,
    text="TRANSFORMACIONES LINEALES — CNC",
    font=("Arial", 22, "bold"),
    bg="#F4F6F8",
    fg="#1F2937"
)

titulo.pack(pady=15)


# =========================================================
# CONTENEDOR PRINCIPAL
# =========================================================

contenedor = tk.Frame(
    ventana,
    bg="#F4F6F8"
)

contenedor.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


# =========================================================
# PANEL IZQUIERDO
# =========================================================

panel_izquierdo = tk.Frame(
    contenedor,
    bg="white",
    width=300,
    height=570,
    relief="solid",
    borderwidth=1
)

panel_izquierdo.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

panel_izquierdo.pack_propagate(False)


# Título del panel

label_menu = tk.Label(
    panel_izquierdo,
    text="TRANSFORMACIONES",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1F2937"
)

label_menu.pack(pady=(25, 20))


# =========================================================
# BOTÓN ROTACIÓN
# =========================================================

def abrir_rotacion():

    ventana_rotacion = tk.Toplevel(ventana)

    ventana_rotacion.title("Rotación")
    ventana_rotacion.geometry("350x350")
    ventana_rotacion.resizable(False, False)

    tk.Label(
        ventana_rotacion,
        text="ROTACIÓN",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        ventana_rotacion,
        text="Ángulo:"
    ).pack()

    entrada_angulo = tk.Entry(
        ventana_rotacion,
        width=20
    )

    entrada_angulo.pack(pady=5)

    tk.Label(
        ventana_rotacion,
        text="Dirección:"
    ).pack(pady=(15, 0))

    direccion = tk.StringVar(
        value="Antihorario"
    )

    tk.Radiobutton(
        ventana_rotacion,
        text="Antihorario",
        variable=direccion,
        value="Antihorario"
    ).pack()

    tk.Radiobutton(
        ventana_rotacion,
        text="Horario",
        variable=direccion,
        value="Horario"
    ).pack()

    tk.Label(
        ventana_rotacion,
        text="Centro de rotación (X, Y):"
    ).pack(pady=(15, 5))

    frame_centro = tk.Frame(
        ventana_rotacion
    )

    frame_centro.pack()

    entrada_x = tk.Entry(
        frame_centro,
        width=8
    )

    entrada_x.pack(
        side="left",
        padx=5
    )

    entrada_y = tk.Entry(
        frame_centro,
        width=8
    )

    entrada_y.pack(
        side="left",
        padx=5
    )

    def aplicar():

        try:
            angulo = float(
                entrada_angulo.get()
            )

            cx = float(
                entrada_x.get()
            )

            cy = float(
                entrada_y.get()
            )

            if direccion.get() == "Horario":
                angulo = -angulo

            theta = math.radians(angulo)

            coseno = math.cos(theta)
            seno = math.sin(theta)

            nuevos_puntos = []

            for x, y in puntos_originales:

                # Trasladar al centro
                x1 = x - cx
                y1 = y - cy

                # Matriz de rotación
                x2 = x1 * coseno - y1 * seno
                y2 = x1 * seno + y1 * coseno

                # Regresar
                x2 += cx
                y2 += cy

                nuevos_puntos.append(
                    (x2, y2)
                )

            messagebox.showinfo(
                "Rotación",
                "Rotación aplicada correctamente."
            )

            ventana_rotacion.destroy()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingresa valores numéricos."
            )

    tk.Button(
        ventana_rotacion,
        text="APLICAR ROTACIÓN",
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        height=2,
        command=aplicar
    ).pack(pady=25)


boton_rotacion = tk.Button(
    panel_izquierdo,
    text="⟳  ROTACIÓN",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    width=25,
    height=2,
    cursor="hand2",
    command=abrir_rotacion
)

boton_rotacion.pack(pady=8)


# =========================================================
# BOTÓN HOMOTECIA
# =========================================================

def abrir_homotecia():

    ventana_homotecia = tk.Toplevel(ventana)

    ventana_homotecia.title("Homotecia")
    ventana_homotecia.geometry("350x330")
    ventana_homotecia.resizable(False, False)

    tk.Label(
        ventana_homotecia,
        text="HOMOTECIA",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        ventana_homotecia,
        text="Factor de escala:"
    ).pack()

    entrada_factor = tk.Entry(
        ventana_homotecia,
        width=20
    )

    entrada_factor.pack(pady=5)

    tk.Label(
        ventana_homotecia,
        text="Centro (X, Y):"
    ).pack(pady=(20, 5))

    frame_centro = tk.Frame(
        ventana_homotecia
    )

    frame_centro.pack()

    entrada_x = tk.Entry(
        frame_centro,
        width=8
    )

    entrada_x.pack(
        side="left",
        padx=5
    )

    entrada_y = tk.Entry(
        frame_centro,
        width=8
    )

    entrada_y.pack(
        side="left",
        padx=5
    )

    def aplicar():

        try:

            factor = float(
                entrada_factor.get()
            )

            cx = float(
                entrada_x.get()
            )

            cy = float(
                entrada_y.get()
            )

            nuevos_puntos = []

            for x, y in puntos_originales:

                x2 = cx + factor * (x - cx)
                y2 = cy + factor * (y - cy)

                nuevos_puntos.append(
                    (x2, y2)
                )

            messagebox.showinfo(
                "Homotecia",
                "Homotecia aplicada correctamente."
            )

            ventana_homotecia.destroy()

        except ValueError:

            messagebox.showerror(
                "Error",
                "Ingresa valores numéricos."
            )

    tk.Button(
        ventana_homotecia,
        text="APLICAR HOMOTECIA",
        bg="#059669",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        height=2,
        command=aplicar
    ).pack(pady=25)


boton_homotecia = tk.Button(
    panel_izquierdo,
    text="↔  HOMOTECIA",
    font=("Arial", 11, "bold"),
    bg="#059669",
    fg="white",
    activebackground="#047857",
    activeforeground="white",
    width=25,
    height=2,
    cursor="hand2",
    command=abrir_homotecia
)

boton_homotecia.pack(pady=8)


# =========================================================
# BOTÓN REFLEXIÓN
# =========================================================

def abrir_reflexion():

    ventana_reflexion = tk.Toplevel(ventana)

    ventana_reflexion.title("Reflexión")
    ventana_reflexion.geometry("350x300")
    ventana_reflexion.resizable(False, False)

    tk.Label(
        ventana_reflexion,
        text="REFLEXIÓN",
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    tk.Label(
        ventana_reflexion,
        text="Selecciona la línea:"
    ).pack()

    linea = tk.StringVar(
        value="Eje X"
    )

    opciones = [
        "Eje X",
        "Eje Y",
        "Recta Y = X",
        "Recta Y = -X"
    ]

    menu = tk.OptionMenu(
        ventana_reflexion,
        linea,
        *opciones
    )

    menu.config(
        width=20
    )

    menu.pack(pady=15)

    def aplicar():

        seleccion = linea.get()

        if seleccion == "Eje X":

            nuevos_puntos = [
                (x, -y)
                for x, y in puntos_originales
            ]

        elif seleccion == "Eje Y":

            nuevos_puntos = [
                (-x, y)
                for x, y in puntos_originales
            ]

        elif seleccion == "Recta Y = X":

            nuevos_puntos = [
                (y, x)
                for x, y in puntos_originales
            ]

        else:

            nuevos_puntos = [
                (-y, -x)
                for x, y in puntos_originales
            ]

        messagebox.showinfo(
            "Reflexión",
            "Reflexión aplicada correctamente."
        )

        ventana_reflexion.destroy()

    tk.Button(
        ventana_reflexion,
        text="APLICAR REFLEXIÓN",
        bg="#7C3AED",
        fg="white",
        font=("Arial", 10, "bold"),
        width=20,
        height=2,
        command=aplicar
    ).pack(pady=25)


boton_reflexion = tk.Button(
    panel_izquierdo,
    text="↔  REFLEXIÓN",
    font=("Arial", 11, "bold"),
    bg="#7C3AED",
    fg="white",
    activebackground="#6D28D9",
    activeforeground="white",
    width=25,
    height=2,
    cursor="hand2",
    command=abrir_reflexion
)

boton_reflexion.pack(pady=8)


# =========================================================
# SEPARADOR
# =========================================================

tk.Frame(
    panel_izquierdo,
    height=2,
    bg="#E5E7EB"
).pack(
    fill="x",
    padx=25,
    pady=20
)


# =========================================================
# BOTÓN VER ORIGINAL
# =========================================================

def ver_original():

    dibujar_pieza(
        puntos_originales
    )


boton_original = tk.Button(
    panel_izquierdo,
    text="VER ORIGINAL",
    font=("Arial", 10, "bold"),
    bg="#6B7280",
    fg="white",
    width=25,
    height=2,
    cursor="hand2",
    command=ver_original
)

boton_original.pack(pady=6)


# =========================================================
# BOTÓN NUEVA PIEZA
# =========================================================

def nueva_pieza():

    messagebox.showinfo(
        "Nueva pieza",
        "Aquí podrás ingresar una nueva pieza."
    )


boton_nueva = tk.Button(
    panel_izquierdo,
    text="NUEVA PIEZA",
    font=("Arial", 10, "bold"),
    bg="#374151",
    fg="white",
    width=25,
    height=2,
    cursor="hand2",
    command=nueva_pieza
)

boton_nueva.pack(pady=6)


# =========================================================
# PANEL DERECHO - PLANO CARTESIANO
# =========================================================

panel_derecho = tk.Frame(
    contenedor,
    bg="white",
    relief="solid",
    borderwidth=1
)

panel_derecho.pack(
    side="right",
    fill="both",
    expand=True
)


# Título del plano

label_plano = tk.Label(
    panel_derecho,
    text="PLANO CARTESIANO",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="#1F2937"
)

label_plano.pack(
    pady=10
)


# =========================================================
# CANVAS
# =========================================================

canvas = tk.Canvas(
    panel_derecho,
    width=820,
    height=500,
    bg="white",
    highlightthickness=0
)

canvas.pack(
    padx=10,
    pady=10
)


# =========================================================
# DIBUJAR PLANO CARTESIANO
# =========================================================

def dibujar_plano():

    canvas.delete("all")

    ancho = 820
    alto = 500

    centro_x = ancho // 2
    centro_y = alto // 2

    escala = 45

    # Cuadrícula vertical
    for x in range(
        centro_x % escala,
        ancho,
        escala
    ):

        canvas.create_line(
            x,
            0,
            x,
            alto,
            fill="#E5E7EB"
        )

    # Cuadrícula horizontal
    for y in range(
        centro_y % escala,
        alto,
        escala
    ):

        canvas.create_line(
            0,
            y,
            ancho,
            y,
            fill="#E5E7EB"
        )

    # Eje X
    canvas.create_line(
        0,
        centro_y,
        ancho,
        centro_y,
        fill="#374151",
        width=2
    )

    # Eje Y
    canvas.create_line(
        centro_x,
        0,
        centro_x,
        alto,
        fill="#374151",
        width=2
    )

    # Números X
    for i in range(-9, 10):

        if i == 0:
            continue

        x = centro_x + i * escala

        canvas.create_text(
            x,
            centro_y + 15,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )

    # Números Y
    for i in range(-5, 6):

        if i == 0:
            continue

        y = centro_y - i * escala

        canvas.create_text(
            centro_x + 15,
            y,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )

    # Etiquetas de los ejes

    canvas.create_text(
        ancho - 15,
        centro_y - 15,
        text="X",
        font=("Arial", 11, "bold"),
        fill="#374151"
    )

    canvas.create_text(
        centro_x + 15,
        15,
        text="Y",
        font=("Arial", 11, "bold"),
        fill="#374151"
    )


# =========================================================
# DIBUJAR PIEZA
# =========================================================

def dibujar_pieza(puntos):

    dibujar_plano()

    centro_x = 820 // 2
    centro_y = 500 // 2

    escala = 45

    coordenadas = []

    for x, y in puntos:

        px = centro_x + x * escala
        py = centro_y - y * escala

        coordenadas.append(
            (px, py)
        )

    # Dibujar polígono

    canvas.create_polygon(
        coordenadas,
        fill="#93C5FD",
        outline="#2563EB",
        width=3
    )

    # Dibujar vértices

    for i, (px, py) in enumerate(coordenadas):

        canvas.create_oval(
            px - 5,
            py - 5,
            px + 5,
            py + 5,
            fill="#2563EB",
            outline="white"
        )

        canvas.create_text(
            px + 12,
            py - 10,
            text=f"P{i + 1}",
            font=("Arial", 9, "bold"),
            fill="#1F2937"
        )


# =========================================================
# MOSTRAR PIEZA AL INICIAR
# =========================================================

dibujar_pieza(
    puntos_originales
)


# =========================================================
# EJECUTAR
# =========================================================

ventana.mainloop()