import tkinter as tk
from tkinter import messagebox




def ingresar_coordenadas():
    messagebox.showinfo(
        "Ingresar coordenadas",
        "Aquí se ingresarán las coordenadas de la pieza."
    )


def cargar_archivo():
    messagebox.showinfo(
        "Cargar archivo",
        "Aquí se cargará un archivo con las coordenadas."
    )


def salir():
    ventana.destroy()




ventana = tk.Tk()

ventana.title("Transformaciones Lineales - CNC")
ventana.geometry("900x600")
ventana.resizable(False, False)


ventana.configure(bg="#F4F6F8")



titulo = tk.Label(
    ventana,
    text="TRANSFORMACIONES LINEALES",
    font=("Arial", 26, "bold"),
    bg="#F4F6F8",
    fg="#1F2937"
)

titulo.pack(pady=(70, 5))




subtitulo = tk.Label(
    ventana,
    text="Sistema de manipulación geométrica para piezas CNC",
    font=("Arial", 15),
    bg="#F4F6F8",
    fg="#4B5563"
)

subtitulo.pack(pady=(0, 45))




descripcion = tk.Label(
    ventana,
    text=(
        "Representación y transformación de piezas mediante\n"
        "rotaciones, homotecias y reflexiones."
    ),
    font=("Arial", 12),
    bg="#F4F6F8",
    fg="#6B7280",
    justify="center"
)

descripcion.pack(pady=(0, 30))



boton_manual = tk.Button(
    ventana,
    text="INGRESAR COORDENADAS",
    font=("Arial", 12, "bold"),
    width=30,
    height=2,
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    cursor="hand2",
    command=ingresar_coordenadas
)

boton_manual.pack(pady=10)




boton_archivo = tk.Button(
    ventana,
    text="CARGAR ARCHIVO",
    font=("Arial", 12, "bold"),
    width=30,
    height=2,
    bg="#374151",
    fg="white",
    activebackground="#1F2937",
    activeforeground="white",
    cursor="hand2",
    command=cargar_archivo
)

boton_archivo.pack(pady=10)



boton_salir = tk.Button(
    ventana,
    text="SALIR",
    font=("Arial", 11),
    width=15,
    cursor="hand2",
    command=salir
)

boton_salir.pack(pady=35)




footer = tk.Label(
    ventana,
    text="Proyecto de Matemática Discreta",
    font=("Arial", 9),
    bg="#F4F6F8",
    fg="#9CA3AF"
)

footer.pack(side="bottom", pady=15)




ventana.mainloop()