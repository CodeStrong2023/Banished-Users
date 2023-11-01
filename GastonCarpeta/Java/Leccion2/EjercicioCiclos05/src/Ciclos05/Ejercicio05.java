/*
Ejercicio 5: realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100,y luego ir pidiendo numeros indicados "es mayor" o
"es menor" segun sea mayor o menor con respecto a N 
el proceso termina cuando el usuario acieta y mostramos 
el numero de intentos hechos.
*/
package Ciclos05;

import javax.swing.JOptionPane;

public class Ejercicio05 {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //esto genera un numero aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
            if(numero < aleatorio){
               JOptionPane.showMessageDialog(null, "digite un numero mayor");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "digite un numero menor");
            }
            else {
             JOptionPane.showMessageDialog(null, "!!!FELICIDADES !!! HAS ADIVINADO EL NUMERO");
                }
        conteo++;
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "adivina el numero en: "+conteo+" intentos");
    }
}
