from UsbReader import UsbReader
from ControlGPIO import ControlGPIO
from ActionsExecuter import ActionsExecuter
from LectorUSB import LectorUSB
def main():
  gpio = ControlGPIO()
  reader = UsbReader()
  reader.createDirectory()
  reader.mountUSB()
  listaArchivos = reader.listArchives()
  test = reader.findArchive(listaArchivos, 'quimera.json')
  lector = LectorUSB(test)
  infoArchivos = lector.buscarInformacion()
  
  try:
      ejecutor = ActionsExecuter(infoArchivos, gpio)
      ejecutor.setCiclo()
      
  except KeyboardInterrupt:
      print("Salida forzada")
  finally:
    gpio.exit()
  
  print(infoArchivos)

  
  #IMPORTANT!!!!!!!!!! DONT REMOVE
  reader.umountUSB()

if __name__ == "__main__":
  '''
  try:
      gpio = ControlGPIO()
      diccionario = {
        "type": 0,
        "action":0,
        "time":0.1,
        "repeat": 13
      }
      Ejecutor = ActionsExecuter(diccionario, gpio)
      Ejecutor.setCiclo()
      
  except KeyboardInterrupt:
      print("Salida forzada")
  finally:
    gpio.exit()
  '''
  main()