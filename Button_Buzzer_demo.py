
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
BUZZER = 25
GPIO.setup(BUZZER, GPIO.OUT)
def buzz(noteFreq, duration):
    halveWaveTime = 1 / (noteFreq * 2 )
    waves = int(duration * noteFreq)
    for i in range(waves):
       GPIO.output(BUZZER, True)
       time.sleep(halveWaveTime)
       GPIO.output(BUZZER, False)
       time.sleep(halveWaveTime)
def play():
    t=0
    notes=[262,294,330,262,262,294,330,262,330,349,392,330,349,392,392,440,392,349,330,262,392,440,392,349,330,262,262,196,262,262,196,262]
    duration=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,1,0.25,0.25,0.25,0.25,0.5,0.5,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,1,0.5,0.5,1]
    for n in notes:
        buzz(n, duration[t])
        time.sleep(duration[t] *0.1)
        t+=1

#play()


 
KEY_UP_PIN     = 26 
KEY_DOWN_PIN   = 6
KEY_LEFT_PIN   = 13 
KEY_RIGHT_PIN  = 5
KEY_PRESS_PIN  = 19 

KEY1_PIN       = 18
KEY2_PIN       = 23


GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up


while 1:
    if GPIO.input(KEY_UP_PIN)==0:
        print ("Joy Up")
        buzz(262, 0.3)
        
    if GPIO.input(KEY_LEFT_PIN)==0: 
        print ("Joy left")
        buzz(262, 0.3)
        
    if GPIO.input(KEY_RIGHT_PIN)==0: 
        print ("Joy right")
        buzz(262, 0.3)
        
    if GPIO.input(KEY_DOWN_PIN)==0: 
        print ("Joy down")
        buzz(262, 0.3)
        
    if GPIO.input(KEY_PRESS_PIN)==0: 
        print ("Joy center")
        buzz(262, 0.3)
        
    if GPIO.input(KEY1_PIN)==0: 
       print ("KEY1")
       buzz(262, 0.3)
        
    if GPIO.input(KEY2_PIN)==0: 
        print ("KEY2")
        buzz(262, 0.3)


GPIO.cleanup()

