def create_cuaternion(coordenadas, ArchivoNuevoCoordenadas, VALOR_INICIO_PUNTO, FicheroComandosFormas, SaltosDePuntos, whois_function):
    for ElementoFormateoQuaternion in coordenadas:
        if (len(ElementoFormateoQuaternion) > 0):

            comentario_coordenadas_quaternion = f"\n! X = {ElementoFormateoQuaternion[0]} Y = { ElementoFormateoQuaternion[1]} Z = {ElementoFormateoQuaternion[2]}\n"
              
            QUATERNION = f"CONST robtarget P{VALOR_INICIO_PUNTO}:=[[{ElementoFormateoQuaternion[0] + 450},{ElementoFormateoQuaternion[1] + 0},400],[4.14816E-8,6.1133E-9,-1,-2.53589E-16],[0,0,-1,0],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]];\n"
            ArchivoNuevoCoordenadas.writelines(comentario_coordenadas_quaternion)
            ArchivoNuevoCoordenadas.writelines(QUATERNION)
            
            # Generacion de punto de levantamiento en caso de tener un levantamiento

            if(len(ElementoFormateoQuaternion) >= 4 and ElementoFormateoQuaternion[3] == 1):
                # Comentario generado para el fichero
                comentario_coordenadas_fichero = f"\n\n!Levantamiento X = {ElementoFormateoQuaternion[0]} Y = { ElementoFormateoQuaternion[1]}Z = {ElementoFormateoQuaternion[2]}\n"
                

                QuaternionLevantamiento = f"CONST robtarget PL{VALOR_INICIO_PUNTO}:=[[{ElementoFormateoQuaternion[0] + 450},{ElementoFormateoQuaternion[1] + 0},450],[4.14816E-8,6.1133E-9,-1,-2.53589E-16],[0,0,-1,0],[9E+9,9E+9,9E+9,9E+9,9E+9,9E+9]];\n\n\n"


                ArchivoNuevoCoordenadas.writelines(comentario_coordenadas_fichero)
                ArchivoNuevoCoordenadas.writelines(QuaternionLevantamiento)

                # Generate comandos levantamiento 

                generate_comandos_levantamientos(VALOR_INICIO_PUNTO, FicheroComandosFormas, SaltosDePuntos)

            elif(len(ElementoFormateoQuaternion) >= 4 and ElementoFormateoQuaternion[3] == 2):
                create_moveL(VALOR_INICIO_PUNTO, FicheroComandosFormas, SaltosDePuntos)

            elif(len(ElementoFormateoQuaternion) >= 4 and ElementoFormateoQuaternion[3] == 3):
                create_circulo(VALOR_INICIO_PUNTO, FicheroComandosFormas, SaltosDePuntos)
            
            elif(len(ElementoFormateoQuaternion) >= 4 and ElementoFormateoQuaternion[3] == 4):
                create_semi_circulo(VALOR_INICIO_PUNTO, FicheroComandosFormas, SaltosDePuntos)
            

            VALOR_INICIO_PUNTO =  VALOR_INICIO_PUNTO + SaltosDePuntos
    if whois_function == "PermitirModificarUltimoPunto":
        #puntoFinal = open("puntodeinicio.txt", "w")
        #contenido_siguiente_punto = str(VALOR_INICIO_PUNTO)
        #puntoFinal.writelines(contenido_siguiente_punto)
        pass

def generate_comandos_levantamientos(PuntoVariable, FicheroComandosFormas, SaltosDePuntos):
    # subo
    subir = f"MoveL PL{PuntoVariable - 10}, v1000, fine, tool0;\n"
    # desplazo 
    desplazo = f"MoveL PL{PuntoVariable}, v1000, fine, tool0;\n"
    # bajo
    bajo = f"MoveL P{PuntoVariable}, v1000, fine, tool0;\n\n"

    # escribir comandos 
    comentario = "\n\n! Levantamiento\n"

    FicheroComandosFormas.writelines(comentario)
    FicheroComandosFormas.writelines(subir)
    FicheroComandosFormas.writelines(desplazo)
    FicheroComandosFormas.writelines(bajo)



def create_moveL(PuntoVariable, FicheroComandosFormas, SaltosDePuntos):
    #   MoveL P10, v1000, fine, tool0;


    linea = f"\nMoveL P{PuntoVariable}, v1000, fine, tool0;\n"
    
    FicheroComandosFormas.writelines(linea)

def create_semi_circulo(PuntoVariable, FicheroComandosFormas, SaltosDePuntos):

    # escribir comentario 
    comentario = "\n\n! Semi circulo\n"

   
    semi_circulo = f"MoveC P{PuntoVariable}, P{PuntoVariable + SaltosDePuntos}, v2000, fine, tool0;\n\n"
    
    FicheroComandosFormas.writelines(comentario)
    FicheroComandosFormas.writelines(semi_circulo)

def create_circulo(PuntoVariable, FicheroComandosFormas, SaltosDePuntos):

# PuntoVariable - (4 * SaltosDePuntos)
# PuntoVariable - (SaltosDePuntos * 3)
    cuarto1_circulo = f"MoveC P{PuntoVariable}, P{PuntoVariable + (SaltosDePuntos)}, v2000, fine, tool0;\n"
    
    cuarto2_circulo = f"MoveC P{PuntoVariable + (SaltosDePuntos * 2)}, P{PuntoVariable - (SaltosDePuntos)}, v2000, fine, tool0;\n\n"
     # escribir comentario 
    comentario = "\n\n! Circulo\n"

    FicheroComandosFormas.writelines(comentario)
    FicheroComandosFormas.writelines(cuarto1_circulo)
    FicheroComandosFormas.writelines(cuarto2_circulo)