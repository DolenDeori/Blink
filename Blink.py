import pyfirmata # importing pyfirmata library
import time      # importing time library

# Defigning the port of our Arduino. In my case it's COMP7
port = 'COM7'
board = pyfirmata.Arduino(port) 


pin = 13
i = 0   # setting the value of counter to 0
while i < 10:
    board.digital[pin].write(1)     # This code sets the LED to 1 i.e. turning on the light.
    time.sleep(4)   # wait for 4 sec
    board.digital[pin].write(0)     # Tis line sets the LED to 0 i.e turning off the light
    time.sleep(4)   # Then agin wait for another 4 sec
    i += 1  # incriment the value of counter