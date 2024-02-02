CREATE DATABASE if not exists info_pessoas;
USE info_pessoas;
CREATE TABLE if not exists pessoas(
    id int auto_increment primary key,
    nome varchar(100) not null,
    idade int not null,
    genero char(1) not null,
    nacionalidade varchar(100) not null,
    email varchar(100) not null unique,
    estado_civil varchar(50) not null,
    nome_do_pai varchar(100) not null,
    nome_da_mae varchar(100) not null
);
INSERT INTO pessoas(nome, idade, genero, nacionalidade, email, estado_civil, nome_do_pai, nome_da_mae) VALUES 
	("Pedro Silva", 18, "M", "Brasileiro", "pedrosilva@gmail.com", "Solteiro", "Pai do Pedro", "Mãe do Pedro"),
    ("Maria Souza", 30, "F", "Brasileira", "mariasouza@gmail.com", "Casada", "Pai da Maria", "Mãe da Maria"),
    ("Henrique Braga", 35, "M", "Brasileiro", "henriquebraga@gmail.com", "Divorciado", "Pai do Henrique", "Mãe do Henrique");
UPDATE pessoas
SET email = "maria30@gmail.com", estado_civil = "Divorciada"
WHERE id = 2;
DELETE from pessoas WHERE id = 1;
