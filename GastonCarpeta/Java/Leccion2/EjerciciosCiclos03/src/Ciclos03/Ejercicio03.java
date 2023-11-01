/*
Ejercicio3: leer numeros hasta que se introduzca un cero 
para cada uno indicar si es par o impar.
primero lo haremos con la clase Scannner
primero con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {

    public static void main(String[] args) {
        int numero;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero"));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null,"el numero ingresado " + numero + "es par");
            } else {
               JOptionPane.showMessageDialog(null,"el numero ingresado " + numero + "es impar");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
    
JOptionPane.showMessageDialog(null, "el numero ingresado es " + numero + "finaliza el programa");
    }
}
