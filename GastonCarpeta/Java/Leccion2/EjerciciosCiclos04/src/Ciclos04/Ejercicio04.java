/*
Ejercici 4: pedir numeros hasta que se tecle uno negativo,
y mostrar cuantos numeros se han introducido.
lo hacemo primero con la clase Scanner
luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        
       
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero :"));
        while(numero >=0){
           JOptionPane.showMessageDialog(null, "el numero "+numero+"es positivo");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero :"));
        }
        JOptionPane.showMessageDialog(null, "a ingrear "+conteo+"numeros que no son negativos");
        
    }
}
