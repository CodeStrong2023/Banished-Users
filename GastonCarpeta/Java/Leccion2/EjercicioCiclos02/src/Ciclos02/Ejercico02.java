/*
Ejercicio2: leer un numero e indicar si es positivo o neegativo. el proceso se repetira hasta que se introduzca 
un cero 0
 */
package Ciclos02;

import javax.swing.JOptionPane;


public class Ejercico02 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        System.out.println("digite un numero: ");
        while(numero !=0){
            if(numero > 0){
                System.out.println("el numero "+numero+"es positivo");
            }
            else{
                System.out.println("el numero "+numero+"es negativo");
            }
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        System.out.println("el numero "+numero+"finaliza el programa");
    }
    
    private static class importJOptionPane {

        public importJOptionPane() {
        }
    }
}
