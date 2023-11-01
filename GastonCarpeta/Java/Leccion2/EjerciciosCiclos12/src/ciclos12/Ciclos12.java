/*
ejercici 12: pedir un numero y calcular su factorial
hacerlo con las dos clases, scanner y JOptionPane
 */
package ciclos12;

import javax.swing.JOptionPane;
// import java.util.scanner;
public class Ciclos12 {
    public static void main(String[] args) {
        //scanner entrada = new scanner(system.in9;
        long factorial = 1;
        //system.out.print("digite un numero":);
        int numero = Integer.parseInt(JOptionPane.showInputDialog("digite un numero: "));
        for(int i=1; i<=numero;i++){
            factorial *=i;
        }
        //system.out.println("\El factorial del numero ingresado es:2+factorial);
        JOptionPane.showMessageDialog(null, "el factorial del numero ingresado es: "+factorial);
    }
}
