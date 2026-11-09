import json
class LectorUSB():
    def __init__(self, archivoUSB):
        self.json = json
        self.archivoUSB = archivoUSB
        self.resultadoUSB = {"type":None, "action":None, "repeat":None, "time":None}
    def buscarInformacion(self):
        for clave in self.archivoUSB: 
            with open(clave) as json_file:
                auxiliarJSON = self.json.load(json_file)
                type = auxiliarJSON["usb"]["type"]
                function = auxiliarJSON["usb"]["funcion"]
                if type == 0: 
                    self.resultadoUSB["type"] = function
                elif type == 1:
                    self.resultadoUSB["action"] = function
                elif type == 2:
                    self.resultadoUSB["repeat"] = function
                elif type == 3:
                    self.resultadoUSB["time"] = function
        return self.resultadoUSB
