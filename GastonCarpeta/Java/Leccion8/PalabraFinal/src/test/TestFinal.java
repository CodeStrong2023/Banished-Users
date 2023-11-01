 /*
uso de la palabra final 
esta palabra tiene diferentes significados dependiendo donde
se aplique:
variables:evita cambiar el valor que almacena la variable 
mettodos:evita que se modifique la definicion o el comportamiento
de un metodo desde una subclase(hija)
clase:evita que se creen clases hijas 
otra caracteristica es que normalmente, cuando trabajamos con variables
se combina con el modificador de acceso estatico para convertir una 
variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clse Math en la cual todos sus atributos
son de tipo static y final, es por esto que la variable pi* se conoce 
como una constante.
*/
package test;
 import domain.Persona;
public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 42913250;
        System.out.println("miDni = "+miDni);
       // miDni = 20312321; no se puede modificar 
       //Persona.CONSTANTE_AQUI =9;//no se modifica
        System.out.println("mi atributo constante es: "+Persona.CONSTANTE_AQUI);
       
        final Persona persona1 = new Persona ();
        //persona1 = new Persona(); //no se puede asiganr una nueva refereencia 
        persona1.setNombre("ariel betancud");
        System.out.println("persona1 nombre: "+persona1.getNombre());
        persona1.setNombre("liliana");
        System.out.println("persona1 nombre: "+persona1.getNombre());
    }
}
