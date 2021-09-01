import csv
import pandas as pd

def comillas(cad):
    cad2=''
    for i in range (0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2


#votos 
#python3 csv_sql_votos.py > votos.sql
archivo = pd.read_csv('/Users/karenromero/Desktop/Proyecto_SistemasGestoresdeBasesdeDatos/2Preprocesamiento/votos.csv')
archivo=pd.DataFrame(archivo)

print ('INSERT INTO votos (id, promedio_votos, total_votos) VALUES')
for i in range (0,len(archivo)):

    id=archivo.iloc[i]['id']
    promedio_votos=archivo.iloc[i]['promedio_votos']
    total_votos=archivo.iloc[i]['total_votos']
    

    if (i!=len(archivo)-1):
        print('({0},{1},{2}),'.format(id, promedio_votos, total_votos))
    else:
        print('({0},{1},{2});'.format(id, promedio_votos, total_votos))