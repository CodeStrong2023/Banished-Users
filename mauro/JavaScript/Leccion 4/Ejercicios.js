/*  Ejercicios:
    Ejercicio 1: Calcualar estación del año
    Ejercicio 2: Hora del día
*/

// Ejercicio 1:
let mes = 6;
let estacion;

if (mes == 1 || mes == 2 || mes == 12){
    estacion = 'Verano';
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = 'Otoño';
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = 'Invierno';
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = 'Primavera';
}
else{
    estacion = "Valor Incorrecto";
}

console.log("El valor corresponde a la estación de: " + estacion);


// Ejercicio 2:
/*
6 - 11 mensaje: Buenos dias
12 - 18 mensaje: Buenas tardes
19 - 23 mensaje: Buenas noches
*/

let horaDia = 9;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Buenos Dias!";
}
else if(horaDia >= 12 && horaDia <= 18){
    mensaje = "Buenos Tardes!";
}
else if(horaDia >= 19 && horaDia <= 23){
    mensaje = "Buenos Noches!";
}
else{
    mensaje = "Hora incorrecta";
}
console.log(mensaje);


// Ejercicio 1 Con Switch
switch(mes){ // No solo se pueden utilizar números, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor Incorrecto";
}
console.log("Bienvenido a la estación de: " + estacion);