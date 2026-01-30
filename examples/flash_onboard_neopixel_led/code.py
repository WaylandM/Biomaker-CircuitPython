import time
import board
import neopixel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    pixel[0] = (50, 0, 0)  # red
    time.sleep(0.5)
    pixel[0] = (0, 0, 0)   # off
    time.sleep(0.5)

