On boards that support CircuitPython you’ll often see two kinds of firmware files offered for download: **.uf2** and **.bin**.
They contain essentially the same firmware, but are meant to be installed in different ways.

### UF2 (USB Flashing Format)

* Designed to be **drag-and-drop friendly**
* You put the board into bootloader mode and it appears as a USB drive (e.g. `CIRCUITPY` or `BOOT`)
* You simply **copy the `.uf2` file onto that drive**
* The bootloader reads the UF2 blocks and flashes the firmware automatically
* Very safe and hard to brick
* No extra tools required

This is the normal method for:

* Adafruit boards
* RP2040 boards
* Most SAMD, nRF, and ESP32-Sx boards with UF2 bootloaders

### BIN (raw binary image)

* A plain compiled firmware image
* Must be written to flash at a specific address
* Requires a flashing tool, for example:

  * `esptool.py` (ESP32 family)
  * `bossac` (some SAMD boards)
  * vendor IDE or SWD/JTAG programmer
* Easier to misuse (wrong address = non-booting board)

This is used when:

* The board doesn’t have a UF2 bootloader
* You are doing low-level or recovery flashing
* You’re using a manufacturer’s flashing utility

### Practical rule of thumb

* If your board shows up as a USB drive when you double-tap reset → use **.uf2**
* If the instructions mention a command-line flasher and an address like `0x1000` or `0x10000` → use **.bin**

For most everyday CircuitPython installs and updates, **use the UF2 file**.


---------------------------------------------

On boards that support CircuitPython you’ll often see two kinds of firmware files offered for download: **.uf2** and **.bin**.
They contain essentially the same firmware, but are meant to be installed in different ways.

### UF2 (USB Flashing Format)

* Designed to be **drag-and-drop friendly**
* You put the board into bootloader mode and it appears as a USB drive (e.g. `CIRCUITPY` or `BOOT`)
* You simply **copy the `.uf2` file onto that drive**
* The bootloader reads the UF2 blocks and flashes the firmware automatically
* Very safe and hard to brick
* No extra tools required

This is the normal method for:

* Adafruit boards
* RP2040 boards
* Most SAMD, nRF, and ESP32-Sx boards with UF2 bootloaders

### BIN (raw binary image)

* A plain compiled firmware image
* Must be written to flash at a specific address
* Requires a flashing tool, for example:

  * `esptool.py` (ESP32 family)
  * `bossac` (some SAMD boards)
  * vendor IDE or SWD/JTAG programmer
* Easier to misuse (wrong address = non-booting board)

This is used when:

* The board doesn’t have a UF2 bootloader
* You are doing low-level or recovery flashing
* You’re using a manufacturer’s flashing utility

### Practical rule of thumb

* If your board shows up as a USB drive when you double-tap reset → use **.uf2**
* If the instructions mention a command-line flasher and an address like `0x1000` or `0x10000` → use **.bin**

For most everyday CircuitPython installs and updates, **use the UF2 file**.
