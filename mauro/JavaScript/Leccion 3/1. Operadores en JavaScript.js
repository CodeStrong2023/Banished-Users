// Clase 7

// Ejercicio 1: Para encontrar números Pares e Impares

let parImpar = 30;

if (parImpar % 2 == 0){
    console.log('Es un número PAR');
}
else{
    console.log('Es un número IMPAR');
}

// Ejercicio 2: Es Mayor de Edad

let edad = 20, adulto = 18;
if(edad += adulto){
    console.log('Usted es una persona adulta');
}
else{
    console.log('Usted es una persona menor de edad');
}


// Clase 8
// Ejercicio 3: Dentro de un Rango

let dentroRango = 5;
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Estas dentro del rango establecido');
}
else{
    console.log('Estas fuera del rango establecido');
}


// Clase 9
// Ejercicio 4: Si el padre puede asistir al juego de su hijo

let vacaciones = false, diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log('El padre puede asistir al juego de su hijo');
}
else{
    console.log('El padre NO puede asistir al juego de su hijo');
}


// Operador Ternario
let resultado2 = 3 > 2? 'Verdadero' : 'Falso';
console.log(resultado2);

// Ejercicio 4: Par o Impar (Con Operador Ternario)

let numero = 9;
resultado2 = numero % 2 == 0? 'Es un número PAR' : 'Es un número IMPAR';
console.log(resultado2);

// Convertir String a Number

let miNum = '20'; // Es una cadena
console.log(typeof miNum);
let edad2 = Number(miNum); // Esta es una función (Number)
console.log(typeof edad2);

// Función isNaN
if(isNaN(edad2)){ // isNaN = is Not a Number (boolean)
    console.log('La variable no contiene solo numeros')
}
else{
    if (edad2 >= 18){
        console.log('Puede votar');
    }
    else{
        console.log('No puede votar');
    }
}

// Operador Ternario**
let resultado3 = edad2 >= 18? 'Puede votar' : 'No puede votar';
console.log(resultado3);
