#Jackson Vaughn
import os
import requests
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
KEY = os.getenv('KEY')
CITY = 'London'
URL = f'https://api.weatherapi.com/v1/current.json?key={KEY}&q={CITY}'

response = requests.get(URL).json()

#print(response)

temp_f = response['current']['temp_f']
