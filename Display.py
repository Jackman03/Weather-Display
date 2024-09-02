#Jackson Vaughn
#This file displays the weather info on the LCD screen

#Imports
import time	
import Driver as LCD	
from datetime import datetime
import GetWeatherData as Data
LCD.setup()
#Clear screen 
LCD.clear()
while True:
	
	#Display current time and date
	
	
	
	#Display City, State and tempeture
	
	#Display weather data and message
	
	LCD.write(Data.CITY,LCD.LINE_1)
	LCD.write(str(Data.temp_f) + " degrees",LCD.LINE_2)
	
	time.sleep(1)


LCD.clear()
