import psycopg2
import pandas as pd

conn = psycopg2.connect(host='localhost', dbname='northwind_traders', user='oleg', password='12345')
return_product = pd.DataFrame(columns=['id продукта', 'наименование продукта', 'наименование категории продукта', 'цена продукта'])
return_category = pd.DataFrame(columns=['id категории', 'наименование категории', 'описание категории', 'список продуктов, относящихся к этой категории'])

def get_product_by_id(id = None):
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f'SELECT product_id, product_name, category_name, unit_price FROM products INNER JOIN categories USING(category_id) WHERE product_id = {id}')
                rows = cur.fetchall()
                for row in rows:
                    return_product.loc[len(return_product)] = row
                return return_product.to_json(orient='records', force_ascii=False)

    except:
        return None

def get_category_by_id(id = None):
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f'SELECT category_id, category_name, description FROM categories WHERE category_id = {id}')
                row = list(cur.fetchall()[0])
                cur.execute(f'SELECT product_name FROM products WHERE category_id = {id}') ## извлекаю список продуктов
                products = cur.fetchall()
                product_list = []
                for i in products:
                    product_list.append(i[0])
                row.append(str(product_list))
                return_category.loc[len(return_category)] = row
                return return_category.to_json(orient='records', force_ascii=False)

    except:
        return None

