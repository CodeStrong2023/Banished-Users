package test;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;
import java.util.Date;


public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Mauro", 10000.0);
        System.out.println("empleado1 = " + empleado1);
        
//        Date fecha1 = new Date();
//        
//        Cliente cliente1 = new Cliente(fecha1, true, "Carlos", 'M', 32, "9 de Julio");
//        System.out.println("cliente1 = " + cliente1);
//        
//        // Clase 10: Sobrecarga de Constructores
//        Persona persona1 = new Persona();
    }
}
