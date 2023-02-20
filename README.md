## PROYECTO INDIVIDUAL - Machine Learning Operations
BY: Gian Pier, Pacheco Mateo (Altezier)

> En este apartado describire un poco el proyecto y los files.

-[Video de documentacion](https://www.youtube.com/watch?v=6n7mPyiAe_4)
-[App en DetaSpace](https://deta.space/discovery/r/ikofw6nssp26cq6k)
-[deta_sets]:(https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn)

### **Temática**

Se empezo a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

Vas a sus datos y te das cuenta que la madurez de los mismos es poca : Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas…. haciendo tu trabajo imposible .

Como segunda parte del requerimiento, se solicitaba elaborar una API a efectos de disponibilizar los datos de manera online, los cuales debían ser accedidos mediante cinco consultas predefinidas.

### **Detalles del requerimiento**
 **Transformaciones:**
 

Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

De haber fechas, deberán tener el formato AAAA-mm-dd

Los campos de texto deberán estar en minúsculas, sin excepciones

El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

### **Consultas API:** 

Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


:red_circle: **MENU:** :red_circle:
* **datasets/** - datasets que utilice en el proyecto.
* **moviescores.csv** - el csv que se utiliza para las consultas.
* **pycache** - carpeta cache de las compilaciones.
* **querys** - notebook con las funciones del API probadas en local.
* **ETL** - Exportación, transformación y carga precio del EDA y query's.
* **EDA** - Análisis exploratorio de los datos.
* **MLOPs** - Desarrollo del modelo predictivo.(considerar el tamaño del dataframe)
* **README** - Pequeña descripción o intro del proyecto en cuestión.

* **FastAPI/** - Carpeta contenedora de todo lo relacionado a la API.
* **main.py** - el código correspondiente al api con las funciones respectivas.
* **spacefile** - pequeño archivo para configurar detalles sobre la api ( configurado previo de subirla). 
* **icon.png** - imagen que se agregara dataspace al subir la api. 
* **requirements.txt** - librerias que se van descargar al subir la api para cargarla en deta.space.
 
:red_circle: **Las funciones que componen la API son:** :red_circle:

* Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.. <br>
* Cantidad de películas por PLATAFORMA con un puntaje mayor a XX en determinado AÑO. <br>
* Cantidad de películas por plataforma con filtro de PLATAFORMA.. <br>
* Actor que más se repite según plataforma y año. <br>

:warning: **Sintaxis a tener en cuenta al escribir una consulta:** :warning:<br>
* Todo debe estar escrito en minúsculas.  <br>
* Las plataformas que admite son: amazon, disney, hulu y netflix. <br>
*  En caso de la query no arroje resultados, un mensaje explicativo se imprimirá en pantalla.<br>

### **Herramientas utilizadas**
-   **[Python](https://www.python.org/)**: lenguaje de programación utilizado, que brinda acceso a librerías apropiadas para realizar la tarea encomendada de manera eficaz y eficiente.
-   **[Pandas](https://pandas.pydata.org/):** librería que nos permite el acceso a los archivos csv provistos, su conversión en dataframes, la transformación de los datos y la posterior exportación de los mismos en un único archivo, el cual luego será utilizado por la API para disponibilizar los datos.
-   **[Pandasql](https://pypi.org/project/pandasql/):** librería que nos permite efectuar consultas con lenguaje SQL sobre Dataframes de Pandas.
-   **[scikit-learn](https://scikit-learn.org/stable/index.html):**  libreria de python para el desarrollo de machine learning .
-   **[FastApi](https://fastapi.tiangolo.com/):** framework para la construcción de la API en Python.
-   **[Uvicorn](https://www.uvicorn.org/):** nos permite efectuar pruebas para controlar el funciomaniento de la API de manera local previa a su despliegue en Deta.
-   **[DetaSpace](https://deta.space):**  evolucion de lo que anter era Deta, igualmente es una plataforma online y gratuita, que nos permite disponibilizar tanto la API como los datos para que puedan ser consultados por el usuario mediante su software.
