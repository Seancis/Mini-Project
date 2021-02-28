from pulsesensor import Pulsesensor
import time
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import os
import glob
import busio
import RPi.GPIO as GPIO
import mysql.connector
"""------------------------------------------------------------------------"""
"""                        DATABASE AWS CONNECTION                         """
"""------------------------------------------------------------------------"""
mydb = mysql.connector.connect(
  host="3.133.13.224",
  user="nperic",
  password="AS3@394$57w*21QSvxa",
  database="project"
)

mycursor = mydb.cursor()



"""------------------------------------------------------------------------"""
"""                             LCD Display                                """
"""------------------------------------------------------------------------"""
# Defining LCD Character Size
lcd_columns = 16
lcd_rows = 2

# GPIO Pin configuration for LCD:
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D4)

# Initializing LCD Class from library
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight
)



p = Pulsesensor()
p.startAsyncBPM()

try:
    while True:
        bpm = p.BPM #Getting bpm from sensor
        calories = ((-55.0969 + (0.6309 * bpm) + (0.1988 * 62) + (0.2017 * 30))/4.184) * 60 * 1
        """Where HR = Heart rate (in beats/minute)
        W = Weight (in kilograms)
        A = Age (in years)
        T = Exercise duration time (in hours)"""

        if bpm > 0:
            lcd_line_1 = "BPM: %d" % bpm
            lcd_line_2 = "\nCalories Burned: %d" % calories
            lcd.message = lcd_line_1 + lcd_line_2
            print("BPM: %d" % bpm)
        else:
            lcd_line_1 = "No Heartbeat"
            lcd_line_2 = " "
            lcd.message = lcd_line_1 + lcd_line_2
            print("No Heartbeat found")
        time.sleep(20)
except:
    p.stopAsyncBPM()


"""
sql = "INSERT INTO heartbeats (totalHeartBeats, caloriesburned) VALUES (%s, %s)"
            val = (bpm, calories)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
"""