#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include "newton.h"

using namespace std;

int main(){
    float valor;
    float tolerancia;
    string polinomio_1 = "x^3 + 4x^2 -10";
    string polinomio_derivado_1 = "3x^2 + 8x";
    string polinomio_2 = "x^2 - 1";
    string polinomio_derivado_2 = "2x";
    string polinomio_3 = "x^2 + 2x + 1";
    string polinomio_derivado_3 = "2x + 2";

    // Pedimos un valor al usuario
    printf("Introduza valor deseado: \n");
    scanf("%f", &valor);
    //
    printf("Defina la tolerancia: \n");
    scanf("%f", &tolerancia);

    // Para guardar el valor original y no el modificado
    float valor_original = valor;

    // Se llama la primera clase hija para la primera ecuacion
    hija_1 primer_ejemplo;
    //primer_ejemplo.info_metodo(polinomio_1, polinomio_derivado_1);
    primer_ejemplo.newton(valor, tolerancia);
    // Se llama la segunda clase hija para la segunda ecuacion
    hija_2 segundo_ejemplo;
    //segundo_ejemplo.info_metodo(polinomio_2, polinomio_derivado_2);
    segundo_ejemplo.newton(valor, tolerancia);
    // Se llama la tercera clase hija para la tercera ecuacion;
    hija_3 tercer_ejemplo;
    //tercer_ejemplo.info_metodo(polinomio_3, polinomio_derivado_3);
    tercer_ejemplo.newton(valor, tolerancia);
}