import RPi.GPIO as GPIO
import schedule
import time
import datetime


relay_pin = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, 1)

def lights_on():
    GPIO.output(relay_pin, 0)

def lights_off():
    GPIO.output(relay_pin, 1)

schedule.every().day.at("06:00").do(lights_on)
schedule.every().day.at("22:00").do(lights_off)
now_hour = datetime.datetime.now().hour

try:
    if now_hour  >= 6 and now_hour < 22:
        lights_on()

    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
