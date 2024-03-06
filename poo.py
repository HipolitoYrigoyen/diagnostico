   ## crea una clase llamda vehiculo capsa de procesar la informacion basica d los autos en una consecionaria. Debera tener constructor y los atributos del vehiculo serán: patente, goma, marca, modelo, kilometraje. Crear metodos (accesos) getter y (modifiacion) setter. mopstrar por pantalla al menos 1 atrubuto y modificar el kilometrajes

#patente
#goma
#marca
#modelo
#kilometraje

class Vehiculo:
    def __init__(self, patente, marca, kilometraje):
        self.patente = patente
        self.marca = marca
        self.kilometraje = kilometraje

    def get_patente(self):
        return self.patente
    def set_patente(self, patente):
        self.patente = patente
    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca
    def get_kilometraje(self):
        return self.kilometraje
    def set_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje
    def mostrar_kilometraje(self):
        print("el kilometraje es de:", self.kilometraje)


vehiculo = Vehiculo("A200 Sedan", "Mercedes Benz", 12400)
print("El vehiculo es de la marca:", vehiculo.get_marca())
vehiculo.mostrar_kilometraje()




 
