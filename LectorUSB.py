import json
class LectorUSB():
    def __init__(self, archivoUSB):
        self.json = json
        self.archivoUSB = self.json.load(archivoUSB)
    def buscarInformacion(self):
        info = []
        for clave in self.archivoUSB: 
            for valor in self.archivoUSB[clave]:
                print(self.archivoUSB[clave][valor])
                info.append((valor, self.archivoUSB[clave][valor]))
        return info
        
