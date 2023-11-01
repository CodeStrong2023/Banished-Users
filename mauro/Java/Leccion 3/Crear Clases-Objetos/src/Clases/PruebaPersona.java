package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); // Llamamos al constructor
        persona1.nombre = "Mauro"; // El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Mesas";
        persona1.obtenerInformacion(); // Llamamos al metodo
        
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Juan";
        persona2.apellido = "Perez";
        persona2.obtenerInformacion();
    }
}
