import os

class UsbReader():
  def __init__(self):
    #Directory acces
    self.BASE_DIRECTORY = '/media/quimeraEyes'
    
    #Direcotrios según su label de usb
    self.USB_LABEL_DIR = {'CICLO_FOR': '/media/quimeraEyes/CICLO_FOR'}
      
  def createDirectory(self): #FIRST COMMAND
    
    try:
      print("creating directory")
      #Initial directory
      os.system('sudo mkdir ' + self.BASE_DIRECTORY)
      
      #USB Directorys
      for clave in self.USB_LABEL_DIR:
        os.system('sudo mkdir ' +  self.USB_LABEL_DIR[clave])
        
    except:
      print("No media directory, create now...")
      os.system('sudo mkdir /media')
      self.createDirectory()

  def mountUSB(self): #SECOND COMMAND
    print("Montando USB")
    try:
      #Mount usb
      for clave in self.USB_LABEL_DIR :
        os.system('sudo mount -L ' + clave + ' ' + self.USB_LABEL_DIR[clave])
    except:
      print("Falta alguna usb para que funcione")
  
  def umountUSB(self): #FINAL COMMAND
    print("Desmontando USB")
    try:
      #Mount usb
      for clave in self.USB_LABEL_DIR:
        os.system('sudo umount ' + self.USB_LABEL_DIR[clave])
    except:
      print("Desmontaje sin exito")
  
  def listArchives(self): # Devolver nombreArchivo : ruta 
    print("listing archives")
    archivesOnUSB = {}
    for clave in self.USB_LABEL_DIR:
      archivesOnUSB[self.USB_LABEL_DIR[clave]] = os.listdir(self.USB_LABEL_DIR[clave])
    return archivesOnUSB

  '''
    El metodo findArchive recive como parametros
    dictRutaArchivos que es un diccionario creado por el metodo listArchives()
    nombreArchivo que es el nombre de un archivo
    devuelve la ruta completa del archivo si está en el directorio
  '''
  def findArchive(self, dictRutaArchivos, nombreArchivo=''): #
    for ruta in dictRutaArchivos:
      for archivo in dictRutaArchivos[ruta]:
        if(archivo == nombreArchivo):
          return ruta + '/' + archivo