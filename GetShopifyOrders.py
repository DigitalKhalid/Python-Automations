import csv
import requests
# import argparse

access_token = input('Provide access token: ')
filters = input('Provide filters: ')

# parser = argparse.ArgumentParser()
# parser.add_argument('access_token', help='provide access token generated from your Shopify admin.')
# parser.add_argument('filter', help='provide filters if any.')
# args  = parser.parse_args()

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
    # stop = input('---Build by Khalid---')

# convert response to json
if response.status_code == 200:
    data = response.json()

    # open csv file
    csv_file = open('orders.csv', 'w')

    # write headers to csv
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Order ID', 'Name', 'Email', 'Total Price'])

    # loop through orders
    for order in data['orders']:
        order_id = order['id']
        name = order['customer']['first_name'] + ' ' + order['customer']['last_name']
        email = order['customer']['email']
        total_price = order['total_price']

        # write order to csv
        csv_writer.writerow([order_id, name, email, total_price])

    # close csv file
    csv_file.close()
    print(f'CSV file create')
    # stop = input('---Build by Khalid---')

else:
    print(f'Request failed with status code {response.status_code}')
    # stop = input('---Build by Khalid---')