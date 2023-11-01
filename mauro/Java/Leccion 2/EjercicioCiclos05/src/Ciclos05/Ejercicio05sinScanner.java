package Ciclos05;

/*
Ejercicio 5: Realizar un juego para adivinar un número,
para ello general un número aleatorio entre 0-100, y
luego ir pidiendo números indicando "es mayor" o
"es menor" según sea mayor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos
el número de intentos hechos.
 */

import javax.swing.JOptionPane;

public class Ejercicio05sinScanner {
    public static void main(String[] args) {
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); // Esto genera un num aleatorio
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            
            if(numero < aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número MAYOR");
            }
            else if(numero > aleatorio){
                JOptionPane.showMessageDialog(null, "Digite un número MENOR");
            }
            else{
                JOptionPane.showMessageDialog(null, "Felicidades! Has adivinado el número: "+aleatorio);
            }
            conteo++;
        }while(numero != aleatorio);
        
        JOptionPane.showMessageDialog(null, "Adivinaste el número en: "+conteo+" intentos");
    }
}
