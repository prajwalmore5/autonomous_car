import RPi.GPIO as GPIO          
from time import sleep
import gspread
from oauth2client.service_account import ServiceAccountCredentials

in1 = 38
in2 = 37
en = 32
in3 = 35
in4 = 36
bn = 31
temp1=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(bn,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
q=GPIO.PWM(bn,1000)
q.start(100)
'''
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('auto.json',scope)
client = gspread.authorize(creds)

sh = client.open('AutoCar')
sheet = sh.get_worksheet(0)
'''

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):
    '''
    speed = sheet.cell(1,1).value
    print(speed)
    '''
    speed=raw_input()
    
    if speed=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         speed='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         speed='z'


    elif speed=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        speed='z'
        
    elif speed=='st':
        print("straight")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        speed='z'
        
    elif speed=='lf':
        print("left")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        speed='z'

    elif speed=='rt':
        print("right")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=1
        speed='z'

    elif speed=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        speed='z'

    elif speed=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        speed='z'

    elif speed=='l':
        print("low")
        p.ChangeDutyCycle(25)
        speed='z'

    elif speed=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        speed='z'

    elif speed=='h':
        print("high")
        p.ChangeDutyCycle(75)
        speed='z'
     
    
    elif speed=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
