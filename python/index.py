import time
import serial


def send_value(led, R, G, B):
    string_led = str(led) + '-' + str(R) + '-' + str(G) + '-' + str(B) + '\n'
    ser.write(string_led)


ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

time.sleep(2)

for i in range(0, 255, 5):
    for j in range(0, 5):
        send_value(j, i, 254 - i, 254 - i)
    time.sleep(0.01)
