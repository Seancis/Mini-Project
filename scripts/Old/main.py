from time import sleep
from datetime import datetime
import board
import time
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import adafruit_character_lcd.character_lcd as characterlcd
import os
import glob
import busio
import RPi.GPIO as GPIO
from sensor import value

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
# Testing ADC values
while True:
    bpmraw = value()
    print(bpmraw)
    
# Use this later for printing bpm and avg calories burned
lcd_line_1 = '  Open | Closed  '
lcd_line_2 = '\n Adjust|  Auto   '
lcd.message = lcd_line_1 + lcd_line_2




"""
# Create message to scroll
scroll_msg = "Fitness Tracker"

lcd.message = scroll_msg
# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(.5)
    lcd.move_left()
time.sleep(0.2)
lcd.clear()

"""
















































