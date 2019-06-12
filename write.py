import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    text = input('New data:')
    print("Halte ein Tag an das Schreibgerät.")
    reader.write(text)
    print("Written")
finally:
    GPIO.cleanup()
