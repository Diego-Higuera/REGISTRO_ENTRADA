
#RRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEE        GGGGGGGGGGGGGIIIIIIIIII   SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTTRRRRRRRRRRRRRRRRR        OOOOOOOOO     
#R::::::::::::::::R  E::::::::::::::::::::E     GGG::::::::::::GI::::::::I SS:::::::::::::::ST:::::::::::::::::::::TR::::::::::::::::R     OO:::::::::OO   
#R::::::RRRRRR:::::R E::::::::::::::::::::E   GG:::::::::::::::GI::::::::IS:::::SSSSSS::::::ST:::::::::::::::::::::TR::::::RRRRRR:::::R  OO:::::::::::::OO 
#RR:::::R     R:::::REE::::::EEEEEEEEE::::E  G:::::GGGGGGGG::::GII::::::IIS:::::S     SSSSSSST:::::TT:::::::TT:::::TRR:::::R     R:::::RO:::::::OOO:::::::O
  #R::::R     R:::::R  E:::::E       EEEEEE G:::::G       GGGGGG  I::::I  S:::::S            TTTTTT  T:::::T  TTTTTT  R::::R     R:::::RO::::::O   O::::::O
  #R::::R     R:::::R  E:::::E             G:::::G                I::::I  S:::::S                    T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::RRRRRR:::::R   E::::::EEEEEEEEEE   G:::::G                I::::I   S::::SSSS                 T:::::T          R::::RRRRRR:::::R O:::::O     O:::::O
  #R:::::::::::::RR    E:::::::::::::::E   G:::::G    GGGGGGGGGG  I::::I    SS::::::SSSSS            T:::::T          R:::::::::::::RR  O:::::O     O:::::O
  #R::::RRRRRR:::::R   E:::::::::::::::E   G:::::G    G::::::::G  I::::I      SSS::::::::SS          T:::::T          R::::RRRRRR:::::R O:::::O     O:::::O
  #R::::R     R:::::R  E::::::EEEEEEEEEE   G:::::G    GGGGG::::G  I::::I         SSSSSS::::S         T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::R     R:::::R  E:::::E             G:::::G        G::::G  I::::I              S:::::S        T:::::T          R::::R     R:::::RO:::::O     O:::::O
  #R::::R     R:::::R  E:::::E       EEEEEE G:::::G       G::::G  I::::I              S:::::S        T:::::T          R::::R     R:::::RO::::::O   O::::::O
#RR:::::R     R:::::REE::::::EEEEEEEE:::::E  G:::::GGGGGGGG::::GII::::::IISSSSSSS     S:::::S      TT:::::::TT      RR:::::R     R:::::RO:::::::OOO:::::::O
#R::::::R     R:::::RE::::::::::::::::::::E   GG:::::::::::::::GI::::::::IS::::::SSSSSS:::::S      T:::::::::T      R::::::R     R:::::R OO:::::::::::::OO 
#R::::::R     R:::::RE::::::::::::::::::::E     GGG::::::GGG:::GI::::::::IS:::::::::::::::SS       T:::::::::T      R::::::R     R:::::R   OO:::::::::OO   
#RRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEE        GGGGGG   GGGGIIIIIIIIII SSSSSSSSSSSSSSS         TTTTTTTTTTT      RRRRRRRR     RRRRRRR     OOOOOOOOO     



#          ╔╦╗╔═╗  ╔═╗╔╗╔╔╦╗╦═╗╔═╗╔╦╗╔═╗  ╦ ╦  ╔═╗╔═╗╦  ╦╔╦╗╔═╗
#           ║║║╣   ║╣ ║║║ ║ ╠╦╝╠═╣ ║║╠═╣  ╚╦╝  ╚═╗╠═╣║  ║ ║║╠═╣
#          ═╩╝╚═╝  ╚═╝╝╚╝ ╩ ╩╚═╩ ╩═╩╝╩ ╩   ╩   ╚═╝╩ ╩╩═╝╩═╩╝╩ ╩
    








"Este programa implementa un sistema de gestión de usuarios y registros de entrada/salida utilizando la biblioteca `tkinter` para crear una interfaz gráfica." 
"Las funcionalidades principales del programa incluyen:"

