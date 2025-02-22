import machine
import utime

pin1 = machine.Pin('LED', machine.Pin.OUT)
pin2 = machine.Pin(12, machine.Pin.OUT)
pin3 = machine.Pin(13, machine.Pin.OUT)
pin4 = machine.Pin(14, machine.Pin.OUT)
pin5 = machine.Pin(15, machine.Pin.OUT)

pins = [pin1, pin2, pin3, pin4, pin5]


for i in range(0, 2**len(pins)):
    binary_string = '{:0{}b}'.format(i, len(pins))
    print(binary_string)

    for j in range(len(pins)):
        pins[j].value(int(binary_string[j]))

    utime.sleep(2)