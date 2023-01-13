import pandas as pd
import os

cur_path = os.path.dirname(__file__)
read_path = os.path.relpath('data/suppliers.json', cur_path)
file = pd.read_json(read_path)
print(file.loc[1]['products'])


