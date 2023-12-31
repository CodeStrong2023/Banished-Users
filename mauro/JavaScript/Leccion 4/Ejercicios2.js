// Hacer un ejercicio similar al que esta hecho, pero ahora con los
// meses del año, debes hacerlo con la estructura switch y luego con
// la función en la opción mejorada

let months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

function getMonth(n) {
    if (n < 1 || n > 12) {
        throw new Error('Número fuera de rango');
    }
    return months[n - 1];
}

let currentMonth = 7;

switch (getMonth(currentMonth)) {
    case 'Enero':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Febrero':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Marzo':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Abril':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Mayo':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Junio':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Julio':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Agosto':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Septiembre':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Octubre':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Noviembre':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    case 'Diciembre':
        console.log('Estamos en ' + getMonth(currentMonth));
        break;
    default:
        console.log('Número de mes no válido');
        break;
}


// Version Mejorada

let months2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

function getMonth2(n) {
    if (n < 1 || n > 12) {
        throw new Error('out of range');
    }
    return months2[n - 1];
}

let currentMonth2 = 5;

console.log(getMonth(1));