import csv
import pandas as pd

movies=pd.read_csv("movies_metadata.csv")
movies=pd.DataFrame(movies)

n=len(movies)
movies_name=pd.DataFrame()

datamovie=[]
datanombrepeli=[]

for i in range(0,n):
      
    datamovie.append(movies.iloc[i]['id'])
    datanombrepeli.append(movies.iloc[i]['original_title'])


movies_name.insert(0,'id',datamovie,True)
movies_name.insert(1,'nombrepelicula',datanombrepeli,True)
movies_name.drop_duplicates(subset=['id'], keep="first", inplace=True)
movies_name.to_csv("peliculas.csv", index= False)

