#Jackson Vaughn
import os
import requests
from dotenv import load_dotenv, dotenv_values
import time
# loading variables from .env file
load_dotenv() 
KEY = os.getenv('KEY')
CITY = 'Orlando'
URL = f'https://api.weatherapi.com/v1/current.json?key={KEY}&q={CITY}'

def GetTemp():
	
	response = requests.get(URL).json()

	#time.sleep(10000)

	temp_f = response['current']['temp_f']
	
	return temp_f
