/*
ejercicio 7: pedir numeros que se introduzca uno negativo 
y calcular el promedio
*/
package Ciclos07;

import javax.swing.JOptionPane;


public class Ejercicio07 {
    public static void main(String[] args) {
         int numero, conteo = 0, suma =0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        while(numero >= 0){ //mientras el numero no sea negativo
          suma += numero;
          conteo++;
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite otro numero: "));
        }
        if(conteo==0){
           JOptionPane.showMessageDialog(null, "Error, la division entre cero no existe");
        }
        else{
            promedio = (float)suma/conteo;
            JOptionPane.showMessageDialog(null, "El promedio es: "+promedio);
        }
    }
}
