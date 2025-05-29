import tkinter as tk 
from tkinter import ttk


ventana=tk.Tk()
#Ajustar medida de ventana
ANCHO=600
LARGO=600
size=f"{ANCHO}x{LARGO}"
ventana.geometry(size)
#cambiar titulo de la ventana
ventana.title("Practica tkinter")
#Cambiar icono de la ventana
ventana.iconbitmap("./practicatk.ico")
#botones
def click():
    #para actualizar un boton se usa el metodo config
    boton1.config(text="¡Bienvenido!Programador estrella")

def click2():
    boton2.config(text="Esta es mi primera practica con tkinter")
    
def click3():
    boton3.config(text="Es muy interesante programar")

def click4():
    boton4.config(text="Es algo que yo nunca había hecho perooo")

def click5():
    boton5.config(text="Recientmente me di cuenta que me gusta programar")

boton1=tk.Button(ventana, text="Holaa,dame click por favor", bg="black", fg="white", relief="flat", command=click)
boton1.pack()
boton2=tk.Button(ventana, text="Da click, por favor", bg="white", fg="black", relief="flat",command=click2)
boton2.pack()
boton3=tk.Button(ventana, text="Tocame, no pierdes nada", bg="purple", fg="black", relief="flat", command=click3)
boton3.pack()
boton4=tk.Button(ventana, text="Vuelve a darme click", bg="pink", fg="black", relief="flat", command=click4)
boton4.pack()
boton5=tk.Button(ventana, text="Dame click por ultima vez", bg="grey", fg="black", relief="flat", command=click5)
boton5.pack()
boton6=tk.Button(ventana, text="Gracias por leer:) BYEEE", bg="green", fg="black", relief="flat")
boton6.pack()


#siempre va hasta el final
ventana.mainloop()

