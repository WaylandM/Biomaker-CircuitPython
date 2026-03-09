import time
import board
import digitalio

# The LED on the sensor kit base is connected to pin D4 (GP4)
led = digitalio.DigitalInOut(board.GP4)   # Change pin if needed
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   # LED ON
    time.sleep(0.5)

    led.value = False  # LED OFF
    time.sleep(0.5)

    