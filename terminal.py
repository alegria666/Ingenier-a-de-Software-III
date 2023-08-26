from inspect import FrameInfo
from tkinter import *
from tkinter import messagebox as MessageBox
import psycopg2

def mostrar_seleccion(metodo_pago):
    mensaje = f"Seleccionaste el método de pago: {metodo_pago}\n ¿Desea efectuar el pago?"
    MessageBox.showinfo("Efecuar pago", mensaje)
    
def seleccion_efectivo():
    mostrar_seleccion("Efectivo")

def seleccion_transferencia():
    mostrar_seleccion("Transferencia")#nequi - bancolombia etc

def seleccion_tarjeta():
    mostrar_seleccion("Tarjeta")#credito debito

def entrada_id(text, ntext):
    if len(ntext) > 4:
        return False
    return text.isdecimal()

def entrada_int(text):
    return text.isdecimal()

def entrada_placa(text):
    if len(text) > 7:
        return False
    else:
        return text
       
def registrar_tiquete(cedulap, idruta):
    if(cedulap=="" or idruta == ""):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO abordajes(id_cedula, idruta) VALUES (%s, %s)'''
        cursor.execute(consulta, (cedulap, idruta))
        MessageBox.showinfo("EXITO", "Registro Satisfactorio")
        conn.commit()
        conn.close()
    
def registrar_ruta(id, salida, destino):
    if(id=="" or salida == "" or destino == "" ):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO rutas(idruta, salida, destino) VALUES (%s, %s, %s)'''
        cursor.execute(consulta, (id, salida, destino))
        print("Registro satisfactorio")
        conn.commit()
        conn.close()
       
def registrar_bus(id, placa, capacidad, idempleado):
    if(id=="" or placa == "" or capacidad == "" or idempleado == ""):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO bus (idbus, placa, capacidad, idempleado) VALUES (%s, %s, %s, %s)'''
        cursor.execute(consulta, (id, placa, capacidad, idempleado))
        print("Registro satisfactorio")
        conn.commit()
        conn.close()
    
def registrar_conductor(id, nombre, apellido, telefono, cedula):
    if(id=="" or nombre == "" or apellido == "" or telefono == "" or cedula ==""):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO empleado (idempleado, nombre, apellido, telefono, cedula) VALUES (%s, %s, %s, %s, %s)'''
        cursor.execute(consulta, (id, nombre, apellido, telefono, cedula))
        print("Registro satisfactorio")
        conn.commit()
        conn.close()
    
def registrar_compra(id_cedula, idempleado, idbus, idruta,valor):   
    if(id_cedula=="" or idempleado == "" or idbus == "" or idruta == ""or valor=="" ):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO venta_tiquete (id_cedula, idempleado, idbus, idruta,valor) VALUES (%s, %s, %s, %s,%s)'''
        cursor.execute(consulta, (id_cedula, idempleado,idbus,idruta,valor))
        print("Registro satisfactorio")
        print(id_cedula,idempleado,idbus,idruta,valor)
        
        MessageBox.showinfo("EXITO", "Registro Satisfactorio\nvalor: ") 
               
        conn.commit()
        conn.close()       
           
def registrar_pasajero(cedula, nombre, apellido, telefono, correo):   
    if(cedula=="" or nombre == "" or apellido == "" or telefono == "" or correo ==""):
        MessageBox.showinfo("ERROR", "Por favor ingresar todos los campos")
    else:
        conn = psycopg2.connect(dbname = "terminal_transporte", 
                                user  = "postgres", 
                                password = "5432", 
                                host = "localhost")
        cursor = conn.cursor()
        consulta = '''INSERT INTO cliente (id_cedula, nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s, %s)'''
        cursor.execute(consulta, (cedula, nombre, apellido, telefono, correo))
        MessageBox.showinfo("EXITO", "Registro Satisfactorio")        
        conn.commit()
        conn.close()
             
def tiquete_boton():
    tiquete_ventana = Toplevel()
    tiquete_ventana.title("Registro Buses")
    tiquete_ventana.geometry("380x200")
    
    canvas = Canvas(tiquete_ventana, height = 380, width = 200)
    canvas.pack()
    
    frame = Frame(tiquete_ventana)
    frame.place(relheight=1, relwidth=1)
    frame.config(background= "#e2f0cb")
    
    label = Label(frame, text = 'AGREGAR RESERVA')
    label.grid(row=0, column = 1)
    label.config(foreground='#6aa9e9',font=("Helvetica", 12, "bold"), background= "#e2f0cb")
    
    label = Label(frame, text = "Cédula pasajero: ")
    label.grid(row=5, column=0)
    label.config(background= "#e2f0cb")

    entry_idc = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_idc.grid(row = 5, column = 1)
    
    label = Label(frame, text = "Id de la ruta: ")
    label.grid(row=7, column=0)
    label.config(background= "#e2f0cb")
    
    entry_idr = Entry(frame,validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_idr.grid(row = 7, column = 1)
    
    r = Button(frame, text='Registrar', command = lambda:registrar_tiquete(entry_idc.get(), 
                                                                        entry_idr.get()
                                                                                ))
    r.grid(row=55, column=3, sticky=W+E)
    
def ruta_boton():
    
    ruta_ventana = Toplevel()
    ruta_ventana.title("Registro Rutas")
    ruta_ventana.geometry("380x250")
    
    canvas = Canvas(ruta_ventana, height = 380, width = 200)
    canvas.pack()
    
    frame = Frame(ruta_ventana)
    frame.place(relheight=1, relwidth=1)
    frame.config(background= "#e2f0cb")
    
    label = Label(frame, text = 'AGREGAR RUTA')
    label.grid(row=0, column = 1)
    label.config(foreground='#6aa9e9',font=("Helvetica", 12, "bold"), background= "#e2f0cb")
    
    label = Label(frame, text = "Id Ruta: ")
    label.grid(row=5, column=0)
    label.config(background= "#e2f0cb")

    entry_idruta = Entry(frame, validate= 'key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_idruta.grid(row = 5, column = 1)
    
    label = Label(frame, text = "Lugar de salida: ")
    label.grid(row=7, column=0)
    label.config(background= "#e2f0cb")
    
    entry_salida = Entry(frame)
    entry_salida.grid(row = 7, column = 1)
    
    label = Label(frame, text = "Lugar de destino: ")
    label.grid(row=9, column=0)
    label.config(background= "#e2f0cb")
    
    entry_destino = Entry(frame)
    entry_destino.grid(row = 9, column = 1)
    

    
    
        
    r = Button(frame, text='Registrar', command = lambda:registrar_ruta(entry_idruta.get(), 
                                                                        entry_salida.get(), 
                                                                        entry_destino.get(), 
                                                                        )) 
                                                                        
    r.grid(row=55, column=3, sticky=W+E)
    
    #info_pago = Button(frame, text='Información de Pago', command=lambda: mostrar_informacion_pago(entry_valor.get()))
    #info_pago.grid(row=55, column=4, sticky=W+E)      
    
def bus_boton():
    bus_ventana = Toplevel()
    bus_ventana.title("Registro Buses")
    bus_ventana.geometry("380x200")

    canvas = Canvas(bus_ventana, height = 380, width = 200)
    canvas.pack()
    
    frame = Frame(bus_ventana)
    frame.place(relheight=1, relwidth=1)
    frame.config(background= "#e2f0cb")
    
    label = Label(frame, text = 'AGREGAR BUS')
    label.grid(row=0, column = 1)
    label.config(foreground='#6aa9e9',font=("Helvetica", 12, "bold"), background= "#e2f0cb")

    label = Label(frame, text = "Id Bus: ")
    label.grid(row=5, column=0)
    label.config(background= "#e2f0cb")

    entry_idbus = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_idbus.grid(row = 5, column = 1)
    
    label = Label(frame, text = "Placa (AAA-###): ")
    label.grid(row=7, column=0)
    label.config(background= "#e2f0cb")
    
    entry_placa = Entry(frame, validate='key', validatecommand=(frame.register(entrada_placa), "%S"))
    entry_placa.grid(row = 7, column = 1)
    
    label = Label(frame, text = "Capacidad: ")
    label.grid(row=9, column=0)
    label.config(background= "#e2f0cb")
    
    entry_capacidad = Entry(frame, validate='key', validatecommand=(frame.register(entrada_int), "%S"))
    entry_capacidad.grid(row = 9, column = 1)
    
    label = Label(frame, text = "Id Empleado: ")
    label.grid(row=11, column=0)
    label.config(background= "#e2f0cb")
    
    entry_ide = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_ide.grid(row = 11, column = 1)
    
    r = Button(frame, text='Registrar', command = lambda:registrar_bus(entry_idbus.get(), 
                                                                        entry_placa.get(), 
                                                                        entry_capacidad.get(), 
                                                                        entry_ide.get()))                                                                                           
    
    r.grid(row=55, column=3, sticky=W+E)
    
def conductor_boton():
    conductor_ventana = Toplevel()
    conductor_ventana.title("Registro Conductor")
    conductor_ventana.geometry("380x200")
    
    canvas = Canvas(conductor_ventana, height = 380, width = 200)
    canvas.pack()
    
    frame = Frame(conductor_ventana)
    frame.place(relheight=1, relwidth=1)
    frame.config(background= "#e2f0cb")
    
    label = Label(frame, text = 'AGREGAR CONDUCTOR')
    label.grid(row=0, column = 1)
    label.config(foreground='#6aa9e9',font=("Helvetica", 12, "bold"), background= "#e2f0cb")
    
    label = Label(frame, text = "Cédula: ")
    label.grid(row=5, column=0)
    label.config(background= "#e2f0cb")

    entry_cedulae = Entry(frame, validate= 'key', validatecommand=(frame.register(entrada_int)))
    entry_cedulae.grid(row = 5, column = 1)
    
    label = Label(frame, text = "Nombre: ")
    label.grid(row=7, column=0)
    label.config(background= "#e2f0cb")
    
    entry_nombree = Entry(frame)
    entry_nombree.grid(row = 7, column = 1)
    
    label = Label(frame, text = "Apellido: ")
    label.grid(row=9, column=0)
    label.config(background= "#e2f0cb")
    
    entry_apellidoe = Entry(frame)
    entry_apellidoe.grid(row = 9, column = 1)
    
    label = Label(frame, text = "Teléfono: ")
    label.grid(row=11, column=0)
    label.config(background= "#e2f0cb")
    
    entry_telefonoe = Entry(frame, validate= 'key', validatecommand=(frame.register(entrada_int), "%S"))
    entry_telefonoe.grid(row = 11, column = 1)
    
    label = Label(frame, text = "Id Empleado: ")
    label.grid(row=13, column=0)
    label.config(background= "#e2f0cb")
    
    entry_ide = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id) ))
    entry_ide.grid(row = 13, column = 1)
    
    r = Button(frame, text='Registrar', command = lambda:registrar_conductor(entry_ide.get(), 
                                                                            entry_nombree.get(), 
                                                                            entry_apellidoe.get(), 
                                                                            entry_telefonoe.get(), 
                                                                            entry_cedulae.get()))
    r.grid(row=55, column=3, sticky=W+E)
    
def pasajero_boton():
    pasajero_ventana = Toplevel()
    pasajero_ventana.title("Registro Pasajero")
    pasajero_ventana.geometry("380x200")

    canvas = Canvas(pasajero_ventana, height = 380, width = 200)
    canvas.pack()
    
    frame = Frame(pasajero_ventana)
    frame.place(relheight=1, relwidth=1)
    frame.config(background="#e2f0cb")
    
    label = Label(frame, text = 'AGREGAR PASAJERO')
    label.grid(row=0, column = 1)
    label.config(foreground='#6aa9e9',font=("Helvetica", 12, "bold"), background= "#e2f0cb")

    label = Label(frame, text = "Cédula: ")
    label.grid(row=5, column=0)
    label.config(background= "#e2f0cb")

    entry_cedulac = Entry(frame, validate="key" ,validatecommand=(frame.register(entrada_id), "%S", "%P"))
    entry_cedulac.grid(row = 5, column = 1)
    
    label = Label(frame, text = "Nombre: ")
    label.grid(row=7, column=0)
    label.config(background= "#e2f0cb")
    
    entry_nombrec = Entry(frame)
    entry_nombrec.grid(row = 7, column = 1)
    
    label = Label(frame, text = "Apellido: ")
    label.grid(row=9, column=0)
    label.config(background= "#e2f0cb")
    
    entry_apellidoc = Entry(frame)
    entry_apellidoc.grid(row = 9, column = 1)
    
    label = Label(frame, text = "Teléfono: ")
    label.grid(row=11, column=0)
    label.config(background= "#e2f0cb")
    
    entry_telefonoc = Entry(frame, validate= 'key', validatecommand=(frame.register(entrada_int), "%S"))
    entry_telefonoc.grid(row = 11, column = 1)
    
    label = Label(frame, text = "Correo: ")
    label.grid(row=13, column=0)
    label.config(background= "#e2f0cb")
    
    entry_correoc = Entry(frame)
    entry_correoc.grid(row = 13, column = 1)
    
    r = Button(frame, text='Registrar', command = lambda:registrar_pasajero(entry_cedulac.get(), 
                                                                            entry_nombrec.get(), 
                                                                            entry_apellidoc.get(), 
                                                                            entry_telefonoc.get(), 
                                                                            entry_correoc.get()))
    
    r.grid(row=55, column=3, sticky=W+E)
    
    pasajero_ventana.mainloop()

def venta_tiquete():
    venta_tiquete_ventana = Toplevel()
    venta_tiquete_ventana.title("Venta de Tiquete")
    venta_tiquete_ventana.geometry("400x250")
    canvas = Canvas(venta_tiquete_ventana, height=400, width=250)
    canvas.pack()
    frame = Frame(venta_tiquete_ventana)
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)

    label = Label(frame, text='Venta de Tiquete')
    label.grid(row=0, column=1)
    label.config(foreground='#6aa9e9', font=("Helvetica", 12, "bold"), background="#e2f0cb")

    label = Label(frame, text="ID Cédula del Pasajero:")
    label.grid(row=1, column=0)
    label.config(background="#e2f0cb")
    
    id_cedula = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    id_cedula.grid(row=1, column=1)

    label = Label(frame, text="ID Empleado:")
    label.grid(row=2, column=0)
    label.config(background="#e2f0cb")

    idempleado = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idempleado.grid(row=2, column=1)

    label = Label(frame, text="ID Bus:")
    label.grid(row=3, column=0)
    label.config(background="#e2f0cb")

    idbus = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idbus.grid(row=3, column=1)

    label = Label(frame, text="ID Ruta:")
    label.grid(row=4, column=0)
    label.config(background="#e2f0cb")

    idruta = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idruta.grid(row=4, column=1)
    
    label = Label(frame, text="Valor:")
    label.grid(row=5, column=0)
    label.config(background="#e2f0cb")

    valor = Entry(frame, validate='key', validatecommand=(frame.register(entrada_int), "%S"))
    valor.grid(row=5, column=1)
    
    s = Button(frame, text='Metodo de Pago', command=metodo_pago)
    s.grid(row=65, column=2)
    s.config(bg = "darkblue", foreground="white")
    
          
    r = Button(frame, text='Registrar', command = lambda:registrar_compra(id_cedula.get(), 
                                                                            idempleado.get(), 
                                                                            idbus.get(), 
                                                                            idruta.get(),
                                                                            valor.get()))
    r.grid(row=80, column=2) 
        
def metodo_pago():
    root = Tk()
    root.title("Selección de Método de Pago")
    root.geometry("300x200")

    efectivo_button = Button(root, text="Efectivo", command=seleccion_efectivo)
    efectivo_button.pack(pady=20)

    transferencia_button = Button(root, text="Transferencia", command=seleccion_transferencia)
    transferencia_button.pack(pady=20)

    tarjeta_button = Button(root, text="Tarjeta", command=seleccion_tarjeta)
    tarjeta_button.pack(pady=20) 
    
    

root = Tk()
root.title("Terminal de Transporte")
root.geometry("400x250")

canvas = Canvas(root, height = 400, width = 250)
canvas.pack()

framep = Frame()
framep.place(relx=0, rely=0, relheight=1, relwidth=1)

image = PhotoImage(file = "bus.png")
label = Label(framep, image=image)
label.place(relheight=1, relwidth=1)

pasajero = Button(label, text='Registrar pasajero', command = pasajero_boton)
pasajero.grid(row=1, column=400)
pasajero.config(bg = "#06132f", foreground="white")

empleado = Button(label, text= 'Registrar conductores', command = conductor_boton)
empleado.grid(row = 5, column=400)
empleado.config(bg = "#06132f", foreground="white")

bus = Button(label, text='Registrar bus', command = bus_boton)
bus.grid(row=9, column=400)
bus.config(bg = "#06132f", foreground="white")

ruta = Button(label, text= 'Registrar ruta', command = ruta_boton)
ruta.grid(row = 13, column=400)
ruta.config(bg = "#06132f", foreground="white")

venta_tiquete_button = Button(label, text='Venta de Tiquetes', command=venta_tiquete)
venta_tiquete_button.grid(row=20, column=400, pady=10)
venta_tiquete_button.config(bg = "darkblue", foreground="white")

root.mainloop()
