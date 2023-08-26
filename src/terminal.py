from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import psycopg2

def mostrar_seleccion(metodo_pago):
  mensaje = f"Seleccionaste el método de pago: {metodo_pago}\n ¿Desea efectuar el pago?"
  messagebox.showinfo("Efecuar pago", mensaje)

def seleccion_efectivo():
  mostrar_seleccion("Efectivo")

def seleccion_transferencia():
  mostrar_seleccion("Transferencia")

def seleccion_tarjeta():
  mostrar_seleccion("Tarjeta")

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


    
def registrar_ruta(id, salida, destino):
  if(id=="" or salida == "" or destino == "" ):
    messagebox.showinfo("ERROR", "Por favor ingresar todos los campos")
  else:
    conn = psycopg2.connect(dbname = "terminal_transporte", 
                            user  = "postgres", 
                            password = "1234", 
                            host = "localhost")
    cursor = conn.cursor()
    consulta = '''INSERT INTO rutas(idruta, salida, destino) VALUES (%s, %s, %s)'''
    cursor.execute(consulta, (id, salida, destino))
    messagebox.showinfo("EXITO", "Registro Satisfactorio") 
    conn.commit()
    conn.close()
       
def registrar_bus(id, placa, capacidad, idempleado):
  if(id=="" or placa == "" or capacidad == "" or idempleado == ""):
    messagebox.showinfo("ERROR", "Por favor ingresar todos los campos")
  else:
    conn = psycopg2.connect(dbname = "terminal_transporte", 
                            user  = "postgres", 
                            password = "1234", 
                            host = "localhost")
    cursor = conn.cursor()
    consulta = '''INSERT INTO bus (idbus, placa, capacidad, idempleado) VALUES (%s, %s, %s, %s)'''
    cursor.execute(consulta, (id, placa, capacidad, idempleado))
    messagebox.showinfo("EXITO", "Registro Satisfactorio") 
    conn.commit()
    conn.close()
    
