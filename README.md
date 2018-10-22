# Pandas

## Tabla de Contenidos

- [Intro](#intro)
- [Propuesta de *Web Service* a ser desarrollado](#propuesta-de-web-service-a-ser-desarrollado)
- [Desarrollo del *Web Service*](#desarrollo-del-web-service)

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

---

## Desarrollo del *Web Service*

A continuacion se describe como llevar a cabo la implementacion del *web service* a partir de los requerimientos indicados anteriormente.
Inicialmente se establece que el URI sera `/pandas/aggr/v1.0`. 
Dicho esto, todos los URLs se construiran de la forma `http://<host>:<port>/pandas/aggr/v1.0`.
Donde `<host>` y `<port>` para efectos de las pruebas sera `localhost` y `5000`, respectivamente.

Ahora, se establece que el archivo donde residira nuestro *web service* sera llamado `pandas_ws.py`. 
A continuacion se colocara la siguiente informacion en este archivo..

## Comandos docker a ejecutar

```
docker run --rm -it -v $(pwd):/myhome -p 5000:5000 josanabr/pandas /bin/bash
```

## Comandos curl a ejecutar


```
curl -i -H "Content-Type: application/json" -X POST -d '{"URL": "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"}' http://localhost:5000/pandas/aggr/v1.0
```

```
curl -i -H "Content-Type: application/json" -X POST -d '{"Agregado": "mean", "Campo": "2"}' http://localhost:5000/pandas/aggr/v1.0/agregado
```
