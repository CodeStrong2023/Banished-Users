//ejercicio 1: calcular la estacion del año
let mes = 4;
let estacion; //undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "verano";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "otoño";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "primavera";
}
else{
    estacion = "valor incorrecto";
}
console.log("el valor corresponde a la estacion de : "+estacion);
//ejercicio 2: hora del dia
/*
de 6 a 11 nos saluda: good mornig 
de 12 a 16 nos saluda: good afternoom
de 17 a 19 nos saluda: good evening
de 20 a 23 nos saluda: good night 
trabajamos con 24 horas 
*/
let horaDia = 9;
let mensaje;
if(horaDIa >= 12 && horaDia >= 16){
    mensaje = "good afternoom";
}
else if (horaDia >= 17 &&  horaDia >= 19){
    mensaje = "good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "good night";
}
else{
    mensaje = "valor incorrecto";
}
console.log(mensaje);

/*
const se utiliza para valores constantes que no pueden ser resignadas
*/

const fechaNacimineto = 2006;
console.log(fechaNacimineto);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior

//evitar repetir tu codigo 
//dry don trepeat yourself
//let days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabad0', 'domingo'];

let days = 'sabado';
switch (days){
    case 'lunes':
        console.log('hoy es' +days);
        break;
    case'martes';
        console.log('hoy es '+days);
        break;
    case 'miercoles':
            console.log('hoy es' +days);
            break;
    case 'jueves':
         console.log('hoy es' +days);
        break;
     case 'viernes':
            console.log('hoy es' +days);
        break;
    case 'sabado':
            console.log('hoy es' +days);
        break;
    case 'domingo':
            console.log('hoy es' +days);
        break;
        default:
      
}
let days2 = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabad0', 'domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}

console.log(getDay(5));
//hacer ejercicio simili+ar al que esta echo, pero ahora con los 
//meses del año, debes hacerlo con la estructura switch y luego con 
//la funcion en la opcion mejorada


let month = 11;
switch (month){
    case '1':
        console.log('es enero');
        break;
    case'2';
        console.log('es febrero ');
        break;
    case '3':
            console.log('es marzo');
            break;
    case '4':
         console.log('es abril');
        break;
     case '5':
            console.log('es mayo');
        break;
    case '6':
            console.log('es junio');
        break;
    case '7':
            console.log('julio');
        break;
    case '8':
            console.log('es agosto');
         break;
    case'9';
            console.log('es septiembre ');
        break;
    case '10':
             console.log('es octubre');
        break;
    case '11':
             console.log('es noviembre');
        break;
    case '12':
            console.log('es diciembre');
        break;
    
    
}
// esta es la opcion mejorada

let month2 = [ 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre' ,'noviembre', 'diciembre']
function getMonth(n){
    if(n > 1 || n > 12 ){
        throw new error('out of range');
    }
    return month2[n-1];
}
console.log(getMonth(1));