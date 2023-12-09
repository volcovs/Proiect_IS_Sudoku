DROP DATABASE IF EXISTS sudoku;
CREATE DATABASE sudoku;
use sudoku;

CREATE TABLE IF NOT EXISTS game (
	id INT NOT NULL AUTO_INCREMENT primary key,
    difficulty VARCHAR(30),
    col1 VARCHAR(18),
    col2 VARCHAR(18),
    col3 VARCHAR(18),
    col4 VARCHAR(18),
    col5 VARCHAR(18),
    col6 VARCHAR(18),
    col7 VARCHAR(18),
    col8 VARCHAR(18),
    col9 VARCHAR(18));
    
    INSERT INTO game(difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9) VALUES
				("easy", "3,1,0,0,9,2,0,0,0", "4,0,0,7,0,5,0,0,3", "0,9,0,0,6,3,2,0,0", "9,0,0,0,5,0,1,0,0",
                "7,0,0,0,8,9,5,6,0", "0,0,1,0,7,4,0,9,0", "0,0,0,6,4,1,0,0,0", "0,4,0,5,2,8,0,7,9", "0,0,5,0,0,0,4,2,0");
                
CREATE TABLE IF NOT EXISTS solution (
	id INT NOT NULL AUTO_INCREMENT primary key,
    id_game INT NOT NULL,
    difficulty VARCHAR(30),
    col1 VARCHAR(18),
    col2 VARCHAR(18),
    col3 VARCHAR(18),
    col4 VARCHAR(18),
    col5 VARCHAR(18),
    col6 VARCHAR(18),
    col7 VARCHAR(18),
    col8 VARCHAR(18),
    col9 VARCHAR(18));
    
    INSERT INTO solution(id_game, difficulty, col1, col2, col3, col4, col5, col6, col7, col8, col9) VALUES
				(1, "easy", "3,1,8,4,9,2,7,5,6", "4,2,6,7,1,5,9,8,3", "5,9,7,8,6,3,2,1,4", "9,8,2,3,5,6,1,4,7", 
                "7,3,4,1,8,9,5,6,2", "6,5,1,2,7,4,3,9,8", "2,7,9,6,4,1,8,3,5", "1,4,3,5,2,8,6,7,9", "8,6,5,9,3,7,4,2,1");
                
	CREATE TABLE IF NOT EXISTS users (
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(50),
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        pass VARCHAR(50),
        games_won INT,
        games_started INT,
        current_game_id INT
    );