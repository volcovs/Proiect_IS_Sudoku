DROP DATABASE IF EXISTS sudoku;
CREATE DATABASE sudoku;
use sudoku;

CREATE TABLE IF NOT EXISTS game (
	id INT NOT NULL AUTO_INCREMENT primary key,
    difficulty VARCHAR(30),
    row1 VARCHAR(9),
    row2 VARCHAR(9),
    row3 VARCHAR(9),
    row4 VARCHAR(9),
    row5 VARCHAR(9),
    row6 VARCHAR(9),
    row7 VARCHAR(9),
    row8 VARCHAR(9),
    row9 VARCHAR(9));
    
    INSERT INTO game(difficulty, row1, row2, row3, row4, row5, row6, row7, row8, row9) VALUES
				("easy", "340970000", "109000040", "000001005", "070000650", "906587420", "253094180", "002150004", "000069072", "030000090");
                
CREATE TABLE IF NOT EXISTS solution (
	id INT NOT NULL AUTO_INCREMENT primary key,
    id_game INT NOT NULL,
    difficulty VARCHAR(30),
    row1 VARCHAR(9),
    row2 VARCHAR(9),
    row3 VARCHAR(9),
    row4 VARCHAR(9),
    row5 VARCHAR(9),
    row6 VARCHAR(9),
    row7 VARCHAR(9),
    row8 VARCHAR(9),
    row9 VARCHAR(9),
    
    FOREIGN KEY (id_game) REFERENCES game(id));
    
    INSERT INTO solution(id_game, difficulty, row1, row2, row3, row4, row5, row6, row7, row8, row9) VALUES
				(1, "easy", "345976218", "129835746", "867241935", "478312659", "916587423", "253694187", "792153864", "581469372", "634728591");