/*
ejercicios3: leer 5 numeros por teclado, almacenados en 
un arreglo y a continuacion realizar la media de los 
numeros positivos, la media de los negativos y contar el 
numero de ceros:
*/
package arreglos_ejercicios_3;

import java.util.Scanner;

public class Arreglos_Ejercicios_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner (System.in);
        float numeros[] =new float[5];
        float negativos=0,positivos=0,mediaNegativos,mediaPositivos;
        int conteo0=0,conteo_negativos=0,conteo_positivos=0;
        
        System.out.println("guardamos los elelementos del arreglo: ");
        for(int i=0;i<5;i++){
            System.out.println((i+1)+".digite un numero: ");
            numeros[i]= entrada.nextFloat();
            if(numeros[i]>0){
                positivos += numeros[i];
                conteo_positivos++;
            }
            else if(numeros[i]<0){
                negativos += numeros[i];
            }
            else{
                conteo0++;
            }
        }
        if(conteo_positivos ==0){
            System.out.println("\nNo se puede sacar la media de los negativos");
        }
        else{
            mediaPositivos = positivos/conteo_positivos;
            System.out.println("\nLamedia de los numeros positivos es"+mediaPositivos);
            
        }
        System.out.println("la cantidad de ceros es: "+conteo0);
        //ingresar:2,-5,6,-2,0
    }
    
}
