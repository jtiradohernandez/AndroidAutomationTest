# Metropolis:Lab Technical Test

Ejercicio UI Automation

## Setup en Windows

- Es necesario tener instalados los siguientes programas:
    - Android Studio + AVD
    - Appium
    - Python
    - Behave

- En Android Studio AVD creamos y configuramos el dispositivo virtual que vamos a utilizar.

- Accedemos al archivo environment.py y escribimos la versión del Sistema Operativo del Dispositivo Virtual creado.


## Ejecución de los Tests Cases

Una vez tenemos todo preparado, realizamos los siguientes pasos:

1. Ejecutamos Appium

2. Ejecutamos el Dispositivo Virtual Android

3. Abrimos una consola de comandos, nos colocarnos en la raiz de este proyecto y lanzamos el siguiente comando:

Behave webChrome.feature

Automaticamente se pasará el Test Case dando un resultado final.
