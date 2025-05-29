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
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0,weight=1)

#el parametro pack cambia los margenes externos x para los lados,y  para y abajo
#ipad sirve para los margenes internos, x pra los lados ,y para arriba y abajo
btn=tk.Button(ventana,text="Hola",bg="fuchsia")
btn.pack(pady=30, ipady=30)
#btn.config(pady=50, padx=50)
btn2=tk.Button(ventana,text="Adios",bg="purple")
btn2.pack(padx=30)
#btn2.config(padx=40, pady=40)

ventana.mainloop()
