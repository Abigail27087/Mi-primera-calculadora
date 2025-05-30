import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb

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

for columna in range(0,2):
    ventana.columnconfigure(columna, weight=1)

for fila in range(0,3):
     ventana.rowconfigure(fila,weight=1)
            
titulo=tk.Label(ventana, font=("Cascadia Code",20),fg="green", text="TIPOS DE VENTANAS")
titulo.grid(column=2,row=0)

def mostrar_mensaje():
    mb.showinfo("Mi primer ventana emergente", "Hola mundo")
    mb.showerror("Ventana error", "Hola mundo")
    mb.showwarning("Ventana warning", "Hola mundo")
    respuesta=mb.askyesno("Ventana si o no", "Hola mundo")
    ventana_dos=tk.Toplevel()
    ventana_dos.title("Mostrar la respuesta si o no")
    label=ttk.Label(ventana_dos, text=respuesta).pack()
    boton_ventana_dos=ttk.Button(ventana_dos, text="Respuesta entendida", command=ventana_dos.destroy).pack()
#DB
#SQL
#Insertar en tablas
btn=ttk.Button(ventana, text="Presioname", command=mostrar_mensaje)
btn.pack()
#siempre va hasta el final
ventana.mainloop()
