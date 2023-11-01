package Ciclos02;

// Ejercicio 2: Leer un número e indicar si es positivo o
// negativo. El proceso se repetira hasta que se introduzca
// un cero 0

import javax.swing.JOptionPane;

public class Ejercicio02sinScanner {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null,"El número "+numero+" finaliza el programa");
    }
}