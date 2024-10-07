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

try:
	while True:
		
		CurTemp = Data.GetTemp()
		LCD.write(Data.CITY,LCD.LINE_1)
		LCD.write(str(CurTemp) + " degrees",LCD.LINE_2)
		time.sleep(5)
		
		#Display date & time in 5 sec range
		for i in range(5):
			now = datetime.now()
			Curdate = str(now.strftime("%m-%d-%Y"))
			Curtime = str(now.strftime("%H:%M:%S"))
			LCD.write(Curdate,LCD.LINE_1)
			LCD.write(Curtime,LCD.LINE_2)
			time.sleep(1)



		LCD.clear()

except KeyboardInterrupt:
	LCD.clear()
	LCD.write("Good bye!",LCD.LINE_1)
	time.sleep(0.5)
	LCD.clear()
	print("exit")


