import tkinter as tk
from tkinter import ttk


# =========================================================
# VENTANA PRINCIPAL
# =========================================================

ventana = tk.Tk()

ventana.title("Transformaciones Lineales - CNC")
ventana.geometry("1200x700")
ventana.resizable(False, False)
ventana.configure(bg="#F4F6F8")


# =========================================================
# COLORES
# =========================================================

COLOR_FONDO = "#F4F6F8"
COLOR_PANEL = "#FFFFFF"
COLOR_PRIMARIO = "#2563EB"
COLOR_PRIMARIO_HOVER = "#1D4ED8"
COLOR_SECUNDARIO = "#6B7280"
COLOR_TEXTO = "#1F2937"
COLOR_BORDE = "#D1D5DB"


# =========================================================
# TÍTULO
# =========================================================

titulo = tk.Label(
    ventana,
    text="TRANSFORMACIONES LINEALES — CNC",
    font=("Arial", 22, "bold"),
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)

titulo.pack(pady=(15, 10))


# =========================================================
# CONTENEDOR PRINCIPAL
# =========================================================

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


# =========================================================
# PANEL IZQUIERDO
# =========================================================

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


# =========================================================
# PANEL DERECHO
# =========================================================

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


# =========================================================
# TÍTULO PANEL IZQUIERDO
# =========================================================

titulo_panel = tk.Label(
    panel_izquierdo,
    text="CONTROLES",
    font=("Arial", 15, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
)

titulo_panel.pack(
    pady=(15, 8)
)


# =========================================================
# FUNCIÓN PARA CREAR TÍTULOS DE SECCIÓN
# =========================================================

def titulo_seccion(texto):

    return tk.Label(
        panel_izquierdo,
        text=texto,
        font=("Arial", 10, "bold"),
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO,
        anchor="w"
    )


# =========================================================
# 1. COORDENADAS
# =========================================================

titulo_seccion("1. COORDENADAS").pack(
    fill="x",
    padx=20,
    pady=(5, 3)
)

frame_coordenadas = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_coordenadas.pack(
    padx=20,
    fill="x"
)


# X

tk.Label(
    frame_coordenadas,
    text="X:",
    font=("Arial", 10),
    bg=COLOR_PANEL
).grid(
    row=0,
    column=0,
    padx=(0, 5)
)

entrada_x = tk.Entry(
    frame_coordenadas,
    width=8,
    font=("Arial", 10)
)

entrada_x.grid(
    row=0,
    column=1,
    padx=(0, 15)
)


# Y

tk.Label(
    frame_coordenadas,
    text="Y:",
    font=("Arial", 10),
    bg=COLOR_PANEL
).grid(
    row=0,
    column=2,
    padx=(0, 5)
)

entrada_y = tk.Entry(
    frame_coordenadas,
    width=8,
    font=("Arial", 10)
)

entrada_y.grid(
    row=0,
    column=3
)


def crear_punto():

    print(
        "Punto creado:",
        entrada_x.get(),
        entrada_y.get()
    )


tk.Button(
    panel_izquierdo,
    text="Crear punto",
    font=("Arial", 9, "bold"),
    bg=COLOR_PRIMARIO,
    fg="white",
    activebackground=COLOR_PRIMARIO_HOVER,
    activeforeground="white",
    cursor="hand2",
    command=crear_punto
).pack(
    pady=(5, 8)
)


# =========================================================
# 2. FIGURAS PREESTABLECIDAS
# =========================================================

titulo_seccion("2. FIGURAS PREESTABLECIDAS").pack(
    fill="x",
    padx=20,
    pady=(2, 3)
)

frame_figuras = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_figuras.pack(
    padx=20,
    fill="x"
)


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
    width=22
)

combo_figuras.set("Seleccionar figura")

combo_figuras.pack(
    side="left",
    padx=(0, 8)
)


def aceptar_figura():

    print(
        "Figura seleccionada:",
        figura_seleccionada.get()
    )


tk.Button(
    frame_figuras,
    text="Aceptar",
    font=("Arial", 9, "bold"),
    bg=COLOR_SECUNDARIO,
    fg="white",
    cursor="hand2",
    command=aceptar_figura
).pack(
    side="left"
)


# =========================================================
# 3. REFLEXIÓN
# =========================================================

titulo_seccion("3. REFLEXIÓN").pack(
    fill="x",
    padx=20,
    pady=(8, 3)
)

frame_reflexion = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_reflexion.pack(
    padx=20
)


def reflexion(tipo):

    print(
        "Reflexión:",
        tipo
    )


# Fila 1

tk.Button(
    frame_reflexion,
    text="EJE X",
    width=11,
    font=("Arial", 9, "bold"),
    command=lambda: reflexion("EJE X")
).grid(
    row=0,
    column=0,
    padx=3,
    pady=3
)

tk.Button(
    frame_reflexion,
    text="EJE Y",
    width=11,
    font=("Arial", 9, "bold"),
    command=lambda: reflexion("EJE Y")
).grid(
    row=0,
    column=1,
    padx=3,
    pady=3
)


# Fila 2

tk.Button(
    frame_reflexion,
    text="BISECTRIZ",
    width=11,
    font=("Arial", 9, "bold"),
    command=lambda: reflexion("BISECTRIZ")
).grid(
    row=1,
    column=0,
    padx=3,
    pady=3
)

tk.Button(
    frame_reflexion,
    text="ORIGEN",
    width=11,
    font=("Arial", 9, "bold"),
    command=lambda: reflexion("ORIGEN")
).grid(
    row=1,
    column=1,
    padx=3,
    pady=3
)


# Fila 3

tk.Button(
    frame_reflexion,
    text="Y = -X",
    width=11,
    font=("Arial", 9, "bold"),
    command=lambda: reflexion("Y = -X")
).grid(
    row=2,
    column=0,
    padx=3,
    pady=3
)


# =========================================================
# 4. HOMOTECIA
# =========================================================

titulo_seccion("4. HOMOTECIA").pack(
    fill="x",
    padx=20,
    pady=(8, 3)
)

frame_homotecia = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_homotecia.pack(
    padx=20
)


# X

tk.Label(
    frame_homotecia,
    text="X:",
    font=("Arial", 9),
    bg=COLOR_PANEL
).grid(
    row=0,
    column=0,
    padx=3
)

hom_x = tk.Entry(
    frame_homotecia,
    width=6
)

hom_x.grid(
    row=0,
    column=1,
    padx=3
)


# Y

tk.Label(
    frame_homotecia,
    text="Y:",
    font=("Arial", 9),
    bg=COLOR_PANEL
).grid(
    row=0,
    column=2,
    padx=3
)

hom_y = tk.Entry(
    frame_homotecia,
    width=6
)

hom_y.grid(
    row=0,
    column=3,
    padx=3
)


# K

tk.Label(
    frame_homotecia,
    text="K:",
    font=("Arial", 9),
    bg=COLOR_PANEL
).grid(
    row=0,
    column=4,
    padx=3
)

hom_k = tk.Entry(
    frame_homotecia,
    width=6
)

hom_k.grid(
    row=0,
    column=5,
    padx=3
)


def aplicar_homotecia():

    print(
        "Homotecia:",
        hom_x.get(),
        hom_y.get(),
        hom_k.get()
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
    pady=(5, 8)
)


# =========================================================
# 5. ROTACIÓN
# =========================================================

titulo_seccion("5. ROTACIÓN").pack(
    fill="x",
    padx=20,
    pady=(3, 3)
)


# Ángulo

frame_angulo = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_angulo.pack(
    padx=20,
    fill="x"
)

tk.Label(
    frame_angulo,
    text="Ángulo:",
    font=("Arial", 9),
    bg=COLOR_PANEL
).pack(
    side="left",
    padx=(0, 5)
)

entrada_angulo = tk.Entry(
    frame_angulo,
    width=10
)

entrada_angulo.pack(
    side="left"
)


# Punto de rotación

tk.Label(
    panel_izquierdo,
    text="Punto de rotación:",
    font=("Arial", 9, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
).pack(
    anchor="w",
    padx=20,
    pady=(5, 2)
)


frame_rotacion = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_rotacion.pack(
    padx=20
)


tk.Label(
    frame_rotacion,
    text="X:",
    font=("Arial", 9),
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
    padx=5
)


tk.Label(
    frame_rotacion,
    text="Y:",
    font=("Arial", 9),
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
    padx=5
)


def aplicar_rotacion():

    print(
        "Rotación:",
        entrada_angulo.get(),
        rot_x.get(),
        rot_y.get()
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
    pady=(5, 8)
)


# =========================================================
# 6. ACCIONES GENERALES
# =========================================================

frame_acciones = tk.Frame(
    panel_izquierdo,
    bg=COLOR_PANEL
)

frame_acciones.pack(
    side="bottom",
    pady=12
)


def limpiar():

    entrada_x.delete(0, tk.END)
    entrada_y.delete(0, tk.END)

    hom_x.delete(0, tk.END)
    hom_y.delete(0, tk.END)
    hom_k.delete(0, tk.END)

    entrada_angulo.delete(0, tk.END)

    rot_x.delete(0, tk.END)
    rot_y.delete(0, tk.END)

    combo_figuras.set("Seleccionar figura")

    print("Formulario limpiado")


def regresar():

    ventana.destroy()


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
    padx=5
)


tk.Button(
    frame_acciones,
    text="REGRESAR",
    width=12,
    height=2,
    font=("Arial", 9, "bold"),
    bg="#DC2626",
    fg="white",
    activebackground="#B91C1C",
    cursor="hand2",
    command=regresar
).pack(
    side="left",
    padx=5
)


# =========================================================
# PLANO CARTESIANO
# =========================================================

label_plano = tk.Label(
    panel_derecho,
    text="PLANO CARTESIANO",
    font=("Arial", 15, "bold"),
    bg=COLOR_PANEL,
    fg=COLOR_TEXTO
)

label_plano.pack(
    pady=(15, 5)
)


canvas = tk.Canvas(
    panel_derecho,
    width=790,
    height=530,
    bg="white",
    highlightthickness=0
)

canvas.pack(
    padx=10,
    pady=5
)


# =========================================================
# DIBUJAR PLANO
# =========================================================

def dibujar_plano():

    canvas.delete("all")

    ancho = 790
    alto = 530

    centro_x = ancho // 2
    centro_y = alto // 2

    escala = 40

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

    # Números eje X
    for i in range(-9, 10):

        if i == 0:
            continue

        x = centro_x + i * escala

        canvas.create_text(
            x,
            centro_y + 14,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )

    # Números eje Y
    for i in range(-6, 7):

        if i == 0:
            continue

        y = centro_y - i * escala

        canvas.create_text(
            centro_x + 14,
            y,
            text=str(i),
            font=("Arial", 8),
            fill="#6B7280"
        )

    # X
    canvas.create_text(
        ancho - 15,
        centro_y - 15,
        text="X",
        font=("Arial", 11, "bold"),
        fill="#374151"
    )

    # Y
    canvas.create_text(
        centro_x + 15,
        15,
        text="Y",
        font=("Arial", 11, "bold"),
        fill="#374151"
    )


dibujar_plano()


# =========================================================
# EJECUTAR
# =========================================================

ventana.mainloop()