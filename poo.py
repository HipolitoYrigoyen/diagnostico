   ## crea una clase llamda vehiculo capsa de procesar la informacion basica d los autos en una consecionaria. Debera tener constructor y los atributos del vehiculo serán: patente, goma, marca, modelo, kilometraje. Crear metodos (accesos) getter y (modifiacion) setter. mopstrar por pantalla al menos 1 atrubuto y modificar el kilometrajes

public class Vehiculo {
   String Patente;
   String Goma;
   String Marca;
   String Modelo;
   String Kilometraje;



public Vehiculo (String Patente, String Goma, String Marca, String Modelo, String Kilometraje){
   this.patente=patente;
   this.goma=goma;
   this.marca=marca;
   this.modelo=modelo;
   this.kilometraje=kilometraje;
 }
}


class Vehiculo{ 
   constructor(kilometraje){
   this.kilometraje = kilometraje;
}
get kilometraje() {
return this.kilometraje;
}
set kilometraje(NuevoKilometraje){ 
this.kilometraje = NuevoKilometraje;
 }
}
   



#patente
#goma
#marca
#modelo
#kilometraje



 
