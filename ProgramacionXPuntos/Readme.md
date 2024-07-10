# Stupid Robotic

## Descripción del Proyecto

**Stupid Robotic** es una herramienta diseñada para automatizar la generación de quaterniones y comandos de movimiento en RoboStudio a partir de coordenadas extraídas manualmente desde AutoCAD. Este proyecto acelera el proceso repetitivo y tedioso de programación en RoboStudio, permitiendo generar automáticamente los quaterniones necesarios y los comandos `MoveL` y `MoveC` según los parámetros de entrada.

## Características

- **Automatización de Procesos en RoboStudio**: Genera automáticamente quaterniones y comandos de movimiento a partir de coordenadas ingresadas manualmente.
- **Soporte para Diferentes Tipos de Movimientos**: Genera comandos `MoveL` y `MoveC` según los parámetros especificados.

## Parámetros de Entrada

El programa acepta los siguientes parámetros de entrada en el formato `x = valor y = valor z = valor tipo`:

- **x**: Coordenada X.
- **y**: Coordenada Y.
- **z**: Coordenada Z.
- **Tipo de Generación** (último parámetro):
  - `1`: Genera variables de levantamiento (`P#` y `PL#`).
  - `2`: Genera una sola variable (`P#`).
  - `3`: Genera comandos `MoveC` para un círculo:
    - El primer `MoveC` va desde el punto actual hasta la primera coordenada ingresada después del `3`.
    - El segundo `MoveC` va desde la coordenada que posee el parametro `3` hasta la segunda coordenada ingresada, y se cierra el círculo usando la coordenada anterior a la que tiene el parametro `3`.
  - `4`: Genera un semi-círculo con un comando `MoveC`, la siguiente coordenada insertada despues de esta la tomara como el punto de finalizacion del semi-circulo.

## Uso

Para utilizar Stupid Robotic, ingrese las coordenadas manualmente desde AutoCAD y luego los parámetros de entrada en el formato especificado. 

**Entrada  →** `x = 10` `y = 35` `z = 0` `1`

....continuará 
