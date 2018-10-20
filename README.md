# Pandas

## Tabla de Contenidos

- [Intro](#intro)
- [Propuesta de *Web Service* a ser desarrollado](#propuesta-de-web-service-a-ser-desarrollado)

---

## Intro
Este es un repositorio con los archivos necesarios para crear una imagen de Docker con Python + Flask + Pandas.
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

---

## Propuesta de *Web Service* a ser desarrollado

Tomando como base el archivo [`reading_csv.py`](reading_csv.py) vamos a construir un nuevo archivo en Python que nos permita exponer ciertas funciones de Pandas como *web services*.

La idea es crear un *web service* que nos permita.

* Instanciar un URL desde el cual se descarga un archivo CSV
* El *web service* podra calcular las siguientes funciones de agregacion: media, la mediana, el minimo, el maximo; de un atributo de un `DataFrame`
* Si se hace la consulta de alguna funcion de agregacion y no hay un `DataFrame` entonces se debe arrojar un error
* El usuario puede solicitar del *web service* lo siguiente:
  * La funcion de agregacion de un atributo del `DataFrame`
  * Aplicacion la agregacion de todos los atributos del `DataFrame`
* Las respuestas deben ser entregadas en formato JSON  

