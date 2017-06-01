#!/usr/bin/env python3
#master_client_v1 Manuel Kilzer 2017 
# [x] Wohnzimmer 1/2 	//Raspberry PI Version B+

#room_clients
# [ ] Wohnzimmer 2/2	//Raspberry PI Version Zero
# [ ] Flur 				//Raspberry PI Version A+
# [ ] Schlafzimmer 		//Raspberry PI Version A+
# [ ] kueche 			//Raspberry PI Version A+
# [ ] Keller 			//Raspberry PI Version A+
# [ ] Terrasse 			//Raspberry PI Version 1B



############################################ MODULE
#### Importieren der benoetigten Module #### MODULE
############################################ MODULE

import threading
import sys
import time
import os
import ftplib
import RPi.GPIO as GPIO
import urllib.request
import urllib.parse
import subprocess



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

#REED_1 3PINS
# REED_1_IN = X1
# + = 3.3V
# - = GROUND
#GPIO.setup(REED_1_IN, GPIO.IN)

#REED_2 3PINS
# REED_2_IN = X2
# + = 3.3V
# - = GROUND
#GPIO.setup(REED_2_IN, GPIO.IN)

#K_LED_1 4PINS
# ROT_1 = 11
# GRN_1 = 13
# BLU_1 = 15
# - = GROUND
#GPIO.setup(ROT_1, GPIO.OUT)
#GPIO.setup(GRN_1, GPIO.OUT)
#GPIO.setup(BLU_1, GPIO.OUT)

#K_LED_2 4PINS
# ROT_2 = 29
# GRN_2 = 31
# BLU_2 = 33
# - = GROUND
#GPIO.setup(ROT_2, GPIO.OUT)
#GPIO.setup(GRN_2, GPIO.OUT)
#GPIO.setup(BLU_2, GPIO.OUT)



############################################### VAR
############ Variablen ######################## VAR
############################################### VAR

ZUSTAND_SICHERHEIT = 0
#SICHERHEIT-Coode: 	# 0 = offen/unsicher
					# 1 = zu/sicher

DATETIME = time.strftime("%d.%m.%Y %H:%M")
TIME = time.strftime("%H:%M")


#INTERVALL_1 = 0.5
#INTERVALL_2 = 1

WOHNZIMMER_REED_1_IN = 0
FLUR_REED_1_IN = 0
SCHLAFZIMMER_REED_1_IN = 0
KUECHE_REED_1_2_IN = 0
KELLER_REED_1_IN = 0
KELLER_TEMPERATUR_IN = 0
KELLER_FEUCHTIGKEIT_IN = 0
TERRASSE_BEWEGUNG_1_IN = 0



####################################################### ROOM DEF
### Definition Raum-Clients -- Master Kommunikation ### ROOM DEF
####################################################### ROOM DEF

#Alle ONLINE???
def geraete_check():
	WOHNZIMMER_ON = os.system("ping -c 1 "+"192.168.178.XX")
	FLUR_ON = os.system("ping -c 1 "+"192.168.178.XX")
	SCHLAFZIMMER_ON = os.system("ping -c 1 "+"192.168.178.XX")
	KUECHE_ON = os.system("ping -c 1 "+"192.168.178.XX")
	KELLER_ON = os.system("ping -c 1 "+"192.168.178.XX")
	TERRASSE_ON = os.system("ping -c 1 "+"192.168.178.XX")


################### NETCAT Kommunikation #####################
################## IN ################ IN ####################

#Wohnzimmer_REED: PORT 1337 Eingehende Verbindung	
def wohnzimmer_client_reed_1_IN():
	global WOHNZIMMER_REED_1_IN
	os.system("nc -l -p 1337 > /home/pi/Desktop/masnc/in/1337_reed_1_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/1337_reed_1_in.txt", "r")
    ZUSTAND_VARIABLE_1337 = fin.readline()   #liest VARIABLE als String aus DATEI
    WOHNZIMMER_VAR_1_IN = int(ZUSTAND_VARIABLE_1337) #macht die VARIABLE zu einer integer Zahl
    fin.close()


#Flur_REED: PORT 1338 Eingehende Verbindung
def flur_client_reed_1_IN(): 
	global FLUR_REED_1_IN
	os.system("nc -l -p 1338 > /home/pi/Desktop/masnc/in/flur/1338_reed_1_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/flur/1338_reed_1_in.txt", "r")
	ZUSTAND_VARIABLE_1338 = fin.readline()   #liest VARIABLE als String aus DATEI
	FLUR_REED_1_IN = int(ZUSTAND_VARIABLE_1338) #macht die VARIABLE zu einer integer Zahl
	fin.close()


#Schlafzimmer_REED: PORT 1339 Eingehende Verbindung
def schlafzimmer_client_reed_1_IN(): 
	global SCHLAFZIMMER_REED_1_IN
	os.system("nc -l -p 1339 > /home/pi/Desktop/masnc/in/schlafzimmer/1339_reed_1_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/schlafzimmer/1339_reed_1_in.txt", "r")
	ZUSTAND_VARIABLE_1339 = fin.readline()   #liest VARIABLE als String aus DATEI
	SCHLAFZIMMER_REED_1_IN = int(ZUSTAND_VARIABLE_1339) #macht die VARIABLE zu einer integer Zahl
	fin.close()


#Kueche_REED: PORT 1340 Eingehende Verbindung
#Coode- Beide Fenster Zu 					== 0 keins
#Coode- Rechtes Fenster offen linkes Zu		== 1 rechts
#Coode- Linkes Fenster offen rechtes Zu 	== 2 links
#Coode- Beide Fenster offen					== 3 beide
def kueche_client_reed_1_2_IN(): 
	global KUECHE_REED_1_2_IN
	os.system("nc -l -p 1340 > /home/pi/Desktop/masnc/in/kueche/1340_reed_1_2_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/kueche/1340_reed_1_2_in.txt", "r")
	ZUSTAND_VARIABLE_1340 = fin.readline()   #liest VARIABLE als String aus DATEI
	KUECHE_REED_1_2_IN = int(ZUSTAND_VARIABLE_1340) #macht die VARIABLE zu einer integer Zahl
	fin.close()


#Keller_REED: PORT 1341 Eingehende Verbindung
def keller_client_reed_1_IN():
	global KELLER_REED_1_IN
	os.system("nc -l -p 1341 > /home/pi/Desktop/masnc/in/keller/1341_reed_1_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/keller/1341_reed_1_in.txt", "r")
	ZUSTAND_VARIABLE_1341 = fin.readline()   #liest VARIABLE als String aus DATEI
	KELLER_REED_1_IN = int(ZUSTAND_VARIABLE_1341) #macht die VARIABLE zu einer integer Zahl
	fin.close()

#Keller_TEMPERATUR: PORT 1342 Eingehende Verbindung
def keller_client_temperatur_IN():
	global KELLER_TEMPERATUR_IN
	os.system("nc -l -p 1342 > /home/pi/Desktop/masnc/in/keller/1342_temperatur_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/keller/1342_temperatur_in.txt", "r")
	ZUSTAND_VARIABLE_1342 = fin.readline()   #liest VARIABLE als String aus DATEI
	KELLER_TEMPERATUR_IN = int(ZUSTAND_VARIABLE_1342) #macht die VARIABLE zu einer integer Zahl
	fin.close()

#Keller_FEUCHTIGKEIT: PORT 1343 Eingehende Verbindung
def keller_client_feuchtigkeit_IN():
	global KELLER_FEUCHTIGKEIT_IN
	os.system("nc -l -p 1343 > /home/pi/Desktop/masnc/in/keller/1343_feuchtigkeit_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/keller/1343_feuchtigkeit_in.txt", "r")
	ZUSTAND_VARIABLE_1343 = fin.readline()   #liest VARIABLE als String aus DATEI
	KELLER_FEUCHTIGKEIT_IN = int(ZUSTAND_VARIABLE_1343) #macht die VARIABLE zu einer integer Zahl
	fin.close()

def kellerabfrage():
	keller_client_reed_1_IN()
	keller_client_temperatur_IN()
	keller_client_feuchtigkeit_IN()


#TERRASSE_BEWEGUNG: PORT 1349 Eingehende Verbindung
def terrasse_client_bewegung_1_IN():
	global TERRASSE_BEWEGUNG_1_IN
	os.system("nc -l -p 1349 > /home/pi/Desktop/masnc/in/terrasse/1349_bewegung_1_in.txt")
	fin = open("/home/pi/Desktop/masnc/in/terrasse/1349_bewegung_1_in.txt", "r")
	ZUSTAND_VARIABLE_1349 = fin.readline()   #liest VARIABLE als String aus DATEI
	TERRASSE_BEWEGUNG_1_IN = int(ZUSTAND_VARIABLE_1349) #macht die VARIABLE zu einer integer Zahl
	fin.close()


def gesamtabfrage():
	wohnzimmer_client_reed_1_IN()
	flur_client_reed_1_IN()
	schlafzimmer_client_reed_1_IN()
	kueche_client_reed_1_2_IN()
	kellerabfrage()
	terrasse_client_bewegung_1_IN()


################### NETCAT Kommunikation ##################### 
################## OUT ############## OUT #################### 

#Example Jede Variable hat eine Eigene Datei so spart man Speichervorgaenge!!!

#Wohnzimmer_ZUSTAND_0_1: PORT 1344 Ausgehende Verbindung
def nc_write_to_wohnzimmer_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1344 < /home/pi/Desktop/masnc/out/wohnzimmer/1344_out_zustand_0.txt")
		print("sending 0 to Wohnzimmer...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1344 < /home/pi/Desktop/masnc/out/wohnzimmer/1344_out_zustand_1.txt")
		print("sending 1 to Wohnzimmer...")

	else:
		print("Der Zustand im Wohnzimmer wurde nicht geaendert!")


#Flur_ZUSTAND_0_1: PORT 1345 Ausgehende Verbindung
def nc_write_to_flur_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1345 < /home/pi/Desktop/masnc/out/flur/1345_out_zustand_0.txt")
		print("sending 0 to Flur...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1345 < /home/pi/Desktop/masnc/out/flur/1345_out_zustand_1.txt")
		print("sending 1 to Flur...")

	else:
		print("Der Zustand im Flur wurde nicht geaendert!")


#Schlafzimmer_ZUSTAND_0_1: PORT 1346 Ausgehende Verbindung
def nc_write_to_schlafzimmer_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1346 < /home/pi/Desktop/masnc/out/schlafzimmer/1346_out_zustand_0.txt")
		print("sending 0 to Schlafzimmer...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1346 < /home/pi/Desktop/masnc/out/schlafzimmer/1346_out_zustand_1.txt")
		print("sending 1 to Schlafzimmer...")

	else:
		print("Der Zustand im Schlafzimmer wurde nicht geaendert!")


#Kueche_ZUSTAND_0_1: PORT 1347 Ausgehende Verbindung
def nc_write_to_kueche_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1347 < /home/pi/Desktop/masnc/out/kueche/1347_out_zustand_0.txt")
		print("sending 0 to Kueche...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1347 < /home/pi/Desktop/masnc/out/kueche/1347_out_zustand_1.txt")
		print("sending 1 to Kueche...")

	else:
		print("Der Zustand in der Kueche wurde nicht geaendert!")


#Keller_ZUSTAND_0_1: PORT 1348 Ausgehende Verbindung
def nc_write_to_keller_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1348 < /home/pi/Desktop/masnc/out/keller/1348_out_zustand_0.txt")
		print("sending 0 to Keller...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1348 < /home/pi/Desktop/masnc/out/keller/1348_out_zustand_1.txt")
		print("sending 1 to Keller...")

	else:
		print("Der Zustand im Keller wurde nicht geaendert!")


#Terrasse_ZUSTAND_0_1: PORT 1350 Ausgehende Verbindung
def nc_write_to_terrasse_zustand_0_1():
	global ZUSTAND_SICHERHEIT
	if ZUSTAND_SICHERHEIT == 0:
		os.system("nc -w 1 192.168.178.XX 1350 < /home/pi/Desktop/masnc/out/terrasse/1350_out_zustand_0.txt")
		print("sending 0 to Terrasse...")

	elif ZUSTAND_SICHERHEIT == 1:
		os.system("nc -w 1 192.168.178.XX 1350 < /home/pi/Desktop/masnc/out/terrasse/1350_out_zustand_1.txt")
		print("sending 1 to Terrasse...")

	else:
		print("Der Zustand auf der Terrasse wurde nicht geaendert!")


def nc_write_to_all_zustand_0_1():
	nc_write_to_wohnzimmer_zustand_0_1()
	nc_write_to_flur_zustand_0_1()
	nc_write_to_schlafzimmer_zustand_0_1()
	nc_write_to_kueche_zustand_0_1()
	nc_write_to_keller_zustand_0_1()
	nc_write_to_terrasse_zustand_0_1()
	print("Es wurde ueberall versucht den Zustand zu aendern!")


########################################################### DEF
################# Sonstige Definitionen ################### DEF
########################################################### DEF

#MASTER LOGFILE
def logTOfile_master(nachricht):
    doc = open("/home/pi/Desktop/logfiles/master.log", "a")##### GESAMT LOG
    doc.write((time.strftime("%a " "%d.%m.%y " "%H:%M MEZ")) +": "+nachricht+ "\n")
    doc.close()
#Example logTOfile_master("Example")

#LCD Zeile 1
def lcd_z1(nachricht):
	open("/home/pi/Desktop/var/lcd_z1.txt", "w").close()
    doc = open("/home/pi/Desktop/var/lcd_z1.txt", "a")##### LCD Zeile 1
    doc.write(nachricht)
    doc.close()
#Example lcd_z1("Example") #16 Digits

#LCD Zeile 2
def lcd_z2(nachricht):
	open("/home/pi/Desktop/var/lcd_z2.txt", "w").close()
    doc = open("/home/pi/Desktop/var/lcd_z2.txt", "a")##### LCD Zeile 2
    doc.write(nachricht)
    doc.close()
#Example lcd_z2("Example") #16 Digits

#FTP UPLOAD
def ftpupload():
    session = ftplib.FTP('ftp.strato.com','kilmanu.de','twox88iix')
    file = open('/home/pi/Desktop/Geraete/geraete.log','rb')
    session.storbinary('STOR /rpi/geraete.log', file)
    file.close()
    session.quit()



######################################### T1 ZEIT
### Hier beginnt Thread 1 Deklaration ### T1 ZEIT
######################################### T1 ZEIT

def zeiterfassung():
	global TIME
	TIME = time.strftime("%H:%M")
	time.sleep(60)

####################################### T1 ZEIT
### Hier endet Thread 1 Deklaration ### T1 ZEIT
####################################### T1 ZEIT



######################################### T2 Sonnenauf//untergang
### Hier beginnt Thread 2 Deklaration ### T2 Sonnenauf//untergang
######################################### T2 Sonnenauf//untergang

#Globale variable SOAU fuer den Sonnenaufgang
#Beispiel = 05:46
def SoAu():
    global SOAU
    fin = open("/home/pi/Desktop/var/sonnenaufgang.txt", "r")
    SOAU = fin.readline()
    fin.close()

#Globale variable SOUN fuer den Sonnenuntergang   
#Beispiel = 21:23
def SoUn():
    global SOUN
    fin = open("/home/pi/Desktop/var/sonnenuntergang.txt", "r")
    SOUN = fin.readline()  
    fin.close()

####################################### T2 Sonnenauf//untergang
### Hier endet Thread 2 Deklaration ### T2 Sonnenauf//untergang
####################################### T2 Sonnenauf//untergang


######################################### T1 ZEIT
###### Hier beginnt Thread 1 COODE ###### T1 ZEIT
######################################### T1 ZEIT

class Thread1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
    	while (True):
    		zeiterfassung()

####################################### T1 ZEIT
###### Hier endet Thread 1 COODE ###### T1 ZEIT
####################################### T1 ZEIT


######################################### T2 Sonnenauf//untergang
###### Hier beginnt Thread 2 COODE ###### T2 Sonnenauf//untergang
######################################### T2 Sonnenauf//untergang

class Thread2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
    	SoAu()
    	SoUn()
        while (True):
    		if TIME == "00:04":
    			SoAu()
    			SoUn()
    			time.sleep(60)

    		else:
    			time.sleep(59)

####################################### T2 Sonnenauf//untergang
###### Hier endet Thread 2 COODE ###### T2 Sonnenauf//untergang
####################################### T2 Sonnenauf//untergang



######################################### Start all Threads
### Hier werden die Threads gestartet ### Start all Threads
######################################### Start all Threads

#Start Thread 1
#Was passiert im Thread
background1 = Thread1()
background1.start()


#Start Thread 2
#Was passiert im Thread
background2 = Thread2()
background2.start()

