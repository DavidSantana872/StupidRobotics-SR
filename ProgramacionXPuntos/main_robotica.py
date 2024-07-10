from CreateQuaternions import create_cuaternion
# Generate saltos
# Input x = 0, y = 0, z = 0, 1
# Ultimo parametro define que es un levaantamiento
# 1 = Genera una variable PL de levantamiento con sus moveL
# 2 = Genera un MoveL con el valor de el
# 3 = Genera un Circulo con el valor de VALOR_INICIO_PUNTO y genera un segundo moveL que cierra el circulo
# 4 = Genera un SemiCirculo con el valor inicial y su valor final

def main(whois_function):
    # desde que punto quieres iniciar
    VALOR_INICIO_PUNTO = open("puntodeinicio.txt", "r")
    VALOR_INICIO_PUNTO = int(VALOR_INICIO_PUNTO.read())
    SALTOS_DE_PUNTOS = 10 
    def es_numero(cadena):
        try:
            float(cadena)  # convertir la cadena a un número flotante
            return True
        except ValueError:
            return False
        
    coordenadas = open("Puntos.txt", "r")
    ArchivoNuevoCoordenadas = open("Quaterniones.txt", "w")
    FicheroComandosFormas = open("ComandosMain.txt", "w")



    coordenadas = (coordenadas.read()).split('\n')
    i = 0
    for coordenada in coordenadas:
        coordenadas[i] = coordenada.split(" ")
        coordenadas[i] = [elemento for elemento in coordenadas[i] if es_numero(elemento)]
        coordenadas[i] = [float(numero) for numero in coordenadas[i]]
        print(coordenadas[i])
        i = i + 1

    # Generar cuaternion mas comentario de las coordenadas y dentro generacion de comandos
    create_cuaternion(coordenadas, ArchivoNuevoCoordenadas, VALOR_INICIO_PUNTO, FicheroComandosFormas, SALTOS_DE_PUNTOS, whois_function)


    ArchivoNuevoCoordenadas.close()
    FicheroComandosFormas.close()
 