"1. **Conexión a una Base de Datos MySQL**: Establece conexión con una base de datos MySQL para manejar usuarios, motivos y registros."
"2. **Gestión de Usuarios**: Permite registrar nuevos usuarios, almacenando su DNI, nombre de usuario y contraseña en una lista simulada en memoria."
"3. **Autenticación de Usuarios**: Proporciona una interfaz de login donde los usuarios pueden ingresar con su nombre de usuario y contraseña."
"4. **Registro de Entradas y Salidas**: Permite a los usuarios registrar entradas y salidas, especificando el motivo y almacenando la fecha y hora."
"5. **Consulta de Datos**: Facilita la visualización de usuarios, motivos y registros mediante consultas a la base de datos."
"6. **Interfaz Gráfica**: Utiliza `tkinter` y `customtkinter` para crear diversas ventanas y widgets (como comboboxes y botones) para interactuar con el sistema."

"En resumen, el programa es una aplicación de escritorio que combina la gestión de bases de datos y una interfaz gráfica para administrar el acceso de usuarios y sus registros de actividad."








"--------------------------------------------------------------------------------------------------------------------------------------------------------"

import tkinter as tk  # Importa el módulo principal de Tkinter para la creación de interfaces gráficas.
from tkinter import ttk, simpledialog  # Importa widgets específicos de Tkinter y el módulo de diálogos simples.
from tkinter import messagebox  # Importa el módulo de cuadros de mensaje de Tkinter.
from datetime import datetime  # Importa la clase datetime para trabajar con fechas y horas.
from tkinter import *  # Importa todos los widgets y funciones de Tkinter.
import os  # Importa el módulo OS para interactuar con el sistema operativo.
import customtkinter as ctk  # Importa CustomTkinter, una extensión para personalizar los widgets de Tkinter.
import mysql.connector  # Importa el conector MySQL para conectar y manejar bases de datos MySQL.
from mysql.connector import Error  # Importa la clase Error del conector MySQL para manejar excepciones específicas de MySQL.

"--------------------------------------------------------------------------------------------------------------------------------------------------------"


 



# FUNCIÓN PARA CONECTAR A LA BASE DE DATOS MYSQL
def conectar_db():
    try:
        # Intenta establecer la conexión con la base de datos MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="FPJ"
        )
        # Verifica si la conexión fue exitosa
        if conexion.is_connected():
            return conexion
    except Error as e:
        # Imprime un mensaje de error si la conexión falla
        print(f"Error al conectar a MySQL: {e}")
        return None



# FUNCIÓN PARA CERRAR LA CONEXIÓN CON LA BASE DE DATOS MYSQL
def cerrar_db(conexion):
    if conexion.is_connected():
        conexion.close()



# FUNCIÓN PARA VER LOS USUARIOS EN LA BASE DE DATOS
def ver_usuarios():
    conexion = conectar_db()  # Conecta a la base de datos
    cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
    cursor.execute("SELECT * FROM USUARIOS")  # Ejecuta una consulta para seleccionar todos los usuarios
    usuarios = cursor.fetchall()  # Recupera todos los registros de la consulta
    for usuario in usuarios:
        print(f"DNI: {usuario[0]}, Nombre de Usuario: {usuario[1]}, Contraseña: {usuario[2]}")  # Imprime los detalles de cada usuario
    cerrar_db(conexion)  # Cierra la conexión con la base de datos



# FUNCIÓN PARA VER LOS MOTIVOS EN LA BASE DE DATOS
def ver_motivos():
    conexion = conectar_db()  # Conecta a la base de datos
    cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
    cursor.execute("SELECT * FROM MOTIVOS")  # Ejecuta una consulta para seleccionar todos los motivos
    motivos = cursor.fetchall()  # Recupera todos los registros de la consulta
    for motivo in motivos:
        print(f"ID: {motivo[0]}, Descripción: {motivo[1]}")  # Imprime los detalles de cada motivo
    cerrar_db(conexion)  # Cierra la conexión con la base de datos



# FUNCIÓN PARA VER LOS REGISTROS EN LA BASE DE DATOS
def ver_registros():
    conexion = conectar_db()  # Conecta a la base de datos
    cursor = conexion.cursor()  # Crea un cursor para ejecutar consultas
    query = """
    SELECT r.ID, u.NOMBRE_USUARIO, r.FICHAJE, m.DESCRIPCION, r.FECHA_HORA
    FROM REGISTROS r
    JOIN USUARIOS u ON r.NOMBRE_USUARIO = u.NOMBRE_USUARIO
    JOIN MOTIVOS m ON r.MOTIVO_ID = m.ID
    """  # Consulta para seleccionar detalles de los registros, uniendo tablas relacionadas
    cursor.execute(query)  # Ejecuta la consulta
    registros = cursor.fetchall()  # Recupera todos los registros de la consulta
    for registro in registros:
        print(f"ID: {registro[0]}, Usuario: {registro[1]}, Fichaje: {registro[2]}, Motivo: {registro[3]}, Fecha y Hora: {registro[4]}")  # Imprime los detalles de cada registro
    cerrar_db(conexion)  # Cierra la conexión con la base de datos



# EJEMPLO DE LLAMADA A LAS FUNCIONES PARA VISUALIZAR DATOS DE LA BASE DE DATOS
ver_usuarios()  # Llama a la función para ver todos los usuarios
ver_motivos()   # Llama a la función para ver todos los motivos
ver_registros() # Llama a la función para ver todos los registros


# LISTA DE USUARIOS REGISTRADOS (SIMULANDO UNA BASE DE DATOS EN MEMORIA)
usuarios = []
# LISTA DE REGISTROS DE ENTRADA/SALIDA
registros = []



# FUNCIÓN PARA MANEJAR EL LOGIN
def login():
    """
    Maneja el proceso de login verificando las credenciales del usuario.
    Si el nombre de usuario y la contraseña coinciden, se inicia la sesión.
    """
    nombre = nombre_usuario_combobox.get()
    contraseña = contraseña_entry.get()
    for user in usuarios:
        if user['NOMBRE DE USUARIO'] == nombre and user['CONTRASEÑA'] == contraseña:
            usuario_actual.set(nombre)
            messagebox.showinfo("Login", f"INICIO DE SESION EXITOSO PARA EL USUARIO: {nombre}")
            ventana_fichaje.deiconify()  # Muestra la ventana de fichaje
            root.withdraw()  # Oculta la ventana principal
            return
    messagebox.showwarning("Login", "USUARIO O CONTRASEÑA INCORRECTO.")  # Muestra una advertencia si las credenciales son incorrectas



# FUNCIÓN PARA ABRIR LA VENTANA DE AGREGAR USUARIO
def añadir_usuario():
    """
    Muestra la ventana para agregar un nuevo usuario.
    """
    ventana_usuario.deiconify()

# FUNCIÓN PARA ABRIR LA VENTANA DE CONSULTA DE FICHAJES
def consultar_fichaje():
    """
    Muestra la ventana para consultar fichajes.
    """
    ventana_fichaje.deiconify()



# FUNCIÓN PARA REGISTRAR UN NUEVO USUARIO
def registro_usuario():
    """
    Registra un nuevo usuario después de verificar que todos los campos están completos
    y que las contraseñas coinciden.
    """
    dni = dni_entry.get()
    nombre_usuario = name_entry.get()
    contraseña = user_password_entry.get()
    confirmar_contraseña = confirm_password_entry.get()
    
    if not dni or not nombre_usuario or not contraseña:
        messagebox.showwarning("Registro", "TODOS LOS CAMPOS SON OBLIGATORIOS.")
        return

    if contraseña != confirmar_contraseña:
        messagebox.showwarning("Registro", "LAS CONTRASEÑAS NO COINCIDEN")
        return



    # REGISTRO DEL USUARIO
    usuario = {
        'DNI': dni,
        'NOMBRE DE USUARIO': nombre_usuario,
        'CONTRASEÑA': contraseña
    }
    usuarios.append(usuario)  # Agrega el nuevo usuario a la lista de usuarios
    update_user_combobox()  # Actualiza el combobox de usuarios
    messagebox.showinfo("Registro", f"Usuario {nombre_usuario} REGISTRADO EXITOSAMENTE")
    ventana_usuario.withdraw()  # Oculta la ventana de registro de usuario



