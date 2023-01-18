/*
Выбрать все заказы, отсортировать по required_date 
(по убыванию) и отсортировать по дате отгрузке 
(по возрастанию)
*/

SELECT * FROM 
(SELECT * FROM orders ORDER BY required_date DESC) as wtf
ORDER BY shipped_date;

/*
Найти среднее значение дней уходящих на доставку 
с даты формирования заказа в USA
*/

SELECT AVG(shipped_date - order_date) FROM orders;

/*
Найти сумму, на которую имеется товаров 
(количество * цену) причём таких, которые 
не сняты с продажи (см. на поле discontinued)
*/

SELECT product_name, unit_price * units_in_stock 
FROM products WHERE discontinued = 0 
AND units_in_stock > 0

