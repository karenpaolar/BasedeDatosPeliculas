import csv
import pandas as pd

def comillas(cad):
    cad2=''
    for i in range (0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2

#crew
# python3 csv_sql_crew.py > crew.sql
archivo = pd.read_csv('/Users/karenromero/Desktop/Proyecto_SistemasGestoresdeBasesdeDatos/2Preprocesamiento/crew.csv')
archivo=pd.DataFrame(archivo)

print ('INSERT INTO crew (credit_id, id_persona, nombres, trabajo, id_movie) VALUES')
for i in range (0,len(archivo)):

    credit_id=archivo.iloc[i]['credit_id']
    id_persona=archivo.iloc[i]['id_persona']
    nombres=archivo.iloc[i]['nombres']
    nombres=comillas(nombres)
    trabajo=archivo.iloc[i]['trabajo']
    trabajo=comillas(trabajo)
    id_movie=archivo.iloc[i]['id_movie']

    if (i!=len(archivo)-1):
        print('(\'{0}\',{1},\'{2}\',\'{3}\',{4}),'.format(credit_id, id_persona, nombres, trabajo, id_movie))
    else:
        print('(\'{0}\',{1},\'{2}\',\'{3}\',{4});'.format(credit_id, id_persona, nombres, trabajo, id_movie))
