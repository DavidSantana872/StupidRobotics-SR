from tkinter import END
from main_robotica import *
import pyperclip # type: ignore
def guarda_numero_variable_punto_inicio(text_area):
    fichero_punto_inicio = open("puntodeinicio.txt", "w")
    fichero_punto_inicio.writelines((text_area.get(1.0, END)))
    text_area.delete("1.0", END)  # Limpiar todo el contenido del área de texto
 
    fichero_punto_inicio.close()
# get data of input 
# save data
def guardarDatosInput(text_area):
    fichero_puntos = open("Puntos.txt", "w")
    fichero_puntos.writelines(text_area.get(1.0, END))
    fichero_puntos.close()
# click in ver generar un copy al porta papeles
# de quaterniones.txt 
def copy_quaterniones_txt(text_area ):
    guardarDatosInput(text_area)
    main("PermitirModificarUltimoPunto")
    fichero_quaterniones = open("Quaterniones.txt", "r")
    contenido = fichero_quaterniones.read()
    pyperclip.copy(contenido)
  

# click in ayuda generar un copy al porta papeles
# de ComandosMain.txt 
def copy_comandosMain_txt(text_area):
    guardarDatosInput(text_area)
    main("NoPermitir")
    fichero_comandos_main = open("ComandosMain.txt", "r")
    contenido = fichero_comandos_main.read()
    print(contenido)
    pyperclip.copy(contenido)
    
