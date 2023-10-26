// Clase 6

var nombre = 'Jose';
var apellido = 'Montes';

// 1era Concatenación
var nombreCompleto = nombre+' '+apellido;
console.log(nombreCompleto);

// 2da Concatenación
var nombreCompleto2 = 'Mauro'+' '+'Mesas';
console.log(nombreCompleto2);

var juntos = nombre + 219; // Leé de izq a der siguiendo la cadena, leé el número como str
console.log(juntos);
juntos = nombre + 78 + 17; // Aquí se puede diferenciar a través de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

// 3ra Concatenación (usando el operador simplificado)
nombre += apellido;
console.log(nombre);

// Let y Const
let nombre2 = 'Pedro';
console.log(nombre2);

const apellido2 = 'Lepes';
// apellido2 = "Peres"; Una constante NO puede ser modificada
console.log(apellido2);