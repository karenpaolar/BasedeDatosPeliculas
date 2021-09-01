import pandas as pd

credits=pd.read_csv("credits.csv")
credits=pd.DataFrame(credits)

n=len(credits)
credits_cast=pd.DataFrame()

credit_id=[]
id_persona=[]
nombre=[]
id_movie=[]

for i in range(0,n):
    cast=credits.iloc[i]['cast']
    cast=eval(cast)   
    for j in range(0,len(cast)):
        dato=(cast[j])
        credit= dato['credit_id']
        persona=dato['id']
        nombre1=dato['name']
        credit_id.append(credit)
        id_persona.append(persona)
        nombre.append(nombre1)
        id_movie.append(credits.iloc[i]['id'])


credits_cast.insert(0,'credit_id',credit_id,True)
credits_cast.insert(1,'id_persona',id_persona,True)
credits_cast.insert(2,'nombres',nombre,True)
credits_cast.insert(3,'id_movie',id_movie,True)

credits_cast.drop_duplicates(subset=['credit_id'], keep="first", inplace=True)
credits_cast.to_csv("actores.csv", index= False)