package test;

// Clase 8
import dominio.Persona; // Usar import dominio.*; para importar todas las clases dentre del paquete

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Mauro", 50.000, false);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        
        // Modificar a través de los métodos
        persona1.setNombre("Juan Perez");
        // persona1.nombre = "Juan Perez"; // Ya no se puede utilizar (por que es privado)
        // System.out.println("Nombre es: = " + persona1.nombre:); // Error
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        // Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        // y imprimir, luego modificar sus valores y volver a imprimir.
        
            // Se crea el objeto con sus valores
            Persona persona2 = new Persona("Marcos", 10.000, true);
        
            // Se imprimen los valores
            System.out.println("persona2 su nombre es: " + persona2.getNombre());
            System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
            System.out.println("persona2 su boolean es: " + persona2.isEliminado());
        
            // Modificó los valores
            persona2.setNombre("Nacho Gonzalez");
            persona2.setSuedo(32.000);
            persona2.setEliminado(false);
        
            // Se imprimen los valores modificados
            System.out.println("persona2 su nombre es: " + persona2.getNombre());
            System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
            System.out.println("persona2 su boolean es: " + persona2.isEliminado());
        
        
        System.out.println("persona1: " + persona1.toString());
    }    
}