# FUNCIÓN PARA ACTUALIZAR EL COMBOBOX DE USUARIOS
def update_user_combobox():
    """
    Actualiza el combobox de nombres de usuario con los usuarios registrados.
    """
    nombre_usuarios = [user['NOMBRE DE USUARIO'] for user in usuarios]
    nombre_usuario_combobox['values'] = nombre_usuarios



# FUNCIÓN PARA REGISTRAR LA ENTRADA/SALIDA
def register_entry_exit():
    """
    Registra la entrada o salida de un usuario con un motivo específico y la fecha y hora actual.
    """
    username = usuario_actual.get()
    fichaje = fichaje_combobox.get()
    motivo = motivo_combobox.get()
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    if not fichaje or not motivo:
        messagebox.showwarning("Registro", "TODOS LOS CAMPOS SON OBLIGATORIOS")
        return

    registro = {
        'NOMBRE DE USUARIO': username,
        'fichaje': fichaje,
        'motivo': motivo,
        'fecha_hora': fecha_hora
    }
    registros.append(registro)  # Agrega el nuevo registro a la lista de registros
    messagebox.showinfo("Registro", f"{fichaje} REGISTRADO EXITOSAMENTE {username}")
    ventana_fichaje.withdraw()  # Oculta la ventana de fichaje
    update_records_combobox()  # Actualiza el combobox de registros



# FUNCIÓN PARA ACTUALIZAR EL COMBOBOX DE REGISTROS
def update_records_combobox():
    """
    Actualiza el combobox de registros con la información de los registros existentes.
    Cada registro se muestra en el formato: "fecha_hora - NOMBRE DE USUARIO - fichaje - motivo".
    """
    registro_str = [f"{r['fecha_hora']} - {r['NOMBRE DE USUARIO']} - {r['fichaje']} - {r['motivo']}" for r in registros]
    records_combobox['values'] = registro_str



# FUNCIÓN PARA APLICAR PLACEHOLDERS A WIDGETS DE ENTRADA
def apply_placeholder(widget, placeholder_text):
    """
    Aplica un texto de marcador de posición (placeholder) a un widget de entrada.
    El texto del placeholder se muestra en gris y desaparece cuando el widget recibe foco.
    
    Args:
        widget: El widget de entrada (por ejemplo, Entry o Combobox) al que se le aplicará el placeholder.
        placeholder_text: El texto del placeholder.
    """
    def on_focus_in(event):
        if widget.get() == placeholder_text:
            widget.delete(0, tk.END)
            widget.config(fg='black') # Agregar el (SHOW) para ocultar la contraseña y no sea visible 
    
    def on_focus_out(event):
        if widget.get() == '':
            widget.insert(0, placeholder_text)
            widget.config(fg='grey')
    
    widget.insert(0, placeholder_text)
    widget.config(foreground='grey')
    widget.bind("<FocusIn>", on_focus_in)
    widget.bind("<FocusOut>", on_focus_out)



# FUNCIÓN PARA ABRIR LA VENTANA DE REGISTRO DE USUARIOS
def abrir_ventana_registro():
    """
    Muestra la ventana para registrar nuevos usuarios.
    """
    ventana_usuario.deiconify()

# Función para limpiar los campos de entrada en la ventana de registro
def limpiar_campos_registro():
    """
    Limpia los campos de entrada en la ventana de registro de usuarios.
    """
    dni_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    user_password_entry.delete(0, 'end')
    confirm_password_entry.delete(0, 'end')







#  ***************************************************************************************************************************** #

"                                                      VENTANA PRINCIPAL                                                         "                                                                                                         

#  ***************************************************************************************************************************** #




# VENTANA PRINCIPAL
root = tk.Tk()
root.title("ACCESO USUARIOS/SISTEMA DE FICHAJE")
root.configure(bg="black")  # Establece el color de fondo en negro



# CREAR EL OBJETO STYLE PARA EL COMBOBOX
style = ttk.Style()


# MOSTRAR LOS TEMAS DISPONIBLES
print(style.theme_names())  # Imprime los nombres de los temas disponibles


# USAR UN TEMA DIFERENTE
style.theme_use('clam')  # Puedes usar cualquier tema disponible: 'clam', 'alt', 'default', 'classic'


# TÍTULO CON MARCOS Y BORDES
title_frame = tk.LabelFrame(root, relief=tk.GROOVE, borderwidth=7, bg="black")
title_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# LABEL PARA EL TÍTULO
title_label = tk.Label(title_frame, text="                         SISTEMA DE ACCESO                         ",
bg="black", fg="white", font=("impact", 16))
title_label.pack(padx=10, pady=10)


"--------------------------------------------------------------------------------------------------------------------------------------------------------"

# VARIABLE PARA ALMACENAR EL USUARIO ACTUAL
usuario_actual = tk.StringVar()

"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# FRAME DE LOGIN
login_frame = tk.LabelFrame(root, relief=tk.GROOVE, borderwidth=7, text="  LOGIN   ", bg="black", fg="gray", font=("impact", 12))
login_frame.grid(padx=10, pady=0)

# LABELS Y CAMPOS DE ENTRADA DENTRO DEL FRAME DE LOGIN
nombre_usuario_combobox = ttk.Combobox(login_frame, width=55) #state="readonly")  # Ajusta el ancho según sea necesario
nombre_usuario_combobox.grid(row=0, column=1, padx=18, pady=5, sticky="e")
apply_placeholder(nombre_usuario_combobox, "INGRESE SU NOMBRE DE USUARIO")  # Aplica placeholder al combobox

contraseña_entry = tk.Entry(login_frame, show="", width=56, border=8)  # Ajusta el ancho según sea necesario
contraseña_entry.grid(row=1, column=1, padx=18, pady=5, sticky="e")
apply_placeholder(contraseña_entry, "INGRESE SU CONTRASEÑA")  # Aplica placeholder al campo de contraseña


# BOTÓN DE LOGIN DENTRO DEL FRAME DE LOGIN
tk.Button(login_frame, text="                                   ENTRAR                                   ", command=login, 
bg="green", fg="white", font=("Verdana", 8), borderwidth=12).grid(row=2, columnspan=2, pady=10)


# TEXTO DE REGISTRO DENTRO DEL FRAME DE LOGIN
texto_registro = tk.Label(login_frame, text="¿NO TIENES UNA CUENTA?", bg="black", fg="white")
texto_registro.grid(row=3, column=0, columnspan=2, pady=0)


# BOTÓN DE REGISTRO COMO UN LABEL (PARA SIMULAR UN ENLACE)
boton_registro = tk.Label(login_frame, text="REGISTRATE", fg="dodger blue", cursor="hand2", bg="black")
boton_registro.grid(row=4, column=0, columnspan=2, pady=5)
boton_registro.bind("<Button-1>", lambda e: abrir_ventana_registro())  # Vincula el evento de clic para abrir la ventana de registro



"--------------------------------------------------------------------------------------------------------------------------------------------------------"



# FRAME DE OPERACIONES
operaciones_frame = tk.LabelFrame(root, text="  OPERACIONES:   ", bg="black", fg="gray", font=("impact", 12), borderwidth=7)
operaciones_frame.grid(padx=10, pady=10)


# BOTÓN PARA CONSULTAR FICHAJES DENTRO DEL FRAME DE OPERACIONES
tk.Button(operaciones_frame, text="                          CONSULTAR FICHAJE                          ", 
command=consultar_fichaje, bg="gray", fg="white" , borderwidth=9).grid(row=0, column=1, padx=6, pady=5)


# BOTÓN PARA SALIR DE LA APLICACIÓN DENTRO DEL FRAME DE OPERACIONES
tk.Button(operaciones_frame, text=" SALIR  ", command=root.quit, bg="RED", fg="white", font=("Verdana", 8), 
borderwidth=9).grid(row=0, column=2, padx=6, pady=5)







#  ***************************************************************************************************************************** #

"                                                  VENTANA DE REGISTRO DE USUARIO                                                "                                                                                                         

#  ***************************************************************************************************************************** #




# CREAR UNA NUEVA VENTANA SECUNDARIA PARA EL REGISTRO DE USUARIO
ventana_usuario = tk.Toplevel(root)
ventana_usuario.title("REGISTRO DE USUARIO")  # Establece el título de la ventana
ventana_usuario.configure(bg="BLACK")  # Establece el color de fondo en negro
ventana_usuario.withdraw()  # Oculta la ventana al inicio



