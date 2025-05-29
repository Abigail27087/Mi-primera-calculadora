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
#configurar columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1)
ventana.columnconfigure(2, weight=1)
#comenzamos con los textos
show_name=tk.Label(ventana, font=("Arial", 20), fg="blue")

instruction=tk.Label(ventana, font=("Arial",20),fg="red", text="Ingresa tu nombre")
instruction.grid(column=1,row=1)

entry=tk.Entry(ventana, font=("Arial", 20), relief="groove")
#insert sirve para poner datos dentro del entry
#Entry.insert(0,"Juan")
entry.grid(column=1,row=2, pady=20)
#el metodo get devuelve el texto dentro de la entry siempre es texto 
#entry a entero int(entry.get())
#entry.get()
entry.get()

#boton para combinar entry y show_name
def click():
    text=entry.get()
    if len(text)<=0:
        text="Es necesario que ingreses tu nombre"
    else:
        text=f"Hola, {text}"
    show_name.config(text=text)
    show_name.grid(column=1,row=0)
btn=tk.Button(ventana, text="Enviar", relief="groove", bg="cyan", command=click)
btn.grid(column=1,row=3) 
ventana.mainloop()
