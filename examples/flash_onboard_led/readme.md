This script will:
1. Set up the onboard LED pin as a digital output.
2. Turn in on for 0.5 seconds.
3. Turn it off for 0.5 seconds.
4. Repeat this on-off cycle indefinitely.


Let’s go through the example line by line and explain what each part does.

```python
import time
import board
import digitalio
```

* `time` gives access to timing functions like `sleep()`.
* `board` contains names for the physical pins on your specific board (like `board.LED`).
* `digitalio` lets you control pins as simple on/off digital signals.

```python
led = digitalio.DigitalInOut(board.LED)
```

* `board.LED` is a predefined pin that’s connected to the onboard LED.
* `DigitalInOut(...)` creates an object that lets you control that pin.
* The variable `led` now represents the LED pin.

```python
led.direction = digitalio.Direction.OUTPUT
```

* Pins can be inputs (read signals) or outputs (send signals).
* Here we set the LED pin to be an **output**, so we can drive it on and off.

```python
while True:
```

* This starts an infinite loop.
* Everything indented underneath will repeat forever until the board is reset or powered off.

```python
    led.value = True   # LED on
```

* Setting `value` to `True` sends a HIGH signal to the pin.
* On most boards this turns the LED on.

```python
    time.sleep(0.5)
```

* Pause the program for 0.5 seconds (500 milliseconds).
* The LED stays on during this pause.

```python
    led.value = False  # LED off
```

* Setting `value` to `False` sends a LOW signal.
* This turns the LED off.

```python
    time.sleep(0.5)
```

* Wait another 0.5 seconds with the LED off.
* Then the loop repeats, so the LED turns on again.

Overall behaviour:

1. Turn LED on
2. Wait half a second
3. Turn LED off
4. Wait half a second
5. Repeat forever

That creates a steady blink: on–off–on–off every second.
