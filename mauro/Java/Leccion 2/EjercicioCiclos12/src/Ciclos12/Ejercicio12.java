package Ciclos12;

import java.util.Scanner;
import javax.swing.JOptionPane;

/*
    Ejercicio 12: Pedir un número y calcular su factorial
    Hacerlo en Scanner y JOptionPane
*/


public class Ejercicio12 {
    public static void main(String[] args) {
        // Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        int numero;
        // System.out.println("Digite un número: ");
        // numero = Integer.parseInt(entrada.nextLine());
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        for(int i=1; i <= numero; i++){
            factorial *= i;
        }
        
        JOptionPane.showMessageDialog(null, "El factorial del número ingresado es: " + factorial);
        //System.out.println("\nEl factorial del número ingresado es: " + factorial);  
    }
}
