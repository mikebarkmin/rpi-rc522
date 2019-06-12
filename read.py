import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Halte ein Tag an das Lesegerät.")

try:
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()
