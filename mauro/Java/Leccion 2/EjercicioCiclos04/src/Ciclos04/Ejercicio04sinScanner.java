package Ciclos04;

/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuátnos números se han introducido.
Lo hacemos con Scanner y JOptionPane
 */

import javax.swing.JOptionPane;

public class Ejercicio04sinScanner {
    public static void main(String[] args) {
        int numero, conteo = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es POSITIVO");
            conteo ++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" números que no son negativos");
    }
}