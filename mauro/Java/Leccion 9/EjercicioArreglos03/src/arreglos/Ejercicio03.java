package arreglos;

import java.util.Scanner;

/*
    Ejercicio 3: Leer 5 números por teclado, almacenarlos en
    un arreglo y a continuacion realizar la media de los
    números positivos, negativos y contar el número de ceros.
*/

public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float numeros[] = new float[5];
        float negativos = 0, positivos = 0, mediaNegativos, mediaPositivos;
        int conteo0 = 0, conteo_negativos = 0, conteo_positivos = 0;
        
        System.out.println("Guardamos los elementos del arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.println((i+1)+". Digite un número: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i]>0){
                positivos += numeros[i];
                conteo_positivos++;
            }
            else if(numeros[i]<0){
                negativos += numeros[i];
                conteo_negativos++;
            }
            else{
                conteo0++;
            }
        }
        
        // Mostrar conteo y media de Positivos
        if(conteo_positivos == 0){
            System.out.println("\nNo se puede sacar la media de los números positivos");
        }
        else{
            mediaPositivos = positivos/conteo_positivos;
            System.out.println("\nLa media de los números positivos es: " + mediaPositivos);
        }
        
        // Mostrar conteo y media de Negativos
        if(conteo_negativos == 0){
            System.out.println("\nNo se puede sacar la media de los números negativos");
        }
        else{
            mediaNegativos = negativos/conteo_negativos;
            System.out.println("\nLa media de los números negativos es: " + mediaNegativos);
        }
        
        // Ceros
        System.out.println("\nLa cantidad de ceros es: " + conteo0);
    }
    
}
