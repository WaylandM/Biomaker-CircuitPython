Line by line explanation:

```python
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
```

* Creates a NeoPixel controller on the pin connected to the onboard RGB LED.
* `1` means there is one pixel.

```python
pixel[0] = (50, 0, 0)
```

* Sets pixel 0 to a colour using RGB values.
* `(50, 0, 0)` = red (brightness 50 out of 255).

```python
pixel[0] = (0, 0, 0)
```

* Sets the pixel to black (all channels 0) = off.

The same infinite loop and `time.sleep(0.5)` calls make it blink on and off.

In both cases, you’re just repeatedly:

* writing a value to the LED
* waiting a bit
* writing the opposite value
* waiting again
