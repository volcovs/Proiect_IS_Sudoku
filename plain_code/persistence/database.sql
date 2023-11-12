DROP DATABASE IF EXISTS sudoku;
CREATE DATABASE sudoku;
use sudoku;

CREATE TABLE IF NOT EXISTS game (
	id INT NOT NULL AUTO_INCREMENT primary key,
    difficulty VARCHAR(30),
    row1 VARCHAR(18),
    row2 VARCHAR(18),
    row3 VARCHAR(18),
    row4 VARCHAR(18),
    row5 VARCHAR(18),
    row6 VARCHAR(18),
    row7 VARCHAR(18),
    row8 VARCHAR(18),
    row9 VARCHAR(18));
    
    INSERT INTO game(difficulty, row1, row2, row3, row4, row5, row6, row7, row8, row9) VALUES
				("easy", "3,4,0,9,7,0,0,0,0", "1,0,9,0,0,0,0,4,0", "0,0,0,0,0,1,0,0,5", "0,7,0,0,0,0,6,5,0",
                "9,0,6,5,8,7,4,2,0", "2,5,3,0,9,4,1,8,0", "0,0,2,1,5,0,0,0,4", "0,0,0,0,6,9,0,7,2", "0,3,0,0,0,0,0,9,0");
                
CREATE TABLE IF NOT EXISTS solution (
	id INT NOT NULL AUTO_INCREMENT primary key,
    id_game INT NOT NULL,
    difficulty VARCHAR(30),
    row1 VARCHAR(18),
    row2 VARCHAR(18),
    row3 VARCHAR(18),
    row4 VARCHAR(18),
    row5 VARCHAR(18),
    row6 VARCHAR(18),
    row7 VARCHAR(18),
    row8 VARCHAR(18),
    row9 VARCHAR(18),
    
    FOREIGN KEY (id_game) REFERENCES game(id));
    
    INSERT INTO solution(id_game, difficulty, row1, row2, row3, row4, row5, row6, row7, row8, row9) VALUES
				(1, "easy", "3,4,5,9,7,6,2,1,8", "1,2,9,8,3,5,7,4,6", "8,6,7,2,4,1,9,3,5", "4,7,8,3,1,2,6,5,9", 
                "9,1,6,5,8,7,4,2,3", "2,5,3,6,9,4,1,8,7", "7,9,2,1,5,3,8,6,4", "5,8,1,4,6,9,3,7,2", "6,3,4,7,2,8,5,9,1");