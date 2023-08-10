#include <cmath>
#include<iostream>
using namespace std;

class metodo_numerico{
    public:

        //metodo_numerico(); //Constructor de clase 
        virtual float resolverEcuacion (float& valor) = 0;  //Método
        virtual float resolverDerivada (float& valor) = 0;  //Método
        float newton(float& valor);
        float tolerancia;


       /** void info_metodo(string polinomio, string polinomio_derivado){
            printf("Método de Newton\n");
            printf("Problema: %s\n", polinomio);
            printf("Derivado: %s\n\n\n", polinomio_derivado);
            printf("+----+-------------+-------------+-------------+-------------+-------"
                "-----+\n");
            printf("+ i  |      xi     |    f(xi)    |    f'(xi)   |    xi + 1   |    "
                "xi_xi   |\n");
            printf("+----+-------------+-------------+-------------+-------------+-------"
                "-----+\n");
        } **/

        void newton (float& valor, float& tolerancia){

            float xi_1;
            float xi_xi;
            int iterador = 0;
            while (iterador != tolerancia){
            // Llamamos a las funciones que resuelven las ecuaciones
            float ultimo_xi;
            float xi_xi;
            float fxi = resolverEcuacion(valor);
            float fxi_derivada = resolverDerivada(valor);
            printf("Método de Newton\n");
            printf("Problema: ");
            printf("Derivado: ");
            printf("+----+-------------+-------------+-------------+-------------+-------"
                "-----+\n");
            printf("+ i  |      xi     |    f(xi)    |    f'(xi)   |    xi + 1   |    "
                "xi_xi   |\n");
            printf("+----+-------------+-------------+-------------+-------------+-------"
                "-----+\n");
            // Se aplica el metodo de Newton para resolver las ecuaciones
            xi_1 = valor - (fxi / fxi_derivada);
            printf("|%3d |%12.8f |%12.8f |%12.8f |%12.8f |%12.8f|\n", iterador, valor, fxi,fxi_derivada, xi_1, xi_xi);
            iterador++;
            ultimo_xi = valor;
            valor = xi_1;
            xi_xi = abs(valor - ultimo_xi);
            if (xi_xi == 0) {
                printf("+----+-------------+-------------+-------------+-------------+---"
                    "---------+\n");
            } 
        }
        }

};

class hija_1 : public metodo_numerico{
    //x^3 + 4x^2 -10
    public:
        float resolverEcuacion(float& valor){
            
            return pow(valor, 3) + 4 * pow(valor, 2) - 10;;
        }
        float resolverDerivada(float& valor){
             
            return pow((3 * valor), 2) + 8 * valor;
        }
/**            float newton(float& valor){
            float xi_1 = valor - (resolverEcuacion(valor)/resolverDerivada(valor));
            return xi_1;
        } **/
};

class hija_2 : public metodo_numerico{
    //x^2 - 1
    public:
        float resolverEcuacion(float& valor){
             
            return pow(valor, 2) -1;
        }
        float resolverDerivada(float& valor){
            
            return pow((valor), 2);
        }
/**        float newton(float& valor){
            float xi_1 = valor - (resolverEcuacion(valor)/resolverDerivada(valor));
            return xi_1;
        } **/


};

class hija_3 : public metodo_numerico{
    //x^2 + 2x + 1
    public:
        float resolverEcuacion(float& valor){
            
            return pow(valor, 2) + 2*valor +1 ;
        }
        float resolverDerivada(float& valor){
            
            return pow((valor), 2) + 1;
        }
/**        float newton(float& valor){
            float xi_1 = valor - (resolverEcuacion(valor)/resolverDerivada(valor));
            return xi_1;
        }   **/


};
