import csv
import pandas as pd

def comillas(cad):
    cad2=''
    for i in range (0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2


#peliculas python3 csv_sql_genero.py > genero.sql
archivo = pd.read_csv('/Users/karenromero/Desktop/Proyecto_SistemasGestoresdeBasesdeDatos/2Preprocesamiento/genero.csv')
archivo=pd.DataFrame(archivo)

print ('INSERT INTO genero (id, id_genero, Genero) VALUES')
for i in range (0,len(archivo)):

    id=archivo.iloc[i]['id']
    id_genero=archivo.iloc[i]['id_genero']
    Genero=archivo.iloc[i]['Genero']
    

    if (i!=len(archivo)-1):
        print('({0},{1},\'{2}\'),'.format(id, id_genero, Genero))
    else:
        print('({0},{1},\'{2}\');'.format(id, id_genero, Genero))