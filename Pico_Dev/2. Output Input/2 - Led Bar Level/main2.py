import machine
import utime

# Define the GPIO pins connected to the LEDs
pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
leds = []

# Initialize each pin as an output and store it in the leds list
for pin_number in pins:
    led = machine.Pin(pin_number, machine.Pin.OUT)
    leds.append(led)

for j in range(len(pins)):
    leds[j].value(0)
    
utime.sleep(2)

for i in range(0, 2**len(pins)):
    binary_string = '{:0{}b}'.format(i, len(pins))

    for j in range(len(pins)):
        leds[j].value(int(binary_string[j]))

    utime.sleep(.2)

utime.sleep(2)

for j in range(len(pins)):
    leds[j].value(0)