from tkinter import END
import pyperclip # type: ignore

def procesar_coordenadas(coordenadas_interfaz):
    fichero_resultados = open("comandos.txt", "w")
    
    coordenadas_interfaz = (coordenadas_interfaz.get(1.0, END))
    arreglo_coordenadas = coordenadas_interfaz.split("\n")
    
    arreglo_coordenadas = [elemento for elemento in arreglo_coordenadas if elemento.strip() != '']

    i = 0
    while i < len(arreglo_coordenadas):
        try:
            if arreglo_coordenadas[i].lower() == "l":
                fichero_resultados.writelines("!Este bloque de codigo entero pertenece a lineas unidas\n")
                arreglo_coordenadas.pop(i)
                while i < len(arreglo_coordenadas):
                    if len(arreglo_coordenadas[i]) > 1:
                        fichero_resultados.write(f"Haciendo Linea: {arreglo_coordenadas[i]}\n")
                    if len(arreglo_coordenadas[i]) <= 1:
                        fichero_resultados.write("\n\n\n")
                        break
                    arreglo_coordenadas.pop(i)
           
            elif arreglo_coordenadas[i].lower() == "c":
                arreglo_coordenadas.pop(i)
                fichero_resultados.write("!Circulo\n")
                while i < len(arreglo_coordenadas) - 1:
                    if len(arreglo_coordenadas[i]) > 1 and len(arreglo_coordenadas[i + 1]) > 1:
                        fichero_resultados.write(f"Haciendo Circulo: {arreglo_coordenadas[i]} - {arreglo_coordenadas[i + 1]}\n")
                    if len(arreglo_coordenadas[i]) <= 1:
                        fichero_resultados.write("\n\n\n")
                        break
                    arreglo_coordenadas.pop(i)
                    arreglo_coordenadas.pop(i)
                    
            elif arreglo_coordenadas[i].lower() == "s":
                
                fichero_resultados.write("!SemiCirculo\n")
                arreglo_coordenadas.pop(i)
                while i < len(arreglo_coordenadas):
                    if len(arreglo_coordenadas[i]) > 1 and len(arreglo_coordenadas[i + 1]) > 1:
                        fichero_resultados.write(f"Haciendo semi: {arreglo_coordenadas[i]} - {arreglo_coordenadas[i + 1]}\n")
                    if len(arreglo_coordenadas[i]) <= 1:
                        fichero_resultados.write("\n\n\n")
                        break
                    arreglo_coordenadas.pop(i)
                    arreglo_coordenadas.pop(i)
                    
            else:
                i += 1
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            
    
    fichero_resultados.close()

def copy_command():
    fichero_quaterniones = open("comandos.txt", "r")
    contenido = fichero_quaterniones.read()
    pyperclip.copy(contenido)

