// creamos un nuevo archivo
/*
empezamos a ver los comentarios ej JavaScript
*/
//tipo string
var nombre ='ariel';
console.log(typeof nombre); String
nombre = 7;
console.log(typeof nombre); Number
nombre = 12.3;
console.log(typeof nombre); number
// tipo numerico
var numero = 3000; 
console.log(numero);
//tipo objet
var objeto = {
    nombre : "ariel"
    apellido : "betancud"
    telefono : "2604634854"
}

console.log(typeof objeto); Object

//tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = symbol("mi simbolo");
console.log(simbolo);

//tipo de dato de clase
class Persona{
	constructor(nombre,apellido){
		this.nombre = nombre;
		this.apellido = apellido;
	}
}

console.log(typeof Persona);

//tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor 
var y = null; //null no es un tipo de dato, pero su origen es object
console.log(typeof y);

//tipo de dato array y empty string
var autos = ['citroen', 'audi', 'bmw'];
console.log(autos);['citroen', 'audi', 'bmw']
console.log(typeof autos); // preguntamos que tipo de dato es:    Object

var z;
console.log(z);//esto se refiere a que es una cadena vacia:   [empty String]
console.log(typeof z); String