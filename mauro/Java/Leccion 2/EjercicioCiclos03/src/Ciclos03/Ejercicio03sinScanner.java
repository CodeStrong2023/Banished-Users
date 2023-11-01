package Ciclos03;

// Ejercicio 3: Leer números hasta que se introduzca un cero
// Para cada uno indicar si es par o impar.
// Primero lo haremos con la clse Scanner
// Luego con la clase JOptionPane

import javax.swing.JOptionPane;

public class Ejercicio03sinScanner {
    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" Es PAR");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número ingresado "+numero+" Es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "El número ingresado es "+numero+" finaliza el programa");
    }
}
