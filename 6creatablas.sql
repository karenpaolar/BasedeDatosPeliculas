CREATE DATABASE bdpeliculas;
\c bdpeliculas;

CREATE TABLE actores (
	credit_id CHAR(100) PRIMARY KEY,
	id_persona REAL,
	nombres CHAR(50),
	id_movie INT
	);
	
CREATE TABLE crew(
	credit_id CHAR(100) PRIMARY KEY,
	id_persona REAL,
    nombres CHAR(50),
    trabajo CHAR(100),
	id_movie INT
	);

CREATE TABLE genero(
	id INT PRIMARY KEY,
	id_genero REAL,
    genero CHAR(20)
    );

CREATE TABLE peliculas(
	id INT PRIMARY KEY,
    nombrepelicula CHAR(200)
    );

CREATE TABLE votos(
	id INT PRIMARY KEY,
    promedio_votos REAL,
    total_votos INT
    );

