
package Caja;// package


public class Caja {// clase publica caja
    //atributos(caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //metodos y constructores (acciones)
    public Caja(){//constructor 1 = vacio 
    }
    //CONSTRUCTOR CON PARAMETROS
    public Caja(int ancho, int alto, int profundo){//constructor 2
      this.ancho = ancho;
      this.alto = alto;
      this.profundo = profundo;
    }
    public int calcularValor(){//metodo para calcular
        return ancho * alto *profundo;
    }

    int calcularVolumen() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
