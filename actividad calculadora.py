import tkinter as tk

def suma() :
    sum_=int(box1.get())
    sum2=int(box2.get())
    result_suma=sum_+sum2
    print(result_suma)

def resta() :
    res=int(box1.get())
    res2=int(box2.get())
    result_rest=res-res2
    print(result_rest)

def mult() :
    multi=int(box1.get())
    multi2=int(box2.get())
    result_multi=multi*multi2
    print(result_multi)

def divis() :
    div=int(box1.get())
    div2=int(box2.get())
    result_div=div/div2
    print(result_div)

def resto() :
    rest=int(box1.get())
    rest2=int(box2.get())
    result_resto=rest%rest2
    print(result_resto)

def cerrar_app():
    ventana.destroy()

#hacerla mas profesional/avanzada

ventana = tk.Tk()
ventana.title("Calculator")
ventana.config(width=170,height=190)

box1 = tk.Entry()
box1.place(x=20,y=20,width=80,height=30)
box2 = tk.Entry()
box2.place(x=20,y=60,width=80,height=30)

boton_suma = tk.Button(text="+", command=suma)
boton_suma.place(x=110,y=20,width=40,height=30)

boton_resta = tk.Button(text="-", command=resta)
boton_resta.place(x=110,y=60,width=40,height=30)

boton_mult = tk.Button(text="*", command=mult)
boton_mult.place(x=20,y=100,width=40,height=30)

boton_div = tk.Button(text="/", command=divis)
boton_div.place(x=65,y=100,width=40,height=30)

boton_result=tk.Button(text="%", command=resto)
boton_result.place(x=110,y=100,width=40,height=30)

boton_salir=tk.Button(text="Salir", command=cerrar_app)
boton_salir.place(x=20, y=140, width=130, height=30)

ventana.mainloop()