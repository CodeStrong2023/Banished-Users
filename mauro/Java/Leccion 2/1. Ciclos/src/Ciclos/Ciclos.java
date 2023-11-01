package Ciclos;


public class Ciclos {
    // Clase 1
    public static void main(String[] args) {
        // Ciclo While (Ejercicios)
        var conteo = 0; // Inferencia de tipos
        while(conteo <= 7){
            System.out.println("conteo = " + conteo);
            conteo++; // Vamos aumentando en uno la variable
        }
        
        // Ciclo Do While
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        // Ciclo For
        for(var contando = 0; contando < 7; contando++){
            if (contando % 2 == 0){ // Números Pares
                System.out.println("contando = " + contando);
            }
        }
        
        // Uso de las palabras Break y Continue junto las etiquetas (labels)
        for(var contando = 0; contando < 7; contando++){
            if (contando % 2 == 0){ // Números Pares
                System.out.println("contando = " + contando);
                break;
            }
        }
        
        inicio:
        for(var contando = 0; contando < 7; contando++){
            if (contando % 2 != 0){ // Números Impares
                continue inicio; // Vamos a la siguiente iteración
            }
            System.out.println("contando = " + contando);
        }
    }
}
