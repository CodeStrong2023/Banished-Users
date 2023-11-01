//paso por referencia
package pasoporreferencia;

import Clases.Persona;

public class PasoPorReferencia {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre = "ester";
        System.out.println("persona1 = " + persona1.nombre);
        cambiarValor(persona1);
        System.out.println("el cambio que hicimos en el nombre es:"+persona1.nombre);
        persona1 = cambiarElValor(persona1);
        Persona persona2 = new Persona();
        //persona persona2= null;
        persona2 = cambiarElValor(persona2);
        System.out.println("el nuevo valor del objeto es: "+persona2.nombre);
    }
    
    public static void cambiarValor(Persona persona){//paso por refererncia 
        persona.nombre = " maria";
    }
   public static  Persona cambiarElValor(Persona persona){
       if (persona == null){
           System.out.println("valor de persona es invalido : null");
       return null;
       }
       else{
          persona.nombre = "monica";
       return persona; 
       }
   }
}
