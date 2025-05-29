import tkinter as tk 

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
#siempre va hasta el final
ventana.mainloop()
