from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep
import Adafruit_DHT 
from PIL import ImageFont

def do_nothing(obj):
    pass

def main():
    serial = i2c(port=1, address=0x3C)
    device = ssd1306(serial)
    device.cleanup = do_nothing

    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 22

    #font = ImageFont.load_default()
    custom_font = ImageFont.truetype("VCR_OSD_MONO.ttf", 21)

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")

            if humidity is not None and temperature is not None:
                str_temp = ' {0:0.2f} *C'.format(temperature)  
                str_hum  = ' {0:0.2f} %'.format(humidity)
                string = "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)
                print(string)
                draw.text((4, 10), str_temp, font=custom_font, fill=255)
                draw.text((4, 31), str_hum, font=custom_font, fill=255)
            else:
                print("Failed to retrieve data from humidity sensor")

            sleep(10)
        


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
