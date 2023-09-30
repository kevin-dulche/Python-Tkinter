from tkinter import *

def miFuncion():
    print("Este mensaje es del boton")

ventana = Tk()
ventana.title("Hola Mundo")
ventana.geometry("400x200")

lb1 = Label(ventana, text="Este es un label")
lb1.config(fg="gray")
lb1.pack()

btn = Button(ventana, text="Presionar", fg="red", bg="yellow", command=miFuncion)

# btn.config(fg="red", bg="blue")

# btn["fg"] = "red"
# btn["bg"] = "yellow"

btn.pack()

ventana.mainloop()