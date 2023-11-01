package Ejercicio6;

import java.util.Scanner;

// Guillermo tiene N dólares. Luis tiene la mitad de lo que posee Guillermo.
// Juan tiene la mitad de lo que poseen Luis y Guillermo juntos.
// Hacer un programa que calcule e imprima la cantidad de dinero que tienen los tres.


public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        System.out.println("Ingrese la cantidad de dinero que tiene Guillermo: ");
        guillermo= Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("El dinero de Luis es: U$$"+luis);
        System.out.println("El dinero de Juan es: U$$"+juan);
        System.out.println("El total de dinero entre los tres es de: U$$"+ total);
    }
}
