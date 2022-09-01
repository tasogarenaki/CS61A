.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet From students WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song From students WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;


CREATE TABLE matchmaker AS
  -- FROM <[table_name1] AS [alias1],[table_name2] AS [alias2]...>
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b    
  WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;


CREATE TABLE sevens AS
  SELECT a.seven FROM students AS a, numbers AS b 
  -- The survey was anonymous, so use time as a unique identifier 
  -- finde out two tables "student" and "numbers" is same person
  WHERE a.time = b.time AND a.number = 7 AND b.'7' = 'True'; 

