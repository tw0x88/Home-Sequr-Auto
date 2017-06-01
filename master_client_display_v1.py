#!/usr/bin/env python2
#master_client_v1 Manuel Kilzer 2017 
# [x] Wohnzimmer 1/2 	//Raspberry PI Version B+



############################################ MODULE
#### Importieren der benoetigten Module #### MODULE
############################################ MODULE

import sys
import time
import os
import RPi.GPIO as GPIO
import lcddriver



######################################## GPIO SET
########## GPIO Einstellungen ########## GPIO SET
######################################## GPIO SET

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#GPIO Layout "BOARD"

#GPIO_01 = 3.3V			GPIO_02 = 5.0V
#GPIO_03 = SDA1,I2C		GPIO_04 = 5.0V
#GPIO_05 = SCL1,I2C		GPIO_06 = GROUND
#GPIO_07 = 7			GPIO_08 = TXD0
#GPIO_09 = GROUND		GPIO_10 = RXD0
#GPIO_11 = 11			GPIO_12 = 12
#GPIO_13 = 13			GPIO_14 = GROUND
#GPIO_15 = 15			GPIO_16 = 16
#GPIO_17 = 3.3V			GPIO_18 = 18
#GPIO_19 = SPI,MOSI		GPIO_20 = GROUND
#GPIO_21 = SPI,MISO		GPIO_22 = 22
#GPIO_23 = SPI,CLK		GPIO_24 = SPI,CE0
#GPIO_25 = GROUND		GPIO_26 = SPI,CE1
#GPIO_27 = I2C,ID		GPIO_28 = I2C,ID
#GPIO_29 = 29			GPIO_30 = GROUND
#GPIO_31 = 31			GPIO_32 = 32
#GPIO_33 = 33			GPIO_34 = GROUND
#GPIO_35 = 35 			GPIO_36 = 36
#GPIO_37 = 37			GPIO_38 = 38
#GPIO_39 = GROUND 		GPIO_40 = 40



########################################## GPIO VAR
############# GPIO Belegung ############## GPIO VAR
########################################## GPIO VAR

#16x2 Display 4PINS
DISPLAY_POWER = 7 # + = 3.3V (Eingentlich 5V benoetigt)
# I2C = GPIO_03
# I2C = GPIO_05
# - = GROUND
GPIO.setup(DISPLAY_POWER, GPIO.OUT)
GPIO.output(DISPLAY_POWER, GPIO.LOW)



############################################### VAR
############ Variablen ######################## VAR
############################################### VAR

TIME = time.strftime("%d.%m.%Y %H:%M")

SEKUNDEN = 2

DISPLAY_Z1 = "A erste Zeile  A"
DISPLAY_Z2 = TIME



########################################################### DEF
###################### Definitionen ####################### DEF
########################################################### DEF

#lcd_readfile_z1
def lcd_readfile_z1():
    global DISPLAY_Z1
    fin = open("/home/pi/Desktop/var/lcd_z1.txt", "r")
    DISPLAY_Z1 = fin.readline()   #liest VARIABLE als string aus DATEI
    
#lcd_readfile_z2
def lcd_readfile_z2():
    global DISPLAY_Z2
    fin = open("/home/pi/Desktop/var/lcd_z2.txt", "r")
    DISPLAY_Z2 = fin.readline()   #liest VARIABLE als string aus DATEI

#lcd aendern
def change_display_z1_z2():
	global DISPLAY_Z1
	global DISPLAY_Z2

	lcd_readfile_z1()
	print DISPLAY_Z1
	lcd.lcd_display_string(DISPLAY_Z1, 1) #16 Digits Zeile 1

	lcd_readfile_z2()
	print DISPLAY_Z2
	lcd.lcd_display_string(DISPLAY_Z2, 2) #16 Digits Zeile 2



########################################################### START
######################## Start Coode ###################### START
########################################################### START

GPIO.output(DISPLAY_POWER, GPIO.HIGH)
lcd = lcddriver.lcd()
lcd.lcd_clear()

lcd.lcd_display_string(DISPLAY_Z2, 2) #16 Digits Zeile 2

while True:
	change_display_z1_z2()
	time.sleep(SEKUNDEN)
