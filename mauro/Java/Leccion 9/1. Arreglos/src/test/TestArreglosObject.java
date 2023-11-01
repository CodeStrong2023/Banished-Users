package test;

import domain.Persona;


public class TestArreglosObject {
    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Mauro");
        personas[1] = new Persona("Gabriel");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[1]);
        
        for (int i = 0; i < personas.length; i++){
            System.out.println("personas "+ i + " = " + personas[i]);
        }
        
        // Trabajamos con arreglos en la sintaxis resumida
        String frutas[] = {"Banana", "Pera", "Manzana", "Durazno"};
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("frutas = " + frutas[i]);
        }
    }
}
