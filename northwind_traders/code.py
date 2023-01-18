import pandas as pd
import os
import psycopg2

'''считаем данные по поставщикам'''
cur_path = os.path.dirname(__file__)
read_path = os.path.relpath('data/suppliers.json', cur_path)
file = pd.read_json(read_path)

'''создадим необходимые таблицы'''
conn = psycopg2.connect(host='localhost', dbname='northwind_traders', user='oleg', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute('''
            DROP TABLE IF EXISTS products_suppl, suppliers;
            CREATE TABLE products_suppl(
            id_tab SERIAL NOT NULL PRIMARY KEY, 
            id_sup text, 
            product_name text);
            CREATE TABLE suppliers(
            id_tab SERIAL NOT NULL PRIMARY KEY,
            company_name VARCHAR(100),
            contact VARCHAR(100),
            address VARCHAR(100),
            phone VARCHAR(100),
            fax VARCHAR(100),
            homepage VARCHAR(100),
            id_sup VARCHAR(100));
            ''')
except:
    print('something went wrong')

'''заполним таблицы данными по поставщикам'''
conn = psycopg2.connect(host='localhost', dbname='northwind_traders', user='oleg', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            for i in range(len(file)):
                a = list(file.loc[i])
                a[-1] = i
                cur.execute('''
                INSERT INTO suppliers(company_name, contact, address, phone, fax, homepage, id_sup)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', a)
                for j in file.iloc[i, 6]:
                    cur.execute('INSERT INTO products_suppl (id_sup, product_name) VALUES (%s, %s)', [i, j])
except:
    print('something went wrong again')