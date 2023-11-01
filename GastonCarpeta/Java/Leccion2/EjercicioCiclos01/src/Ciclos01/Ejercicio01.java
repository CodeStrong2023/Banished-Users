/*
Ejercico1: leer un numero y mostrar su cuadrado,
repetir el proceso hasta que se introduzca un numero negativo
*/
package Ciclos01;


import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
      numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
      while(numero >= 0){
      cuadrado = (int)Math.pow(numero, 2);
          System.out.println("el numero "+numero+"elevado al cuadrado es: "+cuadrado);
          System.out.println("Digite otro numero");
          numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
      }
        System.out.println("el programa a finales por numeros negativo");
    }
}
