import gpiozero
import time

# Maybe include a popup pinout to mark button connection
GPIOA = 4 
GPIOB = 1

peckdiskA = gpiozero.Button(GPIOA)
peckdiskB = gpiozero.Button(GPIOB)

starttime = time.time()
try:    
    while True:
        if peckdiskA.is_pressed:
            print('Coice A :)')
            time.sleep(0.2)
        elif peckdiskB.is_pressed:
            print('Choice B :(')
            time.sleep(0.2)
        looptime = time.time()
        if looptime - starttime > 20:
            print('session ended') 
            break
        
except KeyboardInterrupt:
    print('session aborted') 

peckdiskA.close()
peckdiskB.close()