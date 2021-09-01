import csv
import pandas as pd

def comillas(cad):
    cad2=''
    for i in range (0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2

#actores 
# python3 csv_sql_actores.py > actores.sql
archivo = pd.read_csv('/Users/karenromero/Desktop/Proyecto_SistemasGestoresdeBasesdeDatos/2Preprocesamiento/actores.csv')
archivo=pd.DataFrame(archivo)

print ('INSERT INTO actores (credit_id, id_persona ,nombres ,id_movie) VALUES')
for i in range (0,len(archivo)):

    credit_id=archivo.iloc[i]['credit_id']
    id_persona=archivo.iloc[i]['id_persona']
    nombres=archivo.iloc[i]['nombres']
    nombres=comillas(nombres)
    id_movie=archivo.iloc[i]['id_movie']

    if (i!=len(archivo)-1):
        print('(\'{0}\',{1},\'{2}\',{3}),'.format(credit_id, id_persona, nombres, id_movie))
    else:
        print('(\'{0}\',{1},\'{2}\',{3});'.format(credit_id, id_persona, nombres, id_movie ))
