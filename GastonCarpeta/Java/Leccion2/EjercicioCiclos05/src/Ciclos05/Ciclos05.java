/*
Ejercicio 5: realizar un juego para adivinar un numero,
para ello generar un numero aleatorio entre 0-100,y luego ir pidiendo numeros indicados "es mayor" o
"es menor" segun sea mayor o menor con respecto a N 
el proceso termina cuando el usuario acieta y mostramos 
el numero de intentos hechos.
*/
package Ciclos05;

import java.util.Scanner;

public class Ciclos05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int)(Math.random()*100); //esto genera un numero aleatorio
        do{
            System.out.println("digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if(numero < aleatorio){
                System.out.println("digite un numero mayor");
            }
            else if(numero > aleatorio){
                System.out.println("digite un numero menor");
            }
            else {
             System.out.println("!!!FELICIDADES !!! HAS ADIVINADO EL NUMERO");
                }
        conteo++;
        }while(numero != aleatorio);
        System.out.println("adivina el numero en: "+conteo+" intentos");
    }
}
