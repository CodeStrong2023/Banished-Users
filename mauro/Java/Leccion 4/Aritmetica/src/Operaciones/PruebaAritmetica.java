package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; // Variables Locales
        int b = 7; // Memoria Stack
        miMetodo(); // Llamamos al método nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumar();
        
        // Para almacenar un objeto o los atributos se utiliza la memoria "Heap"
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        // aritmetica1 = null; nunca utilizar esto, no se debe hacer
        // System.gc(); Método para limpiar residuos, es pesado
        
        Persona persona = new Persona("Mauro", "Mesas");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
    // Modularidad creamos un nuevo método
    public static void miMetodo(){
        // a = 10;
        System.out.println("Aqui hay otro método");
    }
}

class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ // Constructor
        super(); // Llamada al constructor de la clase padre object
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this.nombre);
    }
}

class Imprimir{
    public Imprimir(){
        super(); // El constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresión del objeto actual (this): " + this);
    }
}
