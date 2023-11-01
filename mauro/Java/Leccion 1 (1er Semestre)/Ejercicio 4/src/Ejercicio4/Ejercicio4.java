package Ejercicio4;

// Ejercicio 4: El Mayor de dos Números (operador ternario)

import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el primer número: ");
        int num1 = scanner.nextInt();

        System.out.print("Ingrese el segundo número: ");
        int num2 = scanner.nextInt();

        int mayor = (num1 > num2) ? num1 : num2;

        System.out.println("El mayor de los dos números es: " + mayor);
    }
}

