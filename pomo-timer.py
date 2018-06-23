from gpiozero import LED
import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ledGreen = LED(15)
ledBlue = LED(18)
text = input('hit enter or press the button to get to work')

def timer(t, ledLightOn, ledLightOff):
    ledLightOn.on()
    ledLightOff.off()
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

while True:
    input_state = GPIO.input(17)
    if input_state == False or text == '':
        timer(1500, ledBlue, ledGreen)
        timer(300, ledGreen, ledBlue)
        ledGreen.off()
        ledBlue.off()
