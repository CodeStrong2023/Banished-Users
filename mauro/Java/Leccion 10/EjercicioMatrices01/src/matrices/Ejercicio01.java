package matrices;

import java.util.Scanner;

/*
    Ejercicio 1(3* en Clase 12): Crear y cargar una matriz de
    tamaño 3x3, transponerla y mostrarla.
*/

public class Ejercicio01 {
    public static void main(String[] args) {
        // Definimos la matriz
        Scanner entrada = new Scanner(System.in);
        int matriz[][] = new int [3][3];
        
        // Ciclo para llenar la matriz
        System.out.println("Rellenar la matriz: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                        matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println();
        
        System.out.println("Matriz Original: ");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
        
        System.out.println();
        
        // Matriz Transpuesta
        System.out.println("Matriz Transpuesta");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                    System.out.print(matriz[j][i] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}
