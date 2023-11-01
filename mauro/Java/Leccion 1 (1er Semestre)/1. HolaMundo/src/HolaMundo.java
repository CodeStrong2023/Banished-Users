
import java.util.Scanner;

//Comentario simple
/*
Comentarios largos
mas
mas
y mas
*/
public class HolaMundo {
    public static void main(String[] args) {
        // Clase 2
        /*System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        
        // Tipo String
        String miVariableCadena = "Ejemplo";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
        */
        
        // Clase 3
        // Var - inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tab
        
        // Reglas para definir una variable en Java
        // Concatenacion
        
        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        System.out.println (usuario + " " + (a + b));
        
        // Ejercicio: caracteres espeaciales con Java
        
        var nombre = "Natalia";
        System.out.println("Nueva Linea: \n"+nombre); //Diagonal inversa: ALT + 92 y letra 
        System.out.println("Tabulador: \t"+nombre); // Tabulador: Espacio para centrar
        System.out.println("Retroceso: \b"+nombre); //Caracter de retroceso
        System.out.println("Comillas simples: \'"+nombre+"\'"); //Comillas simples
        System.out.println("Comillas dobles: \""+nombre+"\""); //Comillas dobles*/
        
        // Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        
        // Clase 4
        // Tipos Primitivos
        /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: "+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: "+ Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: "+ Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: "+ Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: "+ Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: "+ Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: "+ Long.MIN_VALUE);
        System.out.println("Valor maximo del Long: "+ Long.MAX_VALUE);*/
        
        // Tipos primitivos - Flotantes
        /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("El valor minimo de Float: "+ Float.MIN_VALUE);
        System.out.println("El valor maximo de Float: "+ Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de Double: "+ Double.MIN_VALUE);
        System.out.println("El valor maximo de Double: "+ Double.MAX_VALUE);
        */
        
        // Clase 5
        // Inferencia de Tipos var y Tipos Primitivos
        
        /*var numEntero = 20; // Las literales sin punto automaticamente son de tipo INT
        System.out.println("numEntero = "+ numEntero);
        var numFloat = 10.0F; // Automaticamente con el punto se transforma en tipo DOUBLE
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        // Tipo Primitivos CHAR (solo almacena un caracter y se hace con comillas simples)
        char miVariableChar = 'a';
        System.out.println("miVariableChar = "+miVariableChar);
        
        // Caracter Unicode
        // char
        char varCaracter = '\u0024'; // Indicamos a Java la asignación con el codigo unicode
        System.out.println("varCaracter = "+ varCaracter);
        
        char varCaracterDecimal = 36; // Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = "+ varCaracterDecimal);
        
        char varCaracterSimbolo = '$';  // Un caracter especial, podemos copiar y pegar desde unicode   
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        // var
        var varCaracter1 = '\u0024'; // Indicamos a Java la Asignación con el Codigo Unicode
        System.out.println("varCaracter1 = "+varCaracter1);
        
        var varCaracterDecimal1 = (char)36; // Hacemos la Converción para que tome el tipo CHAR
        System.out.println("varCaracterDecimal1 = "+ varCaracterDecimal1);
        
        var varCaracterSimbolo1 = '$'; // Un Caracter Especial, se puede copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        // int
        int varEnteroChar = '$'; // Nos muestra el valor decimal al simbolo (36)
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracterChar = 'b'; // Valor decimal 98 en juego de caracteres unicode
        System.out.println("caracterChar =" + caracterChar); */
        
        
        // Clase 6
        
        // Conversion de tipos parte 1
        var edad = Integer.parseInt("20"); // Convertimos un dato string a int
        System.out.println("edad = " + (edad + 1)); // Sumamos +1 a el 20 convertido a string
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("ValorPI= " + valorPI);
        
        // Pedir un valor
        var entrada = new Scanner(System.in);// El in significa que trabajaremos con la consola
        // System.out.println("Digite su edad: ");
        // edad = Integer.parseInt( entrada.nextLine()); //Convertimos string a int con parseINT
        // System.out.println("edad = " + edad);
        
        // Conversion de tipos primitivos en JavA Parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(3); // Nos muetra la posicion del indice de la cadena string
        System.out.println("fraseChar = " +fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = "+ fraseChar);
        
        
        // Clase 7
        int num1 = 5, num2 =4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
     
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
      
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado de la divison = " + solucion2);
     
        solucion = num1 % num2; //Guarda el residuo entero de la division
        System.out.println("solucion2 = " + solucion);
        
        if (num1 %2 == 0)
            System.out.println("Es un numero par");
        else
            System.out.println("Es un numero impar");
        
        /*int varNum1 = 1, varNum2 =4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        varNum1 += 1; // varNum1 = varNum1 + 1 (reducido)
        System.out.println("varNum1 = " + varNum1);
        varNum2 -= 2;
        System.out.println("varNum1 (resta) = " + varNum2);
        
        varNum1 *= 5;
        System.out.println("varNum1 (mutplicacion)= " + varNum1);
        
        varNum3 /= 4;
        System.out.println("varNum1 (division)= " + varNum3);
        
        varNum1 %= 6;
        System.out.println("varNum1 (residuo) = " + varNum1);*/

        /*// Operadores Unarios: Cambio de Signo
        var varA = 7;
        var varB = - varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);
        System.out.println(""); 
        
        // Operador de Negacion 
        var varC = true; // Esta literal por default en Java es de tipo boolean
        var varD = !varC; // Aquí esta inviertiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        System.out.println("");
       
        // Operadores Unarios de Incremento : Preincremento
        var varE = 9; // Se va a modificar su valor
        var varF = ++varE; // Simbolo antes de la variable
        // Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE); // Se incrementa en la unidad
        System.out.println("varF = " + varF); // Va a sumar uno 
        System.out.println("");
        
        // Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++; // Primero vemos el valor de la variable y despues el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        System.out.println("");
        
        // Operadores Unarios de Decremento : Predecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);
        System.out.println("");

        // Postdecremento
        var varK = 8;
        var varL = varK--; // Primero el valor de la variable, despues queda el decremento
        System.out.println("varK = " + varK); // Acá va el decremento en 1
        System.out.println("varL = " + varL);*/
        
        // Operadores de Igualdad y Relacionales
        /*var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        System.out.println("");

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        System.out.println("");

        var cadenaA = "Hello";
        var cadenaB = "Bye bye";
        var cadenaC = cadenaA == cadenaB; // Comparacion de referencia de objetos
        System.out.println("cadenaC = " + cadenaC);
        System.out.println("");
        var fVar = cadenaA.equals(cadenaB); // Comprobamos si el contenido de las cadenas son iguales
        System.out.println("fVar = " + fVar);
        System.out.println("");

        var gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);
        System.out.println("");
        if (aNum % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }
        System.out.println("");*/
        
        // Operador Condicional an && (Solo es verdadero si ambos son verdaderos)
        /*var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("Esta fuera del rango establecido");
        }
        
        // Operador Condicional OR (Solo es verdadero si uno es verdadero y otro es falso, solo es falso si ambos son falsos)
        var diaLibre = false;
        var vacaciones = false;
        if (vacaciones || diaLibre) {
            System.out.println("Papa puede asisitir al juego");
        } else {
            System.out.println("Papa no puede asistir al juego");
        }*/
        
        // Operador Ternario
        /*var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Par" : "Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("z = " + z);
        System.out.println("");
        
        var solucionAritmetica = 4 + 5 * 6 / 3; //
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        var solucionArimetica = (4 + 5) * 6 / 3; // Prioriza los parentesis, por eso cambia el resultado
        System.out.println("solucionArimetica = " + solucionArimetica);
        
        
    }
}