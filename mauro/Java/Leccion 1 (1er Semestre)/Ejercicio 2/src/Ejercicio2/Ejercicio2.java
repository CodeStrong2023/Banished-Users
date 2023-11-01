package Ejercicio2;

import java.util.Scanner;

// Ejericio 2: Hacer un programa que calcule e imprima el salario
// de un empleado, a partir de sus horas semanales trabajadas y
// de su salario  por hora

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese las horas trabajadas por semana: ");
        double horasTrabajadas = scanner.nextDouble();

        System.out.print("Ingrese el salario por hora: ");
        double salarioPorHora = scanner.nextDouble();

        double salario = horasTrabajadas * salarioPorHora;

        System.out.println("El salario del empleado es: $" + salario);
    }
}
