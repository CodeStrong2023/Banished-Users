// Clase 3

// Tipos de Datos en JavaScript

// Tipo String(str)
var nombre = 'Mauroooo';
console.log(typeof nombre); //typeof para sabes que tipo de dato es en consola
nombre = ':v';
console.log(typeof nombre);
nombre = 10.2;
console.log(typeof nombre);

// Tipo Numérico
var numero = 1000;
console.log(typeof numero);

// Tipo Objeto
var objeto = {
    nombre : 'Mauro',
    apellido : 'Mesas',
    edad: '21',
}
console.log(typeof objeto);

// Tipo Boolean
var bandera = true;
console.log(typeof bandera);

// Tipo Función
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo Symbol
var simbolo = Symbol("Mi Simbolo");
console.log(simbolo);

// Tipo Clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona)


// Clase 5

// Tipo Undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null = significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);


// Tipo Array y Empty String
var autos = ['Citroen', 'Audi', 'BWM', 'Ford'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z) // Cadena Vacia = Empty String
console.log(typeof z)
