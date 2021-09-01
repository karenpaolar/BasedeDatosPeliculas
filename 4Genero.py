import csv
import pandas as pd

movies=pd.read_csv("movies_metadata.csv")
movies=movies.drop_duplicates()
movies=pd.DataFrame(movies)


n=len(movies)
nulos='NULL'
movies_generes=pd.DataFrame()
dataid=[]
datanames=[]
datamovie=[]
#datanombrepeli=[]
for i in range(0,n):
    genres=movies.iloc[i]['genres']
    genres=eval(genres)   
    if len(genres)==0:
        dataid.append(nulos)
        datanames.append(nulos)
        datamovie.append(movies.iloc[i]['id'])
        #datanombrepeli.append(movies.iloc[i]['original_title'])
    else:
        for j in range(0,len(genres)):
            dato=(genres[j])
            name=dato['name']
            id=dato['id']
            datanames.append(name)
            dataid.append(id)
            datamovie.append(movies.iloc[i]['id'])
            #datanombrepeli.append(movies.iloc[i]['original_title'])

movies_generes.insert(0,'id',datamovie,True)
#movies_generes.insert(1,'nombrepelicula',datanombrepeli,True)
movies_generes.insert(1,'id_genero',dataid,True)
movies_generes.insert(2,'Genero',datanames,True)
movies_generes.drop_duplicates(subset=['id'], keep="first", inplace=True)
movies_generes.dropna(subset=['id_genero' ,'Genero'],inplace=True)
movies_generes.to_csv("genero.csv", index= False)

