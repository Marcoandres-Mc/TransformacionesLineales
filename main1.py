import tkinter as tk
from tkinter import ttk, messagebox
import math


# CONFIGURACIÓN

ANCHO_PLANO = 790
ALTO_PLANO = 530
ESCALA = 40

COLOR_FONDO = "#F4F6F8"
COLOR_PANEL = "#FFFFFF"
COLOR_PRIMARIO = "#2563EB"
COLOR_PRIMARIO_HOVER = "#1D4ED8"
COLOR_SECUNDARIO = "#6B7280"
COLOR_TEXTO = "#1F2937"
COLOR_BORDE = "#D1D5DB"


# FIGURA ACTUAL

puntos = []


# VENTANA

ventana = tk.Tk()

ventana.title("Transformaciones Lineales - CNC")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.configure(bg=COLOR_FONDO)


# FUNCIONES DEL PLANO

def convertir_pantalla(x, y):
    """
    Convierte coordenadas matemáticas
    a coordenadas del Canvas.
    """

    centro_x = ANCHO_PLANO // 2
    centro_y = ALTO_PLANO // 2

    pantalla_x = centro_x + x * ESCALA
    pantalla_y = centro_y - y * ESCALA

    return pantalla_x, pantalla_y


def dibujar_plano():

    canvas.delete("all")

    centro_x = ANCHO_PLANO // 2
    centro_y = ALTO_PLANO // 2

    # CUADRÍCULA


    for x in range(centro_x % ESCALA, ANCHO_PLANO, ESCALA):

        canvas.create_line(
            x,
            0,
            x,
            ALTO_PLANO,
            fill="#E5E7EB"
        )

    for y in range(centro_y % ESCALA, ALTO_PLANO, ESCALA):

        canvas.create_line(
            0,
            y,
            ANCHO_PLANO,
            y,
            fill="#E5E7EB"
        )

    # EJE X
    canvas.create_line(
        0,
        centro_y,
        ANCHO_PLANO,
        centro_y,
        fill="#374151",
        width=2
    )

    # EJE Y
    
    canvas.create_line(
        centro_x,
        0,
        centro_x,
        ALTO_PLANO,
        fill="#374151",
        width=2
    )

    # NÚMEROS X

    for i in range(-9, 10):

        if i == 0:
            continue

        x = centro_x + i * ESCALA

        canvas.create_text(
            x,
            centro_y + 14,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )


    # NÚMEROS Y


    for i in range(-6, 7):

        if i == 0:
            continue

        y = centro_y - i * ESCALA

        canvas.create_text(
            centro_x + 14,
            y,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )

    # LETRAS DE LOS EJES

    canvas.create_text(
        ANCHO_PLANO - 15,
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


def dibujar_figura():

    dibujar_plano()

    if len(puntos) == 0:
        return

    coordenadas = []

    for x, y in puntos:

        px, py = convertir_pantalla(x, y)

        coordenadas.append(
            (px, py)
        )

    # POLÍGONO

    if len(coordenadas) >= 3:

        canvas.create_polygon(
            coordenadas,
            fill="#93C5FD",
            outline="#2563EB",
            width=3
        )

    # PUNTOS

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
            px + 14,
            py - 12,
            text=f"P{i + 1}",
            font=("Arial", 9, "bold"),
            fill="#1F2937"
        )


# FUNCIONES DE FIGURAS

def cargar_figura(nombre):

    global puntos

    if nombre == "Triángulo":

        puntos = [
            (0, 0),
            (4, 0),
            (2, 3)
        ]

    elif nombre == "Cuadrado":

        puntos = [
            (0, 0),
            (4, 0),
            (4, 4),
            (0, 4)
        ]

    elif nombre == "Rectángulo":

        puntos = [
            (0, 0),
            (6, 0),
            (6, 3),
            (0, 3)
        ]

    elif nombre == "Pentágono":

        puntos = [
            (0, 0),
            (4, 0),
            (5, 3),
            (2, 5),
            (-1, 3)
        ]

    elif nombre == "Figura L":

        puntos = [
            (0, 0),
            (4, 0),
            (4, 1),
            (1, 1),
            (1, 4),
            (0, 4)
        ]

    dibujar_figura()



# 1. COORDENADAS

def crear_punto():

    global puntos

    try:

        x = float(entrada_x.get())
        y = float(entrada_y.get())

        puntos.append(
            (x, y)
        )

        dibujar_figura()

        entrada_x.delete(0, tk.END)
        entrada_y.delete(0, tk.END)

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingresa valores numéricos para X e Y."
        )



# 2. FIGURAS PREESTABLECIDAS


def aceptar_figura():

    nombre = figura_seleccionada.get()

    if nombre == "Seleccionar figura":

        messagebox.showwarning(
            "Advertencia",
            "Selecciona una figura."
        )

        return

    cargar_figura(nombre)



# 3. REFLEXIONES

def reflexion(tipo):

    global puntos

    if not puntos:

        messagebox.showwarning(
            "Advertencia",
            "Primero debes crear o seleccionar una figura."
        )

        return

    nuevos_puntos = []

    for x, y in puntos:

        if tipo == "EJE X":

            nuevo_x = x
            nuevo_y = -y

        elif tipo == "EJE Y":

            nuevo_x = -x
            nuevo_y = y

        elif tipo == "BISECTRIZ":

            nuevo_x = y
            nuevo_y = x

        elif tipo == "ORIGEN":

            nuevo_x = -x
            nuevo_y = -y

        elif tipo == "Y = -X":

            nuevo_x = -y
            nuevo_y = -x

        nuevos_puntos.append(
            (nuevo_x, nuevo_y)
        )

    puntos = nuevos_puntos

    dibujar_figura()


# 4. HOMOTECIA

def aplicar_homotecia():

    global puntos

    if not puntos:

        messagebox.showwarning(
            "Advertencia",
            "Primero debes crear o seleccionar una figura."
        )

        return

    try:

        cx = float(hom_x.get())
        cy = float(hom_y.get())
        k = float(hom_k.get())

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingresa valores numéricos."
        )

        return

    nuevos_puntos = []

    for x, y in puntos:

        nuevo_x = x * k + cx
        nuevo_y = y * k + cy

        nuevos_puntos.append(
            (nuevo_x, nuevo_y)
        )

    puntos = nuevos_puntos

    dibujar_figura()


# 5. ROTACIÓN


def aplicar_rotacion():

    global puntos

    if not puntos:

        messagebox.showwarning(
            "Advertencia",
            "Primero debes crear o seleccionar una figura."
        )

        return

    try:

        angulo = float(
            entrada_angulo.get()
        )

        cx = float(
            rot_x.get()
        )

        cy = float(
            rot_y.get()
        )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Ingresa valores numéricos."
        )

        return

    theta = math.radians(
        angulo
    )

    coseno = math.cos(theta)
    seno = math.sin(theta)

    nuevos_puntos = []

    for x, y in puntos:

        # 1. Trasladar el centro al origen

        x1 = x - cx
        y1 = y - cy

        # 2. Matriz de rotación


        x2 = (
            x1 * coseno
            - y1 * seno
        )

        y2 = (
            x1 * seno
            + y1 * coseno
        )


        # 3. Regresar al centro original

        nuevo_x = x2 + cx
        nuevo_y = y2 + cy

        nuevos_puntos.append(
            (nuevo_x, nuevo_y)
        )

    puntos = nuevos_puntos

    dibujar_figura()



# 6. LIMPIAR

def limpiar():

    global puntos

    puntos = []

    entrada_x.delete(
        0,
        tk.END
    )

    entrada_y.delete(
        0,
        tk.END
    )

    hom_x.delete(
        0,
        tk.END
    )

    hom_y.delete(
        0,
        tk.END
    )

    hom_k.delete(
        0,
        tk.END
    )

    entrada_angulo.delete(
        0,
        tk.END
    )

    rot_x.delete(
        0,
        tk.END
    )

    rot_y.delete(
        0,
        tk.END
    )

    figura_seleccionada.set(
        "Seleccionar figura"
    )

    dibujar_plano()



# 7. REGRESAR


def regresar():

    ventana.destroy()

    import main1



# TÍTULO PRINCIPAL

titulo = tk.Label(
    ventana,
    text="TRANSFORMACIONES LINEALES — CNC",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)

titulo.pack(
    pady=(15, 10)
)



# CONTENEDOR

contenedor = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

contenedor.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=5
)



# PANEL IZQUIERDO

panel_izquierdo = tk.Frame(
    contenedor,
    bg=COLOR_PANEL,
    width=350,
    height=600,
    highlightbackground=COLOR_BORDE,
    highlightthickness=1
)

panel_izquierdo.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

panel_izquierdo.pack_propagate(False)


# PANEL DERECHO

panel_derecho = tk.Frame(
    contenedor,
    bg=COLOR_PANEL,
    highlightbackground=COLOR_BORDE,
    highlightthickness=1
)

panel_derecho.pack(
    side="right",
    fill="both",
    expand=True
)



# TÍTULO CONTROLES

tk.Label(
    panel_izquierdo,
    text="CONTROLES",
    font=("Arial", 15, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    pady=(10, 5)
)


# COORDENADAS

tk.Label(
    panel_izquierdo,
    text="1. COORDENADAS",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    anchor="w"
).pack(
    fill="x",
    padx=20,
    pady=(3, 3)
)


frame_coordenadas = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_coordenadas.pack()


tk.Label(
    frame_coordenadas,
    text="X:",
    bg=COLOR_PANEL
).grid(
    row=0,
    column=0
)

entrada_x = tk.Entry(
    frame_coordenadas,
    width=7
)

entrada_x.grid(
    row=0,
    column=1,
    padx=4
)


tk.Label(
    frame_coordenadas,
    text="Y:",
    bg=COLOR_PANEL
).grid(
    row=0,
    column=2
)

entrada_y = tk.Entry(
    frame_coordenadas,
    width=7
)

entrada_y.grid(
    row=0,
    column=3,
    padx=4
)


tk.Button(
    panel_izquierdo,
    text="Crear punto",
    bg=COLOR_PRIMARIO,
    fg="white",
    font=("Arial", 9, "bold"),
    cursor="hand2",
    command=crear_punto
).pack(
    pady=4
)


# FIGURAS PREESTABLECIDAS

tk.Label(
    panel_izquierdo,
    text="2. FIGURAS PREESTABLECIDAS",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    anchor="w"
).pack(
    fill="x",
    padx=20,
    pady=(3, 3)
)


frame_figuras = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_figuras.pack()


figura_seleccionada = tk.StringVar()

combo_figuras = ttk.Combobox(
    frame_figuras,
    textvariable=figura_seleccionada,
    values=[
        "Triángulo",
        "Cuadrado",
        "Rectángulo",
        "Pentágono",
        "Figura L"
    ],
    state="readonly",
    width=19
)

combo_figuras.set(
    "Seleccionar figura"
)

combo_figuras.grid(
    row=0,
    column=0,
    padx=4
)


tk.Button(
    frame_figuras,
    text="Aceptar",
    font=("Arial", 9, "bold"),
    command=aceptar_figura
).grid(
    row=0,
    column=1
)


# REFLEXIÓN

tk.Label(
    panel_izquierdo,
    text="3. REFLEXIÓN",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    anchor="w"
).pack(
    fill="x",
    padx=20,
    pady=(5, 3)
)


frame_reflexion = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_reflexion.pack()


botones_reflexion = [
    ("EJE X", 0, 0),
    ("EJE Y", 0, 1),
    ("BISECTRIZ", 1, 0),
    ("ORIGEN", 1, 1),
    ("Y = -X", 2, 0)
]


for texto, fila, columna in botones_reflexion:

    tk.Button(
        frame_reflexion,
        text=texto,
        width=11,
        font=("Arial", 8, "bold"),
        command=lambda t=texto: reflexion(t)
    ).grid(
        row=fila,
        column=columna,
        padx=3,
        pady=2
    )


# HOMOTECIA

tk.Label(
    panel_izquierdo,
    text="4. HOMOTECIA",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    anchor="w"
).pack(
    fill="x",
    padx=20,
    pady=(5, 3)
)


frame_homotecia = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_homotecia.pack()


tk.Label(
    frame_homotecia,
    text="X:",
    bg=COLOR_PANEL
).grid(row=0, column=0)

hom_x = tk.Entry(
    frame_homotecia,
    width=5
)

hom_x.grid(
    row=0,
    column=1,
    padx=2
)


tk.Label(
    frame_homotecia,
    text="Y:",
    bg=COLOR_PANEL
).grid(row=0, column=2)

hom_y = tk.Entry(
    frame_homotecia,
    width=5
)

hom_y.grid(
    row=0,
    column=3,
    padx=2
)


tk.Label(
    frame_homotecia,
    text="K:",
    bg=COLOR_PANEL
).grid(row=0, column=4)

hom_k = tk.Entry(
    frame_homotecia,
    width=5
)

hom_k.grid(
    row=0,
    column=5,
    padx=2
)


tk.Button(
    panel_izquierdo,
    text="Aceptar",
    font=("Arial", 9, "bold"),
    bg=COLOR_PRIMARIO,
    fg="white",
    cursor="hand2",
    command=aplicar_homotecia
).pack(
    pady=4
)


# ROTACIÓN

tk.Label(
    panel_izquierdo,
    text="5. ROTACIÓN",
    font=("Arial", 10, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO,
    anchor="w"
).pack(
    fill="x",
    padx=20,
    pady=(3, 3)
)


frame_angulo = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_angulo.pack()


tk.Label(
    frame_angulo,
    text="Ángulo:",
    bg=COLOR_PANEL
).grid(
    row=0,
    column=0
)

entrada_angulo = tk.Entry(
    frame_angulo,
    width=9
)

entrada_angulo.grid(
    row=0,
    column=1,
    padx=5
)


tk.Label(
    panel_izquierdo,
    text="Punto de rotación:",
    font=("Arial", 9, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    pady=(3, 2)
)


frame_rotacion = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_rotacion.pack()


tk.Label(
    frame_rotacion,
    text="X:",
    bg=COLOR_PANEL
).grid(
    row=0,
    column=0
)

rot_x = tk.Entry(
    frame_rotacion,
    width=7
)

rot_x.grid(
    row=0,
    column=1,
    padx=4
)


tk.Label(
    frame_rotacion,
    text="Y:",
    bg=COLOR_PANEL
).grid(
    row=0,
    column=2
)

rot_y = tk.Entry(
    frame_rotacion,
    width=7
)

rot_y.grid(
    row=0,
    column=3,
    padx=4
)


tk.Button(
    panel_izquierdo,
    text="Aceptar",
    font=("Arial", 9, "bold"),
    bg=COLOR_PRIMARIO,
    fg="white",
    cursor="hand2",
    command=aplicar_rotacion
).pack(
    pady=4
)


# ACCIONES

frame_acciones = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_acciones.pack(
    side="bottom",
    pady=8
)


tk.Button(
    frame_acciones,
    text="LIMPIAR",
    width=12,
    height=2,
    font=("Arial", 9, "bold"),
    bg="#E5E7EB",
    fg=COLOR_TEXTO,
    cursor="hand2",
    command=limpiar
).pack(
    side="left",
    padx=4
)


tk.Button(
    frame_acciones,
    text="REGRESAR",
    width=12,
    height=2,
    font=("Arial", 9, "bold"),
    bg="#DC2626",
    fg="white",
    cursor="hand2",
    command=regresar
).pack(
    side="left",
    padx=4
)


# PLANO


tk.Label(
    panel_derecho,
    text="PLANO CARTESIANO",
    font=("Arial", 15, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    pady=(10, 3)
)


canvas = tk.Canvas(
    panel_derecho,
    width=ANCHO_PLANO,
    height=ALTO_PLANO,
    bg="white",
    highlightthickness=0
)

canvas.pack(
    padx=10,
    pady=5
)


# DIBUJAR PLANO INICIAL

dibujar_plano()



# EJECUTAR

ventana.mainloop()