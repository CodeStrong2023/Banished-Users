package dominio;

// Clase 7: Encapsulamiento
public class Persona {
    // Atributos
    private String nombre;
    private double sueldo;
    private boolean eliminado;
    
    // Constructor
    public Persona(String nombre, double sueldo, boolean eliminado){
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSuedo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() {
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
    // Clase 8
    public String toString(){ // Too String = Convierte en una cadena cada atributo
        return "Persona [ nombre: " + this.nombre+
                ", sueldo: " + this.sueldo+
                ", eliminado: " + this.eliminado+" ]";
    }
}
