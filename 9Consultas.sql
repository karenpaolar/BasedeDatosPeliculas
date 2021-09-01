SELECT genero, COUNT(id_genero) AS pregunta1
FROM genero
GROUP BY genero;

SELECT peliculas.nombrepelicula, genero AS pregunta1
FROM peliculas, genero
WHERE peliculas.id=genero.id;


SELECT actores.nombres, COUNT(id_movie) AS pregunta2
FROM actores 
GROUP BY nombres
ORDER BY pregunta2 DESC LIMIT 1;

SELECT peliculas.nombrepelicula, COUNT(id_persona) AS pregunta3
FROM actores, peliculas
WHERE peliculas.id = actores.id_movie
GROUP BY peliculas.id
ORDER BY pregunta3 DESC LIMIT 1;

SELECT crew.nombres, COUNT(id_persona) AS pregunta4
FROM crew
where trabajo = 'Director'
GROUP BY nombres, trabajo
ORDER BY pregunta4 DESC LIMIT 1;

SELECT DISTINCT peliculas.nombrepelicula AS pregunta5
FROM peliculas, crew, actores
WHERE peliculas.id = crew.id_movie AND crew.trabajo = 'Director' AND crew.id_persona = actores.id_persona;

SELECT peliculas.nombrepelicula AS peregunta6
FROM votos, peliculas
WHERE votos.id=peliculas.id AND promedio_votos = (SELECT MAX(promedio_votos) from votos);

SELECT peliculas.nombrepelicula AS pregunta7
FROM votos, peliculas
WHERE votos.id=peliculas.id AND total_votos = (SELECT MAX(total_votos) from votos);

