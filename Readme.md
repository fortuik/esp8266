## MicroPython esp8266
http://docs.micropython.org/en/latest/esp8266/

### Install MicroPython on esp8266
http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

Download: http://micropython.org/download/#esp8266

If you install MicroPython to your module for the first time, or after installing any other firmware, you should erase flash completely:
```
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=32m -fm dio 0 esp8266-20161014-v1.8.4.bin
```

### Modules
- http://docs.micropython.org/en/latest/esp8266/library/index.html
- https://github.com/micropython/micropython-lib

### MicroPython cross compiler (LOAD/Push .mpy files)
- https://forum.micropython.org/viewtopic.php?f=16&t=1962
- https://github.com/micropython/micropython/tree/master/mpy-cross
- https://github.com/robert-hh/Shared-Stuff

### Examples:
- https://github.com/mithru/MicroPython-Examples
- http://micropython-on-esp8266-workshop.readthedocs.io/en/latest/


### uPyLoader: A simple tool for communicating with MicroPython board.
- https://github.com/BetaRavener/uPyLoader

### Telnet server, connect per ssh to gate then program over telnet
- https://forum.micropython.org/viewtopic.php?f=16&t=2478

### FTP Server https://github.com/robert-hh/MicroPython-FTP-Server
- https://forum.micropython.org/viewtopic.php?f=16&t=2467
- obsolete: https://github.com/cpopp/MicroFTPServer
- obsolete: https://github.com/robert-hh/Shared-Stuff

### Sonoff esp8266 - https://www.itead.cc/smart-home/sonoff-wifi-wireless-switch.html
- requires TTL-serial adapter to flash micropython
- http://forum.micropython.org/viewtopic.php?f=16&t=2474
- http://forum.micropython.org/viewtopic.php?f=5&t=2477&start=10
- https://github.com/kfricke/micropython-sonoff-switch

### Home Assistant
- https://home-assistant.io/blog/2016/07/28/esp8266-and-micropython-part1/
- https://home-assistant.io/blog/2016/08/31/esp8266-and-micropython-part2/