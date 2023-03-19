import requests
import pandas as pd

access_token = input('Provide access token: ')
filters = input('Provide filters: ')

# API URL
store_name = 'mcgrocer-com'
version = '2023-01'
resource = 'orders'
limit = 250

if filters:
    url = f'https://{store_name}.myshopify.com/admin/api/{version}/{resource}.json?limit={limit}&{filters}'
else:
    url = f'https://{store_name}.myshopify.com/admin/api/{version}/{resource}.json?limit={limit}'

headers = {
    'Accept': 'application/json',
    'X-Shopify-Access-Token': f'{access_token}'
}

# request orders from shopify
try:
    response = requests.get(url, headers=headers)
except:
    print('API not responding')

# convert response to json
if response.status_code == 200:
    data = response.json()
    
    # write csv file
    df = pd.json_normalize(data, 'orders', max_level=2)
    df.to_csv('orders.csv', index=False)

    print(f'CSV file created')

else:
    print(f'Request failed with status code {response.status_code}')
