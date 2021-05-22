import RPi.GPIO as GPIO
import time

class ControlGPIO():
    def __init__(self, pinNumber=16):
      print("Hello world")
      self.pinNumber = pinNumber
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(pinNumber, GPIO.OUT)
      self.tiempo = time
    
    def encenderLed(self):
      GPIO.output(self.pinNumber, True)
    
    def apagarLed(self):
      GPIO.output(self.pinNumber, False)
      
    def exit(self):
        GPIO.cleanup()  