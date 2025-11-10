/*  Declaración de función y llamada de una función  */

console.log("Declaración de función");

function saludar(){
    console.log("Hola Mundo Bienvenido a la clase de Javascript");
}

saludar()

function sumar(a, b){
    let resultado = a + b;
    console.log(`La suma de ${a} y ${b}  es ${resultado}`);
}

sumar (5,10)

function presentar(nombre, edad){
    let mensaje = `Hola mi nombre es ${nombre} y tengo ${edad} años`;
    console.log(mensaje);
}

presentar("Paula", 38);