#import the necessary libraries
import requests
import json

#set the API key
api_key = 'YOUR_API_KEY'

#create the data to send
data = {
    'consent': 'yes',
    'phone': '1234567890'
}

#make the request to the Klaviyo API
response = requests.post('https://a.klaviyo.com/api/v2/sms/consent', headers={'api-key': api_key}, data=data)

#check the response
if response.status_code == 200:
    print('SMS consent successfully sent')
else:
    print('Error sending SMS consent')