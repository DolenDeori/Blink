'''
This is a game where you have to guss a number and when you success fully guess the number 
the LED of arduino will turned on.

The arduino process will be same as Blink.py. After you have loaded the StandardFirmata programme in your arduino.
just run this py file after you have changed the port value to your arduiono port.
Remember This will work for Arduino uno.
'''

import pyfirmata    # To give instruction to arduino with python
import time       
import random       # To generate a random number
import pyttsx3      # For voice instruction

model = pyttsx3.init()

PIN = 13
PORT = 'COM7'
board = pyfirmata.Arduino(PORT)


# making speak function 
def speak(word):
    model.say(word)
    model.runAndWait()


# The game ---------------------------------
random_number = random.randint(1 , 100)

i = 1
while True:
    try:
        user_guess = int(input('Guess a number between 1 and 100 : '))
    except Exception as e:
        print(e)
        continue
    if user_guess == random_number:
        speak('Congratulation ! You won the game.')
        print('Yeee ! you have done it.')
        print(f"Number of attempts : {i}")
        board.digital[PIN].write(1)  # turn on the LED
        time.sleep(10) # wait for 10 sec
        board.digital[PIN].write(0) # turn off the LED
        break

    elif user_guess < random_number:
        speak('The number you have guess is less then the actual. Try a higher number.')
        print("The number you have guess is less then the actual try a higher number.")
        i += 1
        continue
    elif user_guess > random_number:
        speak('The number you have guess is higher then the actual. Try a smaller number.')
        print("The number you have guess is higher then the actual try a smaller number.")
        i += 1
        continue

