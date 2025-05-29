import tkinter as tk 
from tkinter import ttk


ventana=tk.Tk()
#Ajustar medida de ventana
ANCHO=800
LARGO=600
size=f"{ANCHO}x{LARGO}"
ventana.geometry(size)
#cambiar titulo de la ventana
ventana.title("Mi primer ventana")
#Cambiar icono de la ventana
ventana.iconbitmap("./icono.ico")
#botones
def click():
    print("Mensaje detonado por el boton")
    #para actualizar un boton se usa el metodo config
    boton.config(text="Me tocaste ")
boton=ttk.Button(ventana, text="Hola,soy un boton :)", command=click)
boton.pack()

boton2=tk.Button(ventana, text="hola,soy boton 2", bg="red", fg="white", relief="flat")
boton2.pack()


#siempre va hasta el final
ventana.mainloop()

