/*
Выбрать записи работников (включить колонки имени, 
фамилии, телефона, региона) в которых регион 
неизвестен
*/

SELECT last_name, first_name, home_phone, region 
FROM employees WHERE region is Null;

/*
Выбрать такие страны в которых "зарегистированы" 
одновременно заказчики и поставщики, но при этом 
в них не "зарегистрированы" работники
*/

SELECT split_part(suppliers.address, ';', 1) 
FROM suppliers
INTERSECT SELECT country FROM customers
EXCEPT SELECT country FROM employees