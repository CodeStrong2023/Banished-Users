
package test;

import domain.Persona;

 
public class TestArreglosObjetc {
    public static void main(String[] args) {
        Persona personas [] = new Persona[2];
        personas[0] = new Persona("ariel");
        personas[1] = new Persona("osvaldo");
        System.out.println("personas 0 = " + personas [0]);
         System.out.println("personas 0 = " + personas [1]);
         for (int i = 0 ; 1 < personas.length; i++){
             System.out.println("Personas   "+i+ personas [i] );
         }
         //trabajaamos con arreglos en la sintaxis resumida
       String frutas [] = {"banana", "pera", "durazno"} ; 
       for (int i = 0; i < frutas.length; i++){
           System.out.println("frutas = "+i+"="+ frutas[i]);
       }
}
}