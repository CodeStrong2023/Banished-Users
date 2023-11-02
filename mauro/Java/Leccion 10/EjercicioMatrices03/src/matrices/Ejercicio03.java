package matrices;

/*
    Ejercicio 3(5* en Clase 12): Crear y cargar una matriz de tamaño n x m
    mostrar la suma de cada fila y de cada columna.
*/

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol, sumaFilas, sumaCol;
        int posFila, posCol;
        
        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el número de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el número de columnas: "));
        
        matriz = new int [nFilas][nCol];
        int filas[] = new int [nFilas];
        int columnas[] = new int [nCol];
        
        System.out.println("Rellenando la Matriz");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        
        System.out.println();
        
        System.out.println("Matriz Original:");
        for (int i = 0; i < nFilas; i++) {
            for (int j = 0; j < nCol; j++) {
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        System.out.println("");
        
        // Sumado de las filas
        posFila = 0;
        for (int i = 0; i < nFilas; i++) {
            sumaFilas = 0;
            for (int j = 0; j < nCol; j++) {
                sumaFilas += matriz[i][j];
            }
            filas[posFila] = sumaFilas;
            posFila++;
        }
        
        // Sumado de las columnas
        posCol = 0;
        for (int j = 0; j < nCol; j++) {
            sumaCol = 0;
            for (int i = 0; i < nFilas; i++) {
                sumaCol += matriz[i][j];
            }
            columnas[posCol] = sumaCol;
            posCol++;
        }
        
        
        System.out.println("La suma de las filas es: ");
        for (int i = 0; i < nFilas; i++) {
            System.out.print(filas[i]+" - ");
        }
        System.out.println("");
        
        System.out.println("La suma de las columnas es: ");
        for (int i = 0; i < nCol; i++) {
            System.out.print(columnas[i]+" - ");
        }
        System.out.println();
    }
}
