# type:ignore
import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()
U_password = os.getenv("U_Password")
U_user = os.getenv("U_User")

def capturar_valor():
    user = campo_entrada_usuario.get()
    password = campo_entrada_password.get()
    print(user, password)
 
 #Las condiciones para saber cual mensaje corresponde, según la situación.
    if user == U_user and password == U_password:
        mensaje.config(text="Acceso correcto", foreground= "Green")

        print("Acceso correcto")

        print()
        
    else:
        mensaje.config(text="Usuario o contraseña incorrectos", foreground= "red")

        print("Usuario o contraseña incorrectos")

        print()


ventana = tk.Tk()  # Instanciando la clase Tk de Tkinter
ventana.title("Mi primera app en tkinter")
ventana.geometry("300x300")

# Label o texto que se muestra
label_usuario = tk.Label(ventana, text="Usuario", foreground="#FF0000")
label_usuario.pack()

# Campo de entrada -> input
campo_entrada_usuario = tk.Entry(ventana)
campo_entrada_usuario.pack()

label_password = tk.Label(ventana, text="Password")
label_password.pack()

campo_entrada_password = tk.Entry(ventana, show="*")
campo_entrada_password.pack()

# Botón
boton = tk.Button(ventana, text="Capturar", command=capturar_valor)
boton.pack(pady=10)

        #Nuevo label con la variable mensaje para utilizar con tk y poderlo añadir a la ventana de la ap
mensaje = tk.Label(ventana, text="")
mensaje.pack()


# Bucle principal que está en escucha de eventos
ventana.mainloop()
