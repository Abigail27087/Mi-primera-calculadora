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

for i in range(12):
    ventana.rowconfigure(1, weight=1)
    ventana.columnconfigure(1, weight=1)

def show_info():
    print(entrada.get())
btn=tk.Button(ventana, text="guardar", bg="blue", fg="navy", command=show_info)
btn.grid(column=6, row=1, padx=20)
label=tk.Label(ventana, text="Ingresa tu nombre")
label.grid(column=7,row=0)
entrada=tk.Entry(ventana, bg="blue", fg="white", relief="flat")
entrada.grid(column=7,row=1, sticky="we")
#siempre va hasta el final
ventana.mainloop()
