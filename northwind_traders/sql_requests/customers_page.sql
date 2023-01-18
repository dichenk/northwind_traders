--- Посчитать количество заказчиков
SELECT COUNT(*) FROM customers;

/*
Выбрать все уникальные сочетания городов и стран, 
в которых "зарегестрированы" заказчики
*/
SELECT DISTINCT city, country from customers;


/*
Найти заказчиков и обслуживающих их заказы сотрудников,
таких, что и заказчики и сотрудники из города London, 
а доставка идёт компанией Speedy Express. 
Вывести компанию заказчика и ФИО сотрудника.
*/

SELECT customers.company_name, employees.last_name, employees.first_name
FROM orders
INNER JOIN customers USING(customer_id)
INNER JOIN employees USING(employee_id)
INNER JOIN shippers ON orders.ship_via = shippers.shipper_id
WHERE shippers.company_name = 'Speedy Express'
AND customers.city = 'London'
AND employees.city = 'London';


/*
Найти заказчиков, не сделавших ни одного заказа. 
Вывести имя заказчика и order_id.
*/
SELECT customers.contact_name, orders.order_id FROM orders
FULL JOIN customers
USING(customer_id)
WHERE orders.order_id is Null