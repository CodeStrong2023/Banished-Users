// ejercicio para encontrar numeros pares e impares
let parInpar = 7;
if(parInpar % 2 == 0){
    console.log("es un numero PAR;")
}
else{
    console.log("es un numero IMPAR");
}

// ejercicio: es mayot de edad
let edad = 20, adulto = 18;
if(edad >= adulto){
	console.log('usted es una persona adulta');
}
else{
	console.log('usted es una persona menor de edad')
}

//ejercicio: dentor de un rango
let dentroRango = 5; // aqui vamos a ir cambiando el valor 
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('esta dentro del rango establecido')
}
else{
    console.log('esta fuera del rango establecido')
}

//operador ternario
let resultado2 = 3 > 2 ? "verdadero " : "falso";
console.log(resultado2) 
let numero = 9;
resultado2 = numero % 2 == 0 ? "es un numero PAR " : "es un numero IMPAR";
console.log(resultado2)

//convertir string a number
let miNumero = "10"; //es una cadena
console.log(typeof miNumero);
let edad2 = number(miNumero)// esta es una funcion
console.log(typeof edad2);
if(isNaN(edad2)){
    console.log("esta variable no contiene solo numeros")
}
else{


if(edad >= 18){
    console.log("puede votar");
}
else{
    console.log("muy joven para votar");
    }
}
//operador ternario
let resultado3 = edad2 >? 18 ? " puede votar": "muy joven para votar";
console.log(resultado3);

//funcion isNaN