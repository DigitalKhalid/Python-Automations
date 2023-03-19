import csv
import json
import requests
import pandas as pd

with open('shopify-order.json') as f:
    data = json.load(f)

# write csv file
df = pd.json_normalize(data, 'orders', max_level=2)
df.to_csv('orders1.csv', index=False)

print(f'CSV file created')
