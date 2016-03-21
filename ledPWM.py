import RPi.GPIO as GPIO # 
from time import sleep  # 
  
GPIO.setmode(GPIO.BOARD)  # 
  
GPIO.setup(07, GPIO.OUT)# set GPIO as output
  
led = GPIO.PWM(07, 100)    # create object white for PWM on pin 07 at 100 Hertz  
  
led.start(0)              # start white led on 0 percent duty cycle (off)  
red.start(100)              # red fully on (100%)  
  
# now the fun starts, we'll vary the duty cycle to   
# dim/brighten the leds, so one is bright while the other is dim  
  
pause_time = 0.02           # you can change this to slow down/speed up  
  
try:  
    while True:  
        for i in range(0,101):      # 101 because it stops when it finishes 100  
            led.ChangeDutyCycle(i)  
            sleep(pause_time)  
        for i in range(100,-1,-1):      # from 100 to zero in steps of -1  
            led.ChangeDutyCycle(i)  
            sleep(pause_time)  
  
except KeyboardInterrupt:  
    white.stop()            # stop the white PWM output  
    red.stop()              # stop the red PWM output  
    GPIO.cleanup()          # clean up GPIO on CTRL+C exit 