# CREAR EL LABELFRAME CON EL TÍTULO 'REGISTRARSE'
label_frame = tk.LabelFrame(ventana_usuario, text="  REGISTRARSE  ", padx=10, pady=10, bg="black", fg="gray", font=("impact", 12), borderwidth=7)
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")



# AÑADIR LOS WIDGETS AL LABELFRAME
dni_entry = tk.Entry(label_frame, width=45, border=8)  # Campo de entrada para el DNI
dni_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")
apply_placeholder(dni_entry, "INGRESE SU DNI")  # Aplica placeholder al campo DNI

name_entry = tk.Entry(label_frame, width=45, border=8)  # Campo de entrada para el nombre de usuario
name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="e")
apply_placeholder(name_entry, "INGRESE SU NOMBRE DE USUARIO")  # Aplica placeholder al campo nombre de usuario

user_password_entry = tk.Entry(label_frame, show="", width=45, border=8)  # Campo de entrada para la contraseña
user_password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="e")
apply_placeholder(user_password_entry, "INGRESE SU CONTRASEÑA")  # Aplica placeholder al campo contraseña

confirm_password_entry = tk.Entry(label_frame, show="", width=45, border=8)  # Campo de entrada para confirmar la contraseña
confirm_password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="e")
apply_placeholder(confirm_password_entry, "CONFIRME SU CONTRASEÑA")  # Aplica placeholder al campo confirmar contraseña



# BOTÓN DE REGISTRO DENTRO DEL LABELFRAME
btn_registro = Button(label_frame, text="                         REGISTRO                        ", bg="green", fg="white",
command=registro_usuario, font=("Verdana", 9), borderwidth=9)

btn_registro.grid(row=4, column=1, pady=10, padx=5, sticky="s")



# FUNCIÓN PARA LIMPIAR LOS CAMPOS DE REGISTRO DE USUARIO
def limpiar_campos_registro():
    dni_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    user_password_entry.delete(0, 'end')
    confirm_password_entry.delete(0, 'end')



# FUNCIÓN PARA REGISTRAR USUARIO
def registro_usuario():
    dni = dni_entry.get()
    nombre_usuario = name_entry.get()
    contraseña = user_password_entry.get()
    confirmar_contraseña = confirm_password_entry.get()
    
    if not dni or not nombre_usuario or not contraseña:
        messagebox.showwarning("Registro", "TODOS LOS CAMPOS SON OBLIGATORIOS.")  # Muestra una advertencia si hay campos vacíos
        return

    if contraseña != confirmar_contraseña:
        messagebox.showwarning("Registro", "LAS CONTRASEÑAS NO COINCIDEN")  # Muestra una advertencia si las contraseñas no coinciden
        return



# REGISTRO DEL USUARIO
    usuario = {
        'DNI': dni,
        'NOMBRE DE USUARIO': nombre_usuario,
        'CONTRASEÑA': contraseña
    }
    usuarios.append(usuario)  # Añade el nuevo usuario a la lista de usuarios
    update_user_combobox()  # Actualiza el combobox de usuarios
    messagebox.showinfo("Registro", f"Usuario {nombre_usuario} REGISTRADO EXITOSAMENTE")  # Muestra un mensaje de éxito
    ventana_usuario.withdraw()  # Oculta la ventana de registro
    limpiar_campos_registro()  # Limpia los campos después de registrar el usuario


"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# LABELFRAME CON BORDE NEGRO PARA EL BOTÓN DE CANCELAR
border = LabelFrame(ventana_usuario, bd=6, bg="black")
border.grid(pady=10)

# BOTÓN DE CANCELAR DENTRO DEL LABELFRAME
btn = Button(border, text="             CANCELAR              ", width=39, bg="red", command=ventana_usuario.withdraw, fg="white", font=("Verdana", 9))
btn.grid()


"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# # FUNCIÓN PARA EXPANDIR LA VENTANA PRINCIPAL
def expand_window():
    root.geometry("400x200")

# FUNCIÓN PARA CREAR LA VENTANA DE FICHAJE
def open_fichaje_window():
    ventana_fichaje.deiconify()  # Muestra la ventana de fichaje




    


#  ***************************************************************************************************************************** #

"                                               VENTANA DE REGISTRO DE ENTRADA/SALIDA                                            "                                                                                                         

#  ***************************************************************************************************************************** #




# VENTANA DE REGISTRO DE ENTRADA/SALIDA
ventana_fichaje = tk.Toplevel(root)  # Crea una ventana secundaria para el registro de entrada/salida
ventana_fichaje.title("REGISTRO DE ENTRADA/SALIDA")  # Establece el título de la ventana
ventana_fichaje.withdraw()  # Oculta la ventana al inicio
ventana_fichaje.configure(bg="BLACK")  # Establece el color de fondo en negro


"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# CREAR EL OBJETO STYLE Y ESTABLECER EL TEMA (ESTO ES PARA EL ESTILO DEL COMBOBOX)
style = ttk.Style()
style.theme_use('clam')  # Utiliza el tema 'clam' de ttk


"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# # CREAR EL LABELFRAME CON EL TÍTULO 'REGISTRO DE ENTRADA/SALIDA'
label_frame = tk.LabelFrame(ventana_fichaje, text="  REGISTRO DE ENTRADA/SALIDA  ", padx=10, pady=10, bg="black", fg="gray", font=("impact", 12), borderwidth=7)
label_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")



# ELEMENTOS DENTRO DEL LABELFRAME
fecha_entry = tk.Entry(label_frame, border=8, width=40)  # Campo de entrada para la fecha
fecha_entry.insert(0, datetime.now().strftime("  FECHA - %d/%m/%Y"))  # Inserta la fecha actual como marcador de posición
fecha_entry.grid(row=0, column=1, padx=5, pady=5)

hora_entry = tk.Entry(label_frame, border=8, width=40)  # Campo de entrada para la hora
hora_entry.insert(0, datetime.now().strftime("  HORA - %H:%M:%S"))  # Inserta la hora actual como marcador de posición
hora_entry.grid(row=1, column=1, padx=5, pady=5)

fichaje_combobox = ttk.Combobox(label_frame, width=40, values=["Entrada", "Salida"])  # Combobox para el tipo de fichaje
fichaje_combobox.grid(row=2, column=1, padx=5, pady=5)
apply_placeholder(fichaje_combobox, "FICHAJE")  # Aplica un marcador de posición al combobox de fichaje

motivo_combobox = ttk.Combobox(label_frame, width=40, values=["Trabajo", "Reunión", "Descanso"])  # Combobox para el motivo/razón
motivo_combobox.grid(row=3, column=1, padx=5, pady=5)
apply_placeholder(motivo_combobox, "MOTIVO/RAZÓN:")  # Aplica un marcador de posición al combobox de motivo/razón


"--------------------------------------------------------------------------------------------------------------------------------------------------------"


# BOTÓN PARA FICHAR DENTRO DEL LABELFRAME
tk.Button(label_frame, text="                        FICHAR                        ", command=register_entry_exit,
bg="green", fg="white", font=("Verdana", 9), borderwidth=9).grid(row=4, column=1, padx=10, pady=10, sticky="s")



# LABELFRAME CON BORDE NEGRO PARA EL BOTÓN DE CANCELAR
border = LabelFrame(ventana_fichaje, bd=6, bg="black")
border.grid(pady=10)



# BOTÓN DE CANCELAR DENTRO DEL LABELFRAME
btn=tk.Button(border, text="             CANCELAR              ", width=37, bg="red", command=ventana_fichaje.withdraw, fg="white", font=("Verdana", 9))
btn.grid()







#  ***************************************************************************************************************************** #

"                                                  VENTANA DE CONSULTAR REGISTRO                                                 "                                                                                                         

#  ***************************************************************************************************************************** #




# VENTANA PARA CONSULTAR REGISTROS
ventana_registro = tk.Toplevel(root)
ventana_registro.title("CONSULTAR REGISTRO")
ventana_registro.withdraw()

tk.Label(ventana_registro, text="REGISTRO:").grid(row=0, column=0, padx=5, pady=5)
records_combobox = ttk.Combobox(ventana_registro)
records_combobox.grid(row=0, column=1, padx=5, pady=5)




# CARGAR USUARIOS AL INICIAR LA APLICACIÓN
root.mainloop()







 
































