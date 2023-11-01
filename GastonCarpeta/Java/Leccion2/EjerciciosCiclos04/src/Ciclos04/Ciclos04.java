/*
Ejercici 4: pedir numeros hasta que se tecle uno negativo,
y mostrar cuantos numeros se han introducido.
lo hacemo primero con la clase Scanner
luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;

import java.util.Scanner;


public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        
        System.out.println("digite un numero :");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >=0){
            System.out.println("el numero "+numero+"es positivo");
            conteo++;
            System.out.println("digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("a ingrear "+conteo+"numeros que no son negativos");
    }
 
}
