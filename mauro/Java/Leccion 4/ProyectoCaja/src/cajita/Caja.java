package cajita;

/*
    Ejercicio 1: Crear un proyecto según las especificaciones
    mostradas a continuación:
    Formula = ancho * alto * profundidad
*/
        
public class Caja { // Clase publica caja
    // Atributos (caracteristicas)
    int ancho;
    int alto;
    int profundidad;
    
    // Métodos y Constructores (acciones)
    public Caja(){ // Constructor 1 = Vacio
        
    }
    
    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundidad){ // Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    // Método para calcular
    public int calcularVolumen(){
        return ancho * alto * profundidad;
    }
}
