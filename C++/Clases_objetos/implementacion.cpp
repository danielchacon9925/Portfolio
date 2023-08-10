#include <iostream>
#include <stdlib.h>
#include <cmath>
#include "newton.h"

using namespace std;

newton :: newton(){   
}

float newton::resolverEcuacion(float valor){
    pow(valor, 3) + 4 * pow(valor, 2) - 10;
    return 0;
}

float newton :: resolverDerivada(float valor){
    pow((2 * valor), 2) + 8 * valor;  
    return 0;  
}

void newton :: metodo(double valor){
    float fxi = resolverEcuacion(valor);
    float _fxi = resolverDerivada(valor);
    int iterador = 0;
    float xi_xi = 0;
    float ultimo_xi = 0;
    printf("Método de Newton\n");
    printf("Problema: x^3 + 4x^2 -10\n");
    printf("Derivado: 2x^2 + 8x\n\n\n");
    printf("+----+-------------+-------------+-------------+-------------+-------"
        "-----+\n");
    printf("+ i  |      xi     |    f(xi)    |    f'(xi)   |    xi + 1   |    "
        "xi_xi   |\n");
    printf("+----+-------------+-------------+-------------+-------------+-------"
        "-----+\n");
    while(1){
        float xi_1 = valor - (fxi/_fxi);
        printf("|%3d |%12.8f |%12.8f |%12.8f |%12.8f |%12.8f|\n", iterador, valor, fxi,
           _fxi, xi_1, xi_xi);
        iterador++;
        ultimo_xi = valor;
        valor = xi_1;
        xi_xi = abs(valor - ultimo_xi);
        if (xi_xi == 0) {
            printf("+----+-------------+-------------+-------------+-------------+---"
            "---------+\n");
            break;
        }

    }
}
