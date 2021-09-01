import csv
import pandas as pd

def comillas(cad):
    cad2=''
    for i in range (0,len(cad)):
        cad2+=cad[i]
        if(cad[i]=="\'"):
            cad2+="\'"
    return cad2


#peliculas 
# python3 csv_sql_peliculas.py > peliculas.sql
archivo = pd.read_csv('/Users/karenromero/Desktop/Proyecto_SistemasGestoresdeBasesdeDatos/2Preprocesamiento/peliculas.csv')
archivo=pd.DataFrame(archivo)

print ('INSERT INTO peliculas (id ,nombrepelicula) VALUES')
for i in range (0,len(archivo)):

    id=archivo.iloc[i]['id']
    nombrepelicula=archivo.iloc[i]['nombrepelicula']
    nombrepelicula=comillas(nombrepelicula)

    if (i!=len(archivo)-1):
        print('({0},\'{1}\'),'.format(id, nombrepelicula))
    else:
        print('({0},\'{1}\');'.format(id,nombrepelicula))