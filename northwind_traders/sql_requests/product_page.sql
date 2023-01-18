/*
Найти активные (см. поле discontinued) продукты из категории 
Beverages и Seafood, которых в продаже менее 20 единиц. 
Вывести наименование продуктов, кол-во единиц в продаже, 
имя контакта поставщика и его телефонный номер.
*/

SELECT products.product_name, products.units_in_stock, suppliers.contact, suppliers.phone FROM products 
INNER JOIN products_suppl USING(product_name)
INNER JOIN suppliers USING(id_sup)
WHERE discontinued = 0
AND units_in_stock < 20
AND (category_id = 1 OR category_id = 8)


