.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price FROM products GROUP BY category; 


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory GROUP BY item;


CREATE TABLE shopping_list AS
  SELECT name, store FROM products, lowest_prices 
  WHERE name = item GROUP BY category HAVING MIN(MSRP/rating) 
  ORDER BY (CASE category WHEN "games" THEN 1 WHEN "phone" THEN 2 ELSE 3 END);  -- individual order


CREATE TABLE total_bandwidth AS
  SELECT SUM(a.Mbs) FROM stores AS a, shopping_list AS b
  WHERE a.store = b.store;

