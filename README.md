## PROYECTO INDIVIDUAL - Machine Learning Operations
BY: Gian Pier, Pacheco Mateo

> En este apartado describire un poco el proyecto y los files.

[Video de documentacion]()

:red_circle: **MENU:** :red_circle:
* **datasets/** - datasets que utilice en el proyecto.
* **moviescores.csv** - el csv que se utiliza para las consultas.
* **pycache** - carpeta cache de las compilaciones.
* **querys** - notebook con las funciones del API probadas en local.
* **ETL** - Exportación, transformación y carga precio del EDA y query's.
* **EDA** - Análisis exploratorio de los datos.
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
