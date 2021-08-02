# Blink
This is a small python programme for arduino.

## About this project
This is a small project to code arduino uno with python with the help of [pyfirmata](https://pyfirmata.readthedocs.io/en/latest/) library.
This programme will just blink the built in LED light of arduino uno.

## Requirements
* A arduino uno board
* A USB cable type A/B
* ardunio IDE :- [Download Here](https://www.arduino.cc/en/software)
* Python installed in your computer 

## Steps

* Connect the arduino to your PC with the USB cable.
* After downloading the Arduino IDE go to ``` File/Examples/Firmata/StandardFirmata ```
* After StandardFirmata code is loaded. Select ``` Tools/Board ``` and select **Arduino Uno**.
* Then go to ``` Tools/Port ``` and select the port avilable in windows it might me as **COM2** , **COMP3** or similar to that. in mac or linux it might be different. But you have to select one of the option avilable.
* After you have selected your Board and Port hit the Upload button on the top left corner right next to the verify button.

* Now install [pyfirmata](https://pyfirmata.readthedocs.io/en/latest/) library. run ```pip install pyfirmata``` .
* After installing just run the Blink.py file as you run a normal python file.

### Happy Coding.😉


