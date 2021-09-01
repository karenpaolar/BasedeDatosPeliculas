import pandas as pd

credits=pd.read_csv("credits.csv")
credits=pd.DataFrame(credits)

n=len(credits)
credits_crew=pd.DataFrame()

datacredit_id=[]
datamovie=[]
dataid=[]
dataname=[]
datajob=[]


for i in range(0,n):
    crew=credits.iloc[i]['crew']
    crew=eval(crew)   
    for j in range(0,len(crew)):
        dato=(crew[j])
        credit_id=dato['credit_id']
        id=dato['id']
        name=dato['name']
        job=dato['job']
        datacredit_id.append(credit_id)
        datajob.append(job)
        dataid.append(id)
        dataname.append(name)
        datamovie.append(credits.iloc[i]['id'])


credits_crew.insert(0,'credit_id',datacredit_id,True)
credits_crew.insert(1,'id_persona',dataid,True)
credits_crew.insert(2,'nombres',dataname,True)
credits_crew.insert(3,'trabajo',datajob,True)
credits_crew.insert(4,'id_movie',datamovie,True)
credits_crew.drop_duplicates(subset=['credit_id'], keep="first", inplace=True)
credits_crew.to_csv("crew.csv", index= False)