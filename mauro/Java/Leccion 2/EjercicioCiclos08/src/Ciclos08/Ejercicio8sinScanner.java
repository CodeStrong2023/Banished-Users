package Ciclos08;

import javax.swing.JOptionPane;

/*
    Ejercicio 8: Pedir un número N, y mostrar todos los números
    del 1 al N. (JOptionPane)
*/

public class Ejercicio8sinScanner {
    public static void main(String[] args) {
        // Pedimos el numero
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        // Ciclo para mostar los n desde 1
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        }
        
    }
}
