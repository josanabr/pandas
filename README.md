# Pandas

Un repositorio con los archivos necesarios para crear una imagen de Docker con Python + Flask + Pandas.
Este repositorio depende de la imagen [josanabr/flask](https://hub.docker.com/r/josanabr/flask/).

En este directorio se encuentra el [Dockerfile](Dockerfile) que indica como se construye una imagen de Docker con Pandas desplegado. 
Asi mismo se provee un archivo en Python ([reading_csv.py](reading_csv.py)) que muestra una manipulacion basica de un archivo CSV.

Para ejecutar el archivo debe seguir los siguientes pasos:

* Ejecutar el contenedor

```
docker run --rm -it -v $(pwd):/myhome josanabr/pandas /bin/bash
```

* Valide que en el directorio `/myhome` se encuentra el archivo `reading_csv.py`.

* Para ejectuar este programa ejecute `python3 reading_csv.py`
