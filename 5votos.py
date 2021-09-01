import csv
import pandas as pd

movies=pd.read_csv("movies_metadata.csv")
movies=movies.drop_duplicates()
movies=pd.DataFrame(movies)

n=len(movies)
nulos='NULL'
movies_votos=pd.DataFrame()

datamovie=[]
datavote_average=[]
datavote_count=[]

for i in range(0,n):
      
    datamovie.append(movies.iloc[i]['id'])
    datavote_average.append(movies.iloc[i]['vote_average'])
    datavote_count.append(movies.iloc[i]['vote_count'])


movies_votos.insert(0,'id',datamovie,True)
movies_votos.insert(1,'promedio_votos',datavote_average,True)
movies_votos.insert(2,'total_votos',datavote_count,True)
movies_votos.drop_duplicates(subset=['id'], keep="first", inplace=True)
movies_votos.to_csv("votos.csv", index= False)

