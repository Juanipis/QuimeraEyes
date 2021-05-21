import os
from UsbReader import UsbReader
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
  main()