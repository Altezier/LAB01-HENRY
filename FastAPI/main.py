from fastapi import FastAPI
from fastapi import Query
import pandas as pd
import duckdb as dk


app = FastAPI()
# Enlace del propio GitHub para importar el csv
#!https://github.com/Altezier/LAB01-HENRY/blob/main/datasets/moviescores.csv?raw=true 

@app.get("/")
def presentación():
    return "PROYECTO INDIVIDUAL 01 - Pacheco, Gian Pier"


# 1.Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

@app.get("/get_max_duration/")
def get_max_duration(year: int = Query(None),durtype: str = Query(None), platform: str = Query(None)):
    #Lectura de la base de datos localmente alojada en datasets:
    df = pd.read_csv("https://github.com/Altezier/LAB01-HENRY/blob/main/datasets/moviescores.csv?raw=true",sep=';')
    #Transformación de plataformas ingresadas para que lo pueda leer la consulta:
    df['duration_int']=df['duration_int'].astype('int64')

    #Defino las plataformas
    if platform == "amazon":
        plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    elif platform == None: #Aquí le agregue None para que se guarde en la variable.
        plat = None
    else :
        return ("No hay existencias de esa plataforma. Las opciones de plataforma son: amazon, disney, hulu, netflix. En minúsculas respectivamente") #Mensaje de error si es que no se ingreso la plataforma correctamente.

    if durtype == "season" or durtype == "seasons":
        durtype = "seasons"
    elif durtype =="m" or durtype =="min" :
        durtype = "min"    
    elif durtype != None : # Descarto cualquier otro valor que no pudiera ser los previos indicados inclusive el vacio.
         return ("No hay existencias de ese tipo de duración, Las alternativas son: seasons y min. En minúsculas respectivamente.")
    
    #Aquí añado todas las queys opcionales que se va a ir ejecutando según se vean valores faltantes.
    #QUERYS:
    if  not year and plat == None and not durtype:
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df ORDER BY duration_int DESC LIMIT 1").df()
    elif not year and plat == None:
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE duration_type='{durtype}' ORDER BY duration_int DESC LIMIT 1").df()
    elif not year and not durtype:
        result= dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE id like '{plat}' ORDER BY duration_int DESC LIMIT 1").df()
    elif plat == None and not durtype:
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE release_year='{year}' ORDER BY duration_int DESC LIMIT 1").df()
    elif not year :
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE id like '{plat}' and duration_type='{durtype}' ORDER BY duration_int DESC LIMIT 1").df()
    elif plat == None:
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE release_year='{year}' and duration_type='{durtype}' ORDER BY duration_int DESC LIMIT 1").df()
    elif not durtype:
        result=dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE id like '{plat}' and release_year='{year}' ORDER BY duration_int DESC LIMIT 1").df()
    else:
        result = dk.query(f"SELECT title, release_year, duration_int, duration_type FROM df WHERE id like '{plat}' and release_year='{year}' and duration_type='{durtype}' ORDER BY duration_int DESC LIMIT 1").df()
    
    #Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #Se retornan los datos como diccionario.
    
    #Si la variable no tiene contenido:
    else:
        return ("No hay películas en dicha plataforma, en ese año y con el tipo de duration indicado.")
    
#2.Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

@app.get("/get_score_count/")   
def get_score_count(platform: str, score: float, year: int):
    #Lectura de la base de datos:
    df = pd.read_csv("https://github.com/Altezier/LAB01-HENRY/blob/main/datasets/moviescores.csv?raw=true", sep=';')
    
    #Defino las plataformas:
    if platform == "amazon":
        plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. En minúsculas respectivamente")
    #QUERY:
    result = dk.query(f"SELECT COUNT(title) FROM df WHERE id LIKE '{plat}' AND type == 'movie' AND score > {score} AND release_year == {year}").df() 
    #Se verifica el contenido de la variable "result". En caso de no estar vacío:
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No hay películas registradas en esa plataforma, con ese puntaje en el año indicado.")

# 3.Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))
   
@app.get("/get_count_platform/")  
def get_count_platform(platform: str):
    #Lectura de la base de datos:
    df = pd.read_csv("https://github.com/Altezier/LAB01-HENRY/blob/main/datasets/moviescores.csv?raw=true", sep=';')
    
    #Defino las plataformas:
    if platform == "amazon":
        plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. En minúsculas, respectivamente.")
    result = dk.query(f"SELECT COUNT(title) FROM df WHERE id LIKE '{plat}' AND type == 'movie'").df()

    return result.to_dict() 

# 4. Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))
@app.get("/get_actor/")  
def get_actor(platform: str, year: int):
    #Lectura de la base de datos:
    df = pd.read_csv("https://github.com/Altezier/LAB01-HENRY/blob/main/datasets/moviescores.csv?raw=true", sep=';')
    
    #Separo los actores apilándolos en una serie con el id.
    cast_s = df[df['cast'] != 'Sin registro']['cast'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)

    #Junto la columna 'actor' con el dataframe primario.
    cast_df=df.merge(cast_s.rename('actor'), left_index=True, right_index=True).reset_index(drop=True).drop(columns=['cast'])
    cast_df
    
    #Defino las plataformas:
    if platform == "amazon":
        plat = "a%"
    elif platform == "disney":
        plat = "d%"
    elif platform == "hulu":
        plat = "h%"
    elif platform == "netflix":
        plat = "n%"
    else:
        return ("Plataforma incorrecta. Las opciones son: amazon, disney, hulu, netflix. En minúsculas, respectivamente.")
    
    # QUERY
    result = dk.query(f"""SELECT actor ,count(*) as apparitions FROM cast_df WHERE id LIKE '{plat}' AND release_year='{year}' GROUP BY "actor" ORDER BY apparitions DESC LIMIT 1""").df()
    
    if not result.iloc[0,0] == 0:
        return result.to_dict() #retorna los datos solicitados en la consulta, como un diccionario.
    #Si la variable no tiene contenido:
    else:
        return ("No hay un actor registrado, en esa plataforma con el año indicado.")   