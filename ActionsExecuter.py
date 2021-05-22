"""
{
  type: valor
  action: valor
  time: valor
  repeat: valor
}
"""
import time

class ActionsExecuter(object):
    def __init__(self, arguments, ControlGPIO):
        self.time = time
        self.arguments = arguments
        self.ControlGPIO = ControlGPIO
    
    def setActions(self, state):
      #Definicion de acciones
      if(self.arguments["action"] == 0): #Encender y apagar
        if(state==0):
          self.ControlGPIO.encenderLed()
        elif(state==1):
          self.ControlGPIO.apagarLed()

    
    def setCiclo(self):
      #Definicion de ciclos
      if(self.arguments["type"] == 0):
        self.cicloFor(
                      self.arguments["time"],
                      self.arguments["repeat"])
      
      self.ControlGPIO.exit()
    
    def cicloFor(self,time,repeticiones):
      for i in range(repeticiones):
        self.setActions(0)
        self.time.sleep(time)
        self.setActions(1)
        self.time.sleep(time)
