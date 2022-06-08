#aplicacion de escritorio
import tkinter as tk
def bienvenido():
    print("Bienvenidos a python")
def cerrar_app():

    ventana.destroy()
def mostrartexto():
    msg = caja.get()
    print(msg)
ventana = tk.Tk()
ventana.title("Ventana principal")
ventana.config(width=400,height=300)

boton = tk.Button(text="Press Here")
boton.place(x=50, y=150, width=80, height=30)

etiqueta= tk.Label(text="Ingrese su nombre")
etiqueta.place(x=20, y=30)

caja= tk.Entry()
caja.place(x=20, y=50, width=200, height=25 )

boton_saludo= tk.Button(text="Saludo", command=bienvenido)
boton_saludo.place(x=150, y=150, width=80, height=30)

boton_salir=tk.Button(text="Salir", command=cerrar_app)
boton_salir.place(x=250, y=190, width=80, height=30)

boton_msg=tk.Button(text="Ver Mensaje", command=mostrartexto)
boton_msg.place(x=250, y=150, width=80, height=30)

ventana.mainloop()#tiene que ir siempre al final

