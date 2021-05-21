import RPi.GPIO as GPIO
import time

class ControlGPIO():
    def __init__(self, pinNumber=16):
      print("Hello world")
      self.pinNumber = pinNumber
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(pinNumber, GPIO.OUT)
      self.tiempo = time
    
    def blink(self,time, veces):
      for item in range(veces):
        GPIO.output(self.pinNumber, True)
        self.tiempo.sleep(time)
        GPIO.output(self.pinNumber, False)
        self.tiempo.sleep(time)
    
    def exit(self):
        GPIO.cleanup()  