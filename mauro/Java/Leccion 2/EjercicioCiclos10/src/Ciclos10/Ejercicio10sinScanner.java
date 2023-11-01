package Ciclos10;

/*
    Ejercicio 10: Pedir 10 números y escribir la suma total
    (Clase JOptionPane)
*/

import javax.swing.JOptionPane;

public class Ejercicio10sinScanner {
    public static void main(String[] args) {
        int numero, suma = 0;
        for( int i = 1; i <= 10; i++){
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros es: " + suma);
    }
}
