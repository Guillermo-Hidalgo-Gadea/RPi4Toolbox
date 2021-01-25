import time
import RPi.GPIO as GPIO

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)

# Pin 7 (GPIO 4) auf Input setzen
GPIO.setup(7, GPIO.IN)


# Dauersschleife
while 1:

  # GPIO lesen
  if GPIO.input(7) == GPIO.HIGH:
    # output
    print("button press")

    # Warte 100 ms
    time.sleep(0.1)
    
########################
import gpiozero as gpio

button = gpio.Button(4)

try:
    while True:
        button.wait_for_press()
        print("Button was pressed")

except KeyboardInterrupt:
    print("quit")
    
