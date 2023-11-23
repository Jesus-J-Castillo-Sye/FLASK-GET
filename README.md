# FLASK-GET
Deesarrollo de tres endpoints de forma local

# =================================
REQUISITOS

PYTHON Instalado - version del proyecto (3.12.0)

Editor de codigo - Recomendación de visual estudio

Instalación de flask - dentro de un entorno virtual

# =================================

INICIALIZAR EL PORYECTO

Descargamos el proyecto en la carpeta que nosotros deseamos correr dicho proyecto

Por consola nos dirgimos ah dicha ruta, en donde crearemos un entorno para descargar nuestra paqueteria de FLASK y poder ejecutarlo sin afectar otros proyectos de Python.

El comando para crear el entorno es:


py -3 -m venv .venv


Antes de trabajar en su proyecto, active el entorno correspondiente, con el siguiente comando:


.venv\Scripts\activate


Una vez creado y activado el entorno, se le instalara Flask, con el siguiente comando

pip install Flask


# ============================

EJECUCION DE PROYECTO

Para poder ejecutar el proyecto, despues de hacer los pasos de inicializar, en la consala ejecutamos el sigueinte comando


flask --app appi run

Donde "appi" es el nombre de nuestro proyecto

# ============================

VALIDACION DE PROYECTO

Si el proceso fue correcto, nos arrojara un puerto local para hacer las pruebas de nuestro tres endpoint con metodos GET. Usando los siguientes enlaces

http://127.0.0.1:5000/mat-juridico/estado-procesal/{#numaun}

http://127.0.0.1:5000/mat-juridico/archivo/{#numero}/{#numero}

http://127.0.0.1:5000/mat-juridico/relaciones-recuridas/{#numero}/{#rfc-string}