def registrar_conductor(id, nombre, apellido, telefono, cedula):
  if(id=="" or nombre == "" or apellido == "" or telefono == "" or cedula ==""):
    messagebox.showinfo("ERROR", "Por favor ingresar todos los campos")
  else:
    conn = psycopg2.connect(dbname = "terminal_transporte", 
                            user  = "postgres", 
                            password = "1234", 
                            host = "localhost")
    cursor = conn.cursor()
    consulta = '''INSERT INTO empleado (idempleado, nombre, apellido, telefono, cedula) VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(consulta, (id, nombre, apellido, telefono, cedula))
    messagebox.showinfo("EXITO", "Registro Satisfactorio") 
    conn.commit()
    conn.close()
    
def registrar_compra(idruta, idempleado, idbus, id_cedula,valor):   
  if(id_cedula=="" or idempleado == "" or idbus == "" or idruta == ""or valor=="" ):
    messagebox.showinfo("ERROR", "Por favor ingresar todos los campos")
  else:
    factura = ""
    conn = psycopg2.connect(dbname = "terminal_transporte", 
                            user  = "postgres", 
                            password = "1234", 
                            host = "localhost")
    cursor = conn.cursor()
    consulta = '''INSERT INTO venta_tiquete (idruta, idempleado, idbus, id_cedula,valor) VALUES (%s, %s, %s, %s,%s)'''
    cursor.execute(consulta, (idruta, idempleado,idbus,id_cedula,valor))
    messagebox.showinfo("EXITO", "Registro Satisfactorio") 
        
# Crear un mensaje de factura

    factura = f"FACTURA DE COMPRA\n\n"
    factura += f"ID Ruta: {idruta}\n"
    factura += f"ID Empleado: {idempleado}\n"
    factura += f"ID Bus: {idbus}\n"
    factura += f"ID Cédula: {id_cedula}\n"
    factura += f"Valor: {valor}\n"
            

            
            # Mostrar la factura en un messagebox
    messagebox.showinfo("Registro Satisfactorio", factura)
               
    conn.commit()
    conn.close()       
           
def registrar_pasajero(cedula, nombre, apellido, telefono, correo):   
  if(cedula=="" or nombre == "" or apellido == "" or telefono == "" or correo ==""):
    messagebox.showinfo("ERROR", "Por favor ingresar todos los campos")
  else:
    conn = psycopg2.connect(dbname = "terminal_transporte", 
                            user  = "postgres", 
                            password = "1234", 
                            host = "localhost")
    cursor = conn.cursor()
    consulta = '''INSERT INTO cliente (id_cedula, nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s, %s)'''
    cursor.execute(consulta, (cedula, nombre, apellido, telefono, correo))
    messagebox.showinfo("EXITO", "Registro Satisfactorio")        
    conn.commit()
    conn.close()
                 
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
    r.config(bg = "darkblue", foreground="white")

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
    r.config(bg = "darkblue", foreground="white")
    
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

    entry_cedulae = Entry(frame, validate= 'key', validatecommand=(frame.register(entrada_int), "%S",))
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
    
    entry_ide = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P" ))
    entry_ide.grid(row = 13, column = 1)
    
    r = Button(frame, text='Registrar', command = lambda:registrar_conductor(entry_ide.get(), 
                                                                            entry_nombree.get(), 
                                                                            entry_apellidoe.get(), 
                                                                            entry_telefonoe.get(), 
                                                                            entry_cedulae.get()))
    r.grid(row=55, column=3, sticky=W+E)
    r.config(bg = "darkblue", foreground="white")
    
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
    r.config(bg = "darkblue", foreground="white")
    
    pasajero_ventana.mainloop()

def venta_tiquete():
    venta_tiquete_ventana = Toplevel()
    venta_tiquete_ventana.title("Venta de Tiquete")
    venta_tiquete_ventana.geometry("400x250")
    canvas = Canvas(venta_tiquete_ventana, height=400, width=250)
    canvas.pack()
    frame = Frame(venta_tiquete_ventana)
    frame.place(relx=0, rely=0, relheight=1, relwidth=1,)
    frame.config(bg='#2caa67')

    label = Label(frame, text='Venta de Tiquete')
    label.grid(row=0, column=1)
    label.config(foreground='#6aa9e9', font=("Helvetica", 13, "bold"), background="#e2f0cb")

    label = Label(frame, text="ID Pasajero:    ")
    label.grid(row=1, column=0)
    label.config(background="#e2f0cb")
    
    id_cedula = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    id_cedula.grid(row=1, column=1)

    label = Label(frame, text="ID Empleado: ")
    label.grid(row=2, column=0)
    label.config(background="#e2f0cb")

    idempleado = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idempleado.grid(row=2, column=1)

    label = Label(frame, text="ID Bus:            ")
    label.grid(row=3, column=0)
    label.config(background="#e2f0cb")

    idbus = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idbus.grid(row=3, column=1)
    
    label = Label(frame, text="ID Ruta          ")
    label.grid(row=4, column=0)
    label.config(background="#e2f0cb")

    idruta = Entry(frame, validate='key', validatecommand=(frame.register(entrada_id), "%S", "%P"))
    idruta.grid(row=4, column=1)
    
    label = Label(frame, text="Valor:              ")
    label.grid(row=5, column=0)
    label.config(background="#e2f0cb")

    valor = Entry(frame, validate='key', validatecommand=(frame.register(entrada_int), "%S"))
    valor.grid(row=5, column=1)
    
    s = Button(frame, text='Metodo de Pago', command=metodo_pago)
    s.grid(row=65, column=2)
    s.config(bg = "#38a4aa", foreground="black")
    
          
    r = Button(frame, text='Registrar', command = lambda:registrar_compra(idruta.get(), 
                                                                            idempleado.get(), 
                                                                            idbus.get(), 
                                                                            id_cedula.get(),
                                                                            valor.get()))
    r.grid(row=80, column=2) #90c3ce
    r.config(bg = "#90c3ce", foreground="black")    

def metodo_pago():
    root = Tk()
    root.title("Método de Pago")
    root.geometry("300x100")
    root.config(bg = "darkblue")

    efectivo_button = Button(root, text="Efectivo", command=seleccion_efectivo)
    efectivo_button.pack(pady=2)
    efectivo_button.config(bg = "darkgreen", foreground="white")

    transferencia_button = Button(root, text="Transferencia", command=seleccion_transferencia)
    transferencia_button.pack(pady=3)
    transferencia_button.config(bg = "darkgreen", foreground="white")

    tarjeta_button = Button(root, text="Tarjeta", command=seleccion_tarjeta)
    tarjeta_button.pack(pady=3) 
    tarjeta_button.config(bg = "darkgreen", foreground="white")
             
def eliminar():
    ventana_eliminar = Toplevel(root)
    ventana_eliminar.title("Eliminar Registro")
    ventana_eliminar.geometry("300x150")

    label = Label(ventana_eliminar, text="Ingrese ID del registro a eliminar:")
    label.pack(pady=10)

    id_entry = Entry(ventana_eliminar)
    id_entry.pack()

    eliminar_btn = Button(ventana_eliminar, text="Eliminar", command=lambda: eliminar_registro(id_entry.get()))
    eliminar_btn.pack(pady=10)

def eliminar_registro(id_registro):
    if id_registro:
        try:
            conn = psycopg2.connect(dbname="terminal_transporte", user="postgres", password="1234", host="localhost")
            cursor = conn.cursor()
            primer_caracter = int(id_registro[0])

            # Aquí ejecuta la consulta SQL para eliminar el registro con el ID proporcionado
            if primer_caracter == 1:
              consulta = "DELETE FROM cliente WHERE id_cedula = %s"  # Reemplaza 'tabla' con el nombre de la tabla adecuado
            elif primer_caracter == 2:
              consulta = "DELETE FROM empleado WHERE idempleado = %s"
            elif primer_caracter == 4:
              consulta = "DELETE FROM venta_tiquete WHERE idruta = %s"  
            
              
            cursor.execute(consulta, (id_registro,))

            conn.commit()
            conn.close()

            messagebox.showinfo("Éxito", "Registro eliminado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el registro: {str(e)}")
            
def modificar():
    ventana_modificar = Toplevel(root)
    ventana_modificar.title("Modificar Registro")
    ventana_modificar.geometry("300x200")

    label = Label(ventana_modificar, text="Ingrese ID de cédula:")
    label.pack(pady=10)

    id_entry = Entry(ventana_modificar)
    id_entry.pack()

    buscar_btn = Button(ventana_modificar, text="Buscar", command=lambda: mostrar_datos(id_entry.get(), ventana_modificar))
    buscar_btn.pack(pady=10)

def mostrar_datos(id_cedula, ventana_modificar):
    registro = buscar_registro(id_cedula)
    primer_caracter = int(id_cedula[0])
    
    if primer_caracter == 1:
        # Realiza una búsqueda específica para el caso en que el primer carácter sea 'A'
        registro = buscar_registro(id_cedula)
        if registro:
            # Aquí puedes definir acciones específicas para el caso 'A'
            campos = ["nombre", "apellido", "telefono", "correo"]
            entries = {}

            for idx, campo in enumerate(campos):
                label = Label(ventana_modificar, text=campo.capitalize())
                label.pack()

                entry = Entry(ventana_modificar)
                entry.insert(0, registro[idx + 1])  # Saltamos el ID de cédula en la tupla
                entry.pack()

                entries[campo] = entry

    elif primer_caracter == 2:
        # Realiza una búsqueda específica para el caso en que el primer carácter sea 'B'
        registro = buscar_registro(id_cedula)
        if registro:
            # Aquí puedes definir acciones específicas para el caso 'B'
            campos = ["nombre", "apellido", "telefono", "cedula"]  # Cambia los nombres de los campos
            entries = {}

            for idx, campo in enumerate(campos):
                label = Label(ventana_modificar, text=campo.capitalize())
                label.pack()

                entry = Entry(ventana_modificar)
                entry.insert(0, registro[idx + 1])  # Saltamos el ID de cédula en la tupla
                entry.pack()

                entries[campo] = entry
                
    elif primer_caracter == 4:
        # Realiza una búsqueda específica para el caso en que el primer carácter sea 'B'
        registro = buscar_registro(id_cedula)
        if registro:
            # Aquí puedes definir acciones específicas para el caso 'B'
            campos = ["idempleado", "idbus", "id_cedula", "valor"]  # Cambia los nombres de los campos
            entries = {}

            for idx, campo in enumerate(campos):
                label = Label(ventana_modificar, text=campo.capitalize())
                label.pack()

                entry = Entry(ventana_modificar)
                entry.insert(0, registro[idx + 1])  # Saltamos el ID de cédula en la tupla
                entry.pack()

                entries[campo] = entry
    
    modificar_btn = Button(ventana_modificar, text="Modificar", command=lambda: aplicar_modificacion(id_cedula, entries))
    modificar_btn.pack(pady=10)

def aplicar_modificacion(id_cedula, entries):
    try:
        conn = psycopg2.connect(dbname="terminal_transporte", user="postgres", password="1234", host="localhost")
        cursor = conn.cursor()

        primer_caracter = int(id_cedula[0])  # Convertir el primer carácter a un entero

        if primer_caracter == 1:
            # Realiza una modificación específica para el caso en que el primer carácter sea '1'
            campos = ["nombre", "apellido", "telefono", "correo"]
            consulta = "UPDATE cliente SET nombre=%s, apellido=%s, telefono=%s, correo=%s WHERE id_cedula=%s"
        elif primer_caracter == 2:
            # Realiza una modificación específica para el caso en que el primer carácter sea '2'
            campos = ["nombre", "apellido", "telefono", "cedula"]
            consulta = "UPDATE empleado SET nombre=%s, apellido=%s, telefono=%s, cedula=%s WHERE idempleado=%s"
        elif primer_caracter == 4:
            # Realiza una modificación genérica para otros casos
            campos = ["idempleado", "idbus", "id_cedula", "valor"]
            consulta = "UPDATE venta_tiquete SET idempleado=%s, idbus=%s, id_cedula=%s, valor=%s WHERE idruta=%s"

        valores = [entries[campo].get() for campo in campos]

        cursor.execute(consulta, (*valores, id_cedula))

        conn.commit()
        conn.close()

        messagebox.showinfo("Éxito", "Modificación exitosa")
  
    except Exception as e:
        messagebox.showerror("Error", f"Error al modificar el registro: {str(e)}")

def buscar_registro(id_cedula):
    try:
        conn = psycopg2.connect(dbname="terminal_transporte", user="postgres", password="1234", host="localhost")
        cursor = conn.cursor()

        # Obtén el primer carácter de id_cedula
        primer_caracter = int(id_cedula[0])

        if primer_caracter == 1:
            # Realiza una búsqueda específica para el caso en que el primer carácter sea 'A'
            consulta = "SELECT * FROM cliente WHERE id_cedula = %s"
        elif primer_caracter == 2:
            # Realiza una búsqueda específica para el caso en que el primer carácter sea 'B'
            consulta = "SELECT * FROM empleado WHERE idempleado = %s"
        elif primer_caracter == 4:
            # Realiza una búsqueda específica para el caso en que el primer carácter sea 'B'
            consulta = "SELECT * FROM venta_tiquete WHERE idruta = %s"

        cursor.execute(consulta, (id_cedula,))
        registro = cursor.fetchone()

        conn.close()

        return registro
        

    except Exception as e:
        messagebox.showerror("Error", f"Error al buscar el registro: {str(e)}")
        return None

 
root = Tk()
menu = ttk.Style()
menu = tk.Menu(root)
root.config(menu=menu)
root.title("Terminal de Transporte")
root.geometry("400x250")
canvas = Canvas(root, height = 400, width = 250)
canvas.pack()


framep = Frame() 
framep.place(relx=0, rely=0, relheight=1, relwidth=1)

image = PhotoImage(file = "bus.png")
label = Label(framep, image=image)
label.place(relheight=1, relwidth=1)
registros_submenu = tk.Menu(menu)
ventaTicket_submenu = tk.Menu(menu)
menu.add_cascade(label="Registros", menu=registros_submenu)
menu.add_cascade(label="Venta", menu=ventaTicket_submenu)
registros_submenu.add_command(label="Pasajeros", command=lambda: pasajero_boton())
registros_submenu.add_command(label="Conductores", command=lambda: conductor_boton())
registros_submenu.add_command(label="Rutas", command=lambda: ruta_boton())
registros_submenu.add_command(label="Buses", command=lambda: bus_boton())
ventaTicket_submenu.add_command(label="Vender Ticket", command=lambda: venta_tiquete())

modificar_btn = Button(framep, text="Modificar", command=modificar) 
modificar_btn.grid(row=15, column=0)

eliminar_btn = Button(framep, text="Eliminar", command=eliminar)
eliminar_btn.grid(row=15, column=1)

root.mainloop()