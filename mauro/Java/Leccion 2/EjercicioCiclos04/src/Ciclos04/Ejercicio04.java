package Ciclos04;

/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuátnos números se han introducido.
Lo hacemos con Scanner y JOptionPane
 */

import java.util.Scanner;

public class Ejercicio04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un número");
        numero = Integer.parseInt(entrada.nextLine());
        
        while(numero >= 0){
            System.out.println("El numero "+numero+" es POSITIVO");
            conteo ++;
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("A ingresad "+conteo+" números que no son negativos");
    }
}
