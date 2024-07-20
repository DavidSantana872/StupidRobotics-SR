from tkinter import END

def obtener_datos_ficheros():
    fichero = open("coordenadas.txt", "r")
    fichero = fichero.read()
    return fichero

def es_numero(cadena):
    try:
        float(cadena)  # convertir la cadena a un número flotante
        return True
    except ValueError:
        return False
    
def limpiar_arreglo(coordenadas_datos):
    datos = coordenadas_datos
    datos = datos.split("\n")
    lista_datos = [x for x in datos if len(x) >= 2]
    lista_adaptada = []
    
    for coordenada in lista_datos:
        coordenada = coordenada.split(" ")
        # borrar los caracteres innecesarios 
        coordenada = [x for x in coordenada if es_numero(x)]
        lista_adaptada.append(coordenada)
    
    return lista_adaptada

def generar_levantamiento(coordenada1, coordenada2, fichero_comandos):
    fichero_comandos.write("\n\n! Levanamiento\n")
    fichero_comandos.write(f"! X = {coordenada1[0]} Y = {coordenada1[1]} Z = 0\n")
    fichero_comandos.write(f"! X = {coordenada2[0]} Y = {coordenada2[1]} Z = 0\n\n")
    fichero_comandos.write(f"\tMoveL Offs(p10,{coordenada1[0]}*ESC,{coordenada1[1]}*ESC,50), v1000, fine, tool0;\n")
    fichero_comandos.write(f"\tMoveL Offs(p10,{coordenada2[0]}*ESC,{coordenada2[1]}*ESC,50), v1000, fine, tool0;\n")
    fichero_comandos.write(f"\tWaitTime t;\n")
    fichero_comandos.write(f"\tMoveL Offs(p10,{coordenada2[0]}*ESC,{coordenada2[1]}*ESC,0), v1000, fine, tool0;\n")
    fichero_comandos.write("\n\n")

  
    
def generarLinea(coordenadas, fichero_comandos):
    fichero_comandos.write("\n! Linea\n")
    fichero_comandos.write(f"! X = {coordenadas[0]} Y = {coordenadas[1]} Z = 0\n")
    fichero_comandos.write(f"MoveL Offs(p10,{coordenadas[0]}*ESC,{coordenadas[1]}*ESC,0), v1000, fine, tool0;\n")


def generar_circulo(coordenada1, coordenada2, coordenada3, coordenada4, fichero_comandos):
    fichero_comandos.write("\n\n! Circulo\n\n")
    fichero_comandos.write(f"! X = {coordenada1[0]} Y = {coordenada1[1]} Z = 0\n")
    fichero_comandos.write(f"! X = {coordenada2[0]} Y = {coordenada2[1]} Z = 0\n\n")
    fichero_comandos.write(f"\tMoveC Offs(p10,{coordenada1[0]}*ESC,{coordenada1[1]}*ESC,0.0000), Offs(p10,{coordenada2[0]}*ESC,{coordenada2[1]}*ESC,0.0000), v1500, fine, tool0;\n\n")
    fichero_comandos.write(f"! X = {coordenada3[0]} Y = {coordenada3[1]} Z = 0\n\n")
    fichero_comandos.write(f"! X = {coordenada4[0]} Y = {coordenada4[1]} Z = 0\n\n")
    fichero_comandos.write(f"\tMoveC Offs(p10,{coordenada3[0]}*ESC,{coordenada3[1]}*ESC,0.0000), Offs(p10,{coordenada4[0]}*ESC,{coordenada4[1]}*ESC,0.0000), v1500, fine, tool0;\n")
    fichero_comandos.write("\n\n\n")

def generar_semi_circulo(coordenada1, coordenada2, fichero_comandos):
    fichero_comandos.write("! SemiCirculo\n\n")
    fichero_comandos.write(f"! X = {coordenada1[0]} Y = {coordenada1[1]} Z = 0\n")
    fichero_comandos.write(f"! X = {coordenada2[0]} Y = {coordenada2[1]} Z = 0\n\n")
    fichero_comandos.write(f"MoveC Offs(p10,{coordenada1[0]}*ESC,{coordenada1[1]}*ESC,0.0000), Offs(p10,{coordenada2[0]}*ESC,{coordenada2[1]}*ESC,0.0000), v1500, fine, tool0;\n")
    
    
def main(text_area):
    datos_coordenadas = limpiar_arreglo((text_area.get(1.0, END)))
    i = 0 
    fichero_comandos = open("comandos.txt", "w")
    while (i < len(datos_coordenadas)):
        coordenadas = datos_coordenadas[i]
        
        # Levantamiento 
        if (coordenadas[3] == "1"):
            generar_levantamiento(datos_coordenadas[i], datos_coordenadas[i + 1], fichero_comandos)
            i = i + 1

        # Linea
        
        elif (coordenadas[3] == "2"):
            generarLinea(coordenadas, fichero_comandos)
            
        elif(coordenadas[3] == "3"):
            generar_circulo(datos_coordenadas[i], datos_coordenadas[i + 1], datos_coordenadas[i + 2], datos_coordenadas[i + 3], fichero_comandos)
            i = i + 3
        
        elif(coordenadas[3] == "4"):
            generar_semi_circulo(datos_coordenadas[i], datos_coordenadas[i + 1], fichero_comandos)
            i = i + 1   
        i = i + 1
        
