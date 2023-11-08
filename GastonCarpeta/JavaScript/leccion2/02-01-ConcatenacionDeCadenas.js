var nombre = 'jose';
var apellido = ' montes';
var nombreCompleto = nombre+' '+apellido;// primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'ariel'+' '+'betancud';//segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //lee de izquierda a der siguiendo la cadena lee el numero como str
console
console.log(juntos);
juntos = nombre +(78 + 17);// aqui se pued diferenciar a traves de los parentesis 
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;//tercera concatenacion usando el operador simplificado
console.log(nombre);

// hoy ya no se usa var, se utiliza let y const
let nombre2 = "pedro";
console.log(nombre);

const apellido2 = "lepes";
//apellido2 = "peres"; // una constante no puede ser modificada
console.log(apellido2)