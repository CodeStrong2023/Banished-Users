package Ejercicio1;

import java.util.Scanner;

// Ejericio 1: Tienda de Libros

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Ingrese los datos del libro
        System.out.println("Ingrese los datos del libro");
        System.out.print("Escriba el nombre del libro: ");
        String nombre = input.nextLine();
        System.out.print("Escriba el ID del libro: ");
        int id = input.nextInt();
        System.out.print("Escriba el precio del libro: ");
        double precio = input.nextDouble();
        System.out.print("Indique si el envío es gratuito (True/False): ");
        boolean envioGratuito = input.nextBoolean();

        // Mostrar los datos del libro
        System.out.println("Nombre: " + nombre);
        System.out.println("ID: " + id);
        System.out.println("Precio: " + "$" + precio);
        System.out.println("Envío Gratuito?: " + envioGratuito);
    }
}
