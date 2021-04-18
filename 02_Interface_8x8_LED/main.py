import max7219 as display
from machine import Pin, SPI
from time import sleep
from machine import ADC

class custom_8x8():
    def __init__(self):
        self.M_LED_NUM = 4
        self.M_LED_SCROLL_DELAY = 0.09
        cs_pin_pico = 5

        spi = SPI(0)
        self.display = display.Matrix8x8(spi=spi, cs=Pin(cs_pin_pico), num=self.M_LED_NUM)
        self.display.brightness(2)
        
    
    def text_scroll(self, text):
        p = self.M_LED_NUM * 8
        for p in range(self.M_LED_NUM * 8, len(text) * -8 -1, -1):
            self.display.fill(False)
            self.display.text(text, p, 1, not False)
            self.display.show()
            sleep(self.M_LED_SCROLL_DELAY)
            
    def get_current_temp(self):
        temp_sensor = ADC(4)
        to_volts = 3.3 / 65535
        current_temp = temp_sensor.read_u16() * to_volts
        temperature = 27 - (current_temp - 0.706)/0.001721
        return temperature

matrix_led = custom_8x8()
while True:
    text = str(matrix_led.get_current_temp())
    matrix_led.text_scroll(text)



