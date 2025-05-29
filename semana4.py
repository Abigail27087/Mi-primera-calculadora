import tkinter as tk 

ventana=tk.Tk()
#Ajustar medida de ventana
ANCHO=800
LARGO=600
size=f"{ANCHO}x{LARGO}"
ventana.geometry(size)
#cambiar titulo de la ventana
ventana.title("Mi primer calculadora")
#Cambiar icono de la ventana
ventana.iconbitmap("./icono.ico")
#siempre va hasta el final
#configurar columnas
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1)
ventana.columnconfigure(2, weight=1)
#comenzamos con los textos
titulo=tk.Label(ventana, font=("Cascadia Code",20),fg="green", text="MI PRIMERA CALCULADORA")
titulo.grid(column=1,row=1)


numero1=tk.Entry(ventana, font=("Arial", 20), relief="groove")
numero1.grid(column=0,row=3, pady=20)
texto1=tk.Label(ventana, font=("Cascadia Code",20),fg="fuchsia", text="Ingrese el primer número")
texto1.grid(column=0,row=2)
numero2=tk.Entry(ventana, font=("Arial", 20), relief="groove")
numero2.grid(column=2,row=3, pady=20)
texto2=tk.Label(ventana, font=("Cascadia Code",20),fg="fuchsia", text="Ingrese el segundo número")
texto2.grid(column=2,row=2)

#entry a entero int(entry.get())
#entry.get()
resultado=tk.StringVar()
#boton para combinar entry y show_name
def suma():
    num1=int(numero1.get())
    num2=int(numero2.get())
    resultado_suma=num1+num2
    resultado.set(f"RESULTADO:{resultado_suma}")
    

def resta():
    num1=int(numero1.get())
    num2=int(numero2.get())
    resultado_resta=num1-num2
    resultado.set(f"RESULTADO:{resultado_resta}")

def multiplicación():
    num1=int(numero1.get())
    num2=int(numero2.get())
    resultado_multiplicacion=num1*num2
    resultado.set(f"RESULTADO:{resultado_multiplicacion}")

def división():
    num1=int(numero1.get())
    num2=int(numero2.get())
    resultado_division=num1/num2
    resultado.set(f"RESULTADO:{resultado_division}")

btn=tk.Button(ventana, text="SUMA", relief="solid", bg="cyan", command=suma)
btn.grid(column=1,row=4,pady=10) 

btn2=tk.Button(ventana,text="RESTA", relief="solid", bg="red", command=resta)
btn2.grid(column=1, row=5, pady=10)

btn3=tk.Button(ventana,text="MULTIPLICACIÓN", relief="solid", bg="pink", command=multiplicación)
btn3.grid(column=1, row=6, pady=10)

btn4=tk.Button(ventana,text="DIVISIÓN", relief="solid", bg="light green", command=división)
btn4.grid(column=1, row=7, pady=10)

resultado_label=tk.Label(ventana,textvariable=resultado,font=("Arial", 30))
resultado_label.grid(column=1,row=2)

ventana.mainloop()
