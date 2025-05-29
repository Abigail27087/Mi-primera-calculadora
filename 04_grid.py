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
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2,weight=1)

#condigurar columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

btn1=tk.Button(ventana, text="Boton 1", bg="black")
#si no definimos fila ni columna se queda en 0 ambas
btn1.grid(sticky="news")
#news toma todo el espacio
#ns toma el centro de el espacio de maner a vertical
#we toma el centro del espacio de manera horizontal
btn2=tk.Button(ventana, text="Boton 1", bg="white")
#si no definimos fila ni columna se queda en 0 ambas
btn2.grid(sticky="ns")
btn3=tk.Button(ventana, text="Boton 1", bg="green")
#si no definimos fila ni columna se queda en 0 ambas
btn3.grid(sticky="we")
btn4=tk.Button(ventana, text="Boton 1", bg="cyan")
#si no definimos fila ni columna se queda en 0 ambas
btn4.grid(sticky="news", column=1, row=0)
btn5=tk.Button(ventana, text="Boton 1", bg="yellow")
#si no definimos fila ni columna se queda en 0 ambas
btn5.grid( column=1, row=1)#cuando no definimos un punto cardinal entonces autamaticamente se va a el medio 
btn51=tk.Button(ventana, text="Boton 5.1")
btn51.grid(sticky="n", row=1, column=1)
btn52=tk.Button(ventana, text="Boton 5.2")
btn52.grid(sticky="s", row=1, column=1)
btn53=tk.Button(ventana, text="Boton 5.3")
btn53.grid(sticky="e", row=1, column=1)
btn54=tk.Button(ventana, text="Boton 5.4")
btn54.grid(sticky="w", row=1, column=1)

btn6=tk.Button(ventana, text="Boton 1", bg="pink")
#si no definimos fila ni columna se queda en 0 ambas
btn6.grid(sticky="news",column=1,row=2)
btn7=tk.Button(ventana, text="Boton 1", bg="purple")
#si no definimos fila ni columna se queda en 0 ambas
btn7.grid(sticky="news", column=2,row=0)
btn8=tk.Button(ventana, text="Boton 1", bg="orange")
#si no definimos fila ni columna se queda en 0 ambas
btn8.grid(sticky="news", column=2,row=1)
btn9=tk.Button(ventana, text="Boton 1", bg="red")
#si no definimos fila ni columna se queda en 0 ambas
btn9.grid(sticky="news", column=2, row=2)

#siempre va hasta el final
ventana.mainloop()
