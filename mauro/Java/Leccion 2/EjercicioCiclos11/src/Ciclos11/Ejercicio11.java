
package Ciclos11;

/*
    Ejercicio 11: Diseñar un programa que muestre el producto
    de los 10 primeros números impares
    (JOptionPane solo)
*/

import javax.swing.JOptionPane;

public class Ejercicio11 {
    public static void main(String[] args) {
        
        long producto = 1;
        for(int i = 1; i <= 20 ; i += 2){ // El aumento apunta a solo ir por numeros impares
                     producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los números impares es: " + producto);
    }
    
}
