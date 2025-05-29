import tkinter as tk 
import random
ventana=tk.Tk()
#Ajustar medida de ventana
ANCHO=600
LARGO=600
size=f"{ANCHO}x{LARGO}"
ventana.geometry(size)
#cambiar titulo de la ventana
ventana.title("Mi primer ventana")
#Cambiar icono de la ventana
ventana.iconbitmap("./icono.ico")
colores=["blue","light blue","light green", "yellow","orange","ivory","navy","dark green","cyan","gray","light pink","fuchsia", "red","magenta"]

def crear_botones():
    for fila in range(0,11):
        ventana.rowconfigure(fila, weight=1)
        for columna in range(0,11):
            ventana.columnconfigure(columna, weight=1)
            color = random.choice(colores)
            numero=columna+1
            boton = tk.Button(ventana,text=f"Boton {numero}", bg=color)
            boton.grid(row=fila, column=columna, sticky="news")
crear_botones()

ventana.mainloop() 