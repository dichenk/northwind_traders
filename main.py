import os
from northwind_traders.code import *
from northwind_traders.functions import *

'''работаем с заполнением бд'''
tasks1_2()


while 1:
    answer = (input('product or category? ')).lower()
    if answer in ('product', '1', 'first', 'whatever'):
        answer = input('you\'ve choosen a product\ninput an id: ')
        answer = get_product_by_id(answer)
    else:
        answer = input('you\'ve choosen a category\ninput an id: ')
        answer = get_category_by_id(answer)
    print(f'получен ответ формата {type(answer)}, вот он:\n{answer}')

