import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Halte ein Tag an das Lesegerät.")

try:
    while True:
        id, text = reader.read()
        print(id)
        print(text)
        sleep(4)
except KeyboardInterrupt:
    GPIO.cleanup()
