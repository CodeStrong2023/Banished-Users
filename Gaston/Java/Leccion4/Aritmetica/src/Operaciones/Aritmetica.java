
package Operaciones;


public class Aritmetica {
    // atributos de la clase
    int a;
    int b;
    
    //el constructor es un metodo especial
    public Aritmetica (){//constructor 1
        System.out.println("se esta ejecutando este constructor numero uno");
    }
    // estamos viendo lo que se llama sobrecarga de consructores
    public Aritmetica (int a, int b){//constructor 2
        this.a = a;
        this.b = b;
        System.out.println("se esta ejecutando el constructor numero dos");
    }
    
    //metodo
    public void sumarNumeros(){
        int resultado =  a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
      //  int resultado = a + b;
        return a + b;
    }
    public int sumarConArgumetnos(int a, int b){
       this.a = a; // el argumetno a se asgina al atributo this.a
       this.b = b;
       // return a + b;
       return sumarConRetorno();
    }
}
