from UsbReader import UsbReader
from ControlGPIO import ControlGPIO
from ActionsExecuter import ActionsExecuter
def main():
  reader = UsbReader()
  reader.createDirectory()
  reader.mountUSB()
  listaArchivos = reader.listArchives()
  print(listaArchivos)
  test = reader.findArchive(listaArchivos, 'test2.txt')
  with open(test) as archive:
    print(archive.read())

  
  #IMPORTANT!!!!!!!!!! DONT REMOVE
  reader.umountUSB()

if __name__ == "__main__":
  try:
      gpio = ControlGPIO()
      diccionario = {
        "type": 0,
        "action":0,
        "time":0.2,
        "repeat": 19
      }
      #gpio.blink(2,3)
      Ejecutor = ActionsExecuter(diccionario, gpio)
      Ejecutor.setCiclo()
      
  except KeyboardInterrupt:
      print("Salida forzada")
  finally:
    gpio.exit()
  
  #main()