/*
Ejercicio9: pedir el dia mes y año de una fecha e 
indicar si la fecha es correcta. suponiendo que todos 
los meses son de 30 dias.
 */
package Ciclos09;

import javax.swing.JOptionPane;

public class Ejercicio09 {

    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("digite el dia: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("digite el mes: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("digite el año: "));
        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((anio != 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null, "la fecha ingresada es: " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "fecha incorrecta, año incorrecto");
                }
            } else {
                JOptionPane.showMessageDialog(null, "fecha incorrecta, mes incorrecto");
            }
        } else {
            JOptionPane.showMessageDialog(null, "fecha incorrecta, dia incorrecto");
        }
    }
}
