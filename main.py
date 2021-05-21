from UsbReader import UsbReader
from ControlGPIO import ControlGPIO

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
      gpio.blink(0.5, 10)
  except KeyboardInterrupt:
      print("Salida forzada")
  finally:
    gpio.exit()
  
  #main()