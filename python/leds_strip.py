import time
import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)


def send_value(led, R, G, B):
    string_led = str(led) + '-' + str(R) + '-' + str(G) + '-' + str(B) + '\n'
    ser.write(string_led)
    time.sleep(0.02)


leds = 5
step = 5
delay = 0

time.sleep(2)

for i in range(0, 255, step):
    for j in range(0, leds):
        send_value(j, i, 254 - i, 254 - i)
    time.sleep(delay)
