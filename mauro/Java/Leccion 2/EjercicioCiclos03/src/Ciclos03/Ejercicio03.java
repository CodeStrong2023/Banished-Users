package Ciclos03;

// Ejercicio 3: Leer números hasta que se introduzca un cero
// Para cada uno indicar si es par o impar.
// Primero lo haremos con la clse Scanner
// Luego con la clase JOptionPane

import java.util.Scanner;

public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("Digite un número: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero % 2 == 0){
                System.out.println("El número ingresado "+numero+" Es PAR");
            }
            else{
                System.out.println("El número ingresado "+numero+" Es IMPAR");
            }
            System.out.println("Digite otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El número ingresado es "+numero+" finaliza el programa");
    }
}
