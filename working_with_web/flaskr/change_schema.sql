CREATE TABLE IF NOT EXISTS buildings(id PRIMARY KEY, adress TEXT);
CREATE TABLE IF NOT EXISTS flats(id PRIMARY KEY, building_id INTEGER, number INTEGER);
INSERT INTO buildings (adress)
VALUES
   ("Adress_1"),
   ("Adress_2"),
   ("Adress_3"),
   ("Adress_4");
INSERT INTO flats (building_id, number)
VALUES
   (1, 58), (1, 59), (1, 60),
   (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
   (3, 100), (3, 101),
   (4, 10), (4,11), (4,12);