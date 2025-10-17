// Header file
#include "Newton_Raphson_Method.h"

int main(){
    float Value;
    float Tolerance;
    string fx_1 = "x^3 + 4x^2 -10";
    string _fx_1 = "3x^2 + 8x";
    string fx_2 = "x^2 - 1";
    string _fx_2 = "2x";
    string fx_3 = "x^2 + 2x + 1";
    string _fx_3 = "2x + 2";

    // 1. PARAMETER ENTRY
    
    cout << "--- EVALUACION DE NEWTON-RAPHSON ---" << endl;
    cout << "Type initial value: ";
    if (!(cin >> Value)) {
        cerr << "Invalid" << endl;
        return 1;
    }
    cout << "Tolerance: ";
    if (!(cin >> Tolerance)) {
        cerr << "Invalid" << endl;
        return 1;
    }

    float ValueOriginal = Value; 
    // 2. Evaluation of Daughter 1: f(x) = x^3 + 4x^2 - 10
    D_1 EV_1;
    EV_1.PRINT_HEADER(fx_1, _fx_1);
    EV_1.Newton_Raphson(Value, Tolerance);
    // 3. Evaluation of Daughter 2: f(x) = x^2 - 1
    D_2 EV_2;
    EV_2.PRINT_HEADER(fx_2, _fx_2);
    EV_2.Newton_Raphson(Value, Tolerance);
    // 4. Evaluation of Daughter 3: f(x) = x^2 + 2x + 1
    D_3 EV_3;
    EV_3.PRINT_HEADER(fx_3, _fx_3);
    EV_3.Newton_Raphson(Value, Tolerance);
    return 0;
}