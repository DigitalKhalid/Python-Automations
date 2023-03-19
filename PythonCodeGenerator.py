import requests

prompt = input('Please enter the description of your use case: Write python code to ')
file_name = input('Please specify a file name to save the generated code: ')

api_key = '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'
api_host = 'https://api.openai.com/v1/'
api_endpoint = 'completions'

url = api_host + api_endpoint

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key
}

data = {
    "model": "text-davinci-003",
    "prompt": f"write python script to {prompt}",
    "max_tokens": 500, # limits the response in terms of tokens generated for text.
    "temperature": 0.5, # range fro m 0 ~ 2, 0 for most precise and predictive response and 2 for super creative and random response.
    # "top_p": 1, # top_p is probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
    # user either temperature or top_p but not both.
    "n": 1, # number of responses generated
    "stream": False,
    "logprobs": None,
    # "stop": "\n" #Up to 4 sequences where the API will stop generating further tokens.
}

try:
    response  = requests.post(url, headers=headers, json=data)
except:
    print('Unable to connect to the AI server.')
    stop = input('-----build by BizzSole-----')

if response.status_code == 200:
    code = response.json()['choices'][0]['text']
    with open(f'{file_name}.py', 'w') as file:
        file.write(code)
    
    print('Python script created.')
    stop = input('-----build by BizzSole-----')
else:
    print(f'Request failed with status_code {response.status_code}')
    stop = input('-----build by BizzSole-----')