import Adafruit_CharLCD  as LCD
import Adafruit__ADS1x15 
import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
GPIO.SETMODE(GPIO.BCM)
lcd1 = 12
lcd2 =7
lcd3 = 8
lcd4= 25
lcd5 =24
lcd6=23
lcd = LCD. Adafruit_CharLCD(lcd1,lcd2,lcd3,lcd4,lcd5,lcd6,0,16,2)
fromaddr = "21je0921@iitism.ac.in" //sender email  address
toaddr ="sahaswatadri@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] ="pulse_rate"
while True :
    pulse_rate =Adafruit__ADS1x15.read_retry(Adafruit__ADS1x15.ADS1115,21)
    lcd.message("pulse :" +str(pulse_rate)+"beat/minute")
    time.sleep(1)
    msg.attach(MIMEText(pulse_rate,'plain'))
server =smtplib.SMTP('smtp.gmail.com',25)
server.starttls()
server.login(fromaddr,"XY9076rtp")//where XY9076rtp is password of fromaddr
if  pulse_rate > 100:
    text1 = "HIGH PULSE RATE"
    server.sendmail(fromaddr,toaddr,text1) 
elif pulse_rate < 60 :
    text2 = "LOW PULSE RATE"
    server.sendmail(fromaddr,toaddr,text2)
else:
    server.quit()



