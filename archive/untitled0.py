
import time
import pigpio

# GPIO pin
servo = 14 

MIN_WIDTH=500
MAX_WIDTH=2500



pi = pigpio.pi()

if not pi.connected:
   exit()

while True:

   try:
       pi.set_servo_pulsewidth(14, 500)
       time.sleep(1)
       pi.set_servo_pulsewidth(14, 0)
       time.sleep(1)
       #pi.set_servo_pulsewidth(14, 1475) neutral position
       pi.set_servo_pulsewidth(14, 2500)
       time.sleep(1)
       pi.set_servo_pulsewidth(14, 0)
       time.sleep(1)

   except KeyboardInterrupt:
      break

print("\nTidying up")
pi.set_servo_pulsewidth(14, 0)

pi.stop()


pi.set_servo_pulsewidth(14, 2500)
time.sleep(0.82)
pi.set_servo_pulsewidth(14, 0)
time.sleep(1)
pi.set_servo_pulsewidth(14, 500)
time.sleep(0.82)
pi.set_servo_pulsewidth(14, 0)