
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("osvaldo", 57.000, false);
        System.out.println("persona1 = "+ persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //modificar a traves de los metodos
        persona1.setNombre("juan ignacio");
        //persona1.nombre = "juan ignacio";// ya no se puede usar
       // System.out.println("nombre es: "+persona1.nombre);//errros 
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        // tarea: crear otro objeto de tipo persona, asignar valores de manera inicial 
        //y imprimir, luego modificar sus valores y volver a imprimir
        System.out.println("persona1: "+persona1.toString());
    }   
}
/*
//tarea realizada
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona1 = Persona("Juan", 30)
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)


persona1.nombre = "María"
persona1.edad = 25
print("Nombre modificado:", persona1.nombre)
print("Edad modificada:", persona1.edad)
*/