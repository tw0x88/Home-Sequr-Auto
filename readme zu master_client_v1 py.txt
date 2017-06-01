readme.txt zu master_client_v1.py


++++++++++ Variablensammlung ++++++++++

DISPLAY_POWER = 7 
Schaltet das Display via GPIO Pin 7 an und aus
(Display kann erst nach dem anschalten verwendet werden).


ZUSTAND_SICHERHEIT = 0 
#SICHERHEIT-Coode: 	# 0 = offen/unsicher
					# 1 = zu/sicher
Wird abgefragt um den jeweiligen Room-Clients die entsprechende
Variable zu übergeben.


DATETIME = time.strftime("%d.%m.%Y %H:%M")
Das Format ist: 12.12.2012 08:45 //#16 Digits
//
TIME = time.strftime(%H:%M")
Das Format ist: 08:45 
Gibt einen Zeitstempel zum zeitpunkt des Aufrufes ab.


#INTERVALL_1 = 0.5
#INTERVALL_2 = 1
In Verbindung mit time.sleep()


WOHNZIMMER_REED_1_IN = 0
FLUR_REED_1_IN = 0
SCHLAFZIMMER_REED_1_IN = 0
KUECHE_REED_1_2_IN = 0
KELLER_REED_1_IN = 0
KELLER_TEMPERATUR_IN = 0
KELLER_FEUCHTIGKEIT_IN = 0
TERRASSE_BEWEGUNG_1_IN = 0
Eingehende Datenverbindung von den jeweiligen Room-Clients.


WOHNZIMMER_ON 
FLUR_ON
SCHLAFZIMMER_ON
KUECHE_ON 
KELLER_ON 
TERRASSE_ON
Erreichbarkeit der anderen Pi's // Clients via Ping in (ms)
0 = ONLINE // Alles 1+ ist OFFLINE eventuelle fein justierung.


ZUSTAND_VARIABLE_1337
ZUSTAND_VARIABLE_1338
ZUSTAND_VARIABLE_1339
ZUSTAND_VARIABLE_1340
ZUSTAND_VARIABLE_1341
ZUSTAND_VARIABLE_1342
ZUSTAND_VARIABLE_1343

ZUSTAND_VARIABLE_1349
Definitions-Variablen innerhalb von [def] nur dort funktional.
Hier zur umwandlung von string zu int.


/home/pi/Desktop/masnc/out/wohnzimmer/1344_out_zustand_0.txt
/home/pi/Desktop/masnc/out/wohnzimmer/1344_out_zustand_1.txt

/home/pi/Desktop/masnc/out/flur/1345_out_zustand_0.txt
/home/pi/Desktop/masnc/out/flur/1345_out_zustand_1.txt

/home/pi/Desktop/masnc/out/schlafzimmer/1346_out_zustand_0.txt
/home/pi/Desktop/masnc/out/schlafzimmer/1346_out_zustand_1.txt

/home/pi/Desktop/masnc/out/kueche/1347_out_zustand_0.txt
/home/pi/Desktop/masnc/out/kueche/1347_out_zustand_1.txt

/home/pi/Desktop/masnc/out/keller/1348_out_zustand_0.txt
/home/pi/Desktop/masnc/out/keller/1348_out_zustand_1.txt

/home/pi/Desktop/masnc/out/terrasse/1350_out_zustand_0.txt")
/home/pi/Desktop/masnc/out/terrasse/1350_out_zustand_1.txt")
ZUSTAND_SICHERHEIT wird hier Übergeben
Ausgehende Übergabevariablen jeweils 0 oder 1 in einer Datei.
werden via Netcat (nc) an die jeweiligen Clients geschickt.


background1
background2
Definitions-Variablen innerhalb von [Thread].
Hier zum starten von Threads.



++++++++++ Variablens TXT Sammlung ++++++++++

/home/pi/Desktop/var/lcd_z1.txt
/home/pi/Desktop/var/lcd_z2.txt
LCD Display z1 und z2 für die jeweilige Zeile
Übergabe der Texte von Python 3 zu 2
