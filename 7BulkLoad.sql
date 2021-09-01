\COPY actores(credit_id, id_persona ,nombres ,id_movie) FROM 'actores.csv' DELIMITER ',' CSV HEADER;

\COPY crew(credit_id, id_persona, nombres, trabajo, id_movie) FROM 'crew.csv' DELIMITER ',' CSV HEADER;

\COPY peliculas(id ,nombrepelicula) FROM 'peliculas.csv' DELIMITER ',' CSV HEADER;

\COPY genero(id ,id_genero ,Genero) FROM 'genero.csv' DELIMITER ',' CSV HEADER;

\COPY votos(id ,promedio_votos ,total_votos) FROM 'votos.csv' DELIMITER ',' CSV HEADER;


