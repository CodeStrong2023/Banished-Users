
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona Persona1;
        Persona1 = new Persona(); //llamamos al constructor
        Persona1.nombre = "gaston"; //el valor hexadecimal normalmente comienza con 0x
        Persona1.apellido = "cuello";
        Persona1.obtenerInformacion();
        
        Persona Persona2 = new Persona(); 
        System.out.println("persona2 =" + Persona2);
        System.out.println("Persona1 =" + Persona1);
        Persona2.obtenerInformacion();
        Persona2.nombre = "osvaldo";Persona2.apellido = "giordanini";
        Persona2.obtenerInformacion();
    }
}
