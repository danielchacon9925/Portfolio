// Header file
#include "Newton_Raphson_Method.h"

// ===================================
// BASE CLASS IMPLEMENTATION: METHOD =
// ===================================
void METHOD::PRINT_HEADER(const string& Eq, const string& Dq) const{
    cout << "\n==========================================================================" << endl;
    cout << "  NEWTON-RAPHSON METHOD" << endl;
    cout << "  F(x): " << Eq << endl;
    cout << "  F'(x): " << Dq << endl;
    cout << "==========================================================================" << endl;
    cout << "+----+-------------+-------------+-------------+-------------+------------+" << endl;
    cout << "| i  |      xi     |    f(xi)    |    f'(xi)   |    xi+1     |    xi_xi   |" << endl;
    cout << "+----+-------------+-------------+-------------+-------------+------------+" << endl;
};
//_______________________________________
void METHOD::Newton_Raphson(float& xi,float& Tolerance){
    // Reset value
    float INITIAL_VALUE = xi;
    // Iterator counter
    int Iteration_Counter = 0;
    // Variables initialization
    float xi_xi = 0; 
    float last_xi = 0;
    while (Iteration_Counter != Tolerance){
        float fxi = Solve_Eq(xi);
        float _fxi = Solve_Dq(xi);
        float xi_1 = xi - (fxi / _fxi);
        printf("|%3d |%12.8f |%12.8f |%12.8f |%12.8f |%12.8f|\n", Iteration_Counter, xi, fxi,
            _fxi, xi_1, xi_xi);
        // Update values
        Iteration_Counter++;
        last_xi=xi;
        xi=xi_1;
        xi_xi = abs(xi-last_xi);
        if (xi_xi == 0) {
        printf("+----+-------------+-------------+-------------+-------------+---"
                "---------+\n");
        // Reset in each class
        xi = INITIAL_VALUE;
        break;
        }
    }
};
//______________________________________________________________________________
// =====================================
// DAUGHTER_1(D_1) CLASS IMPLEMENTATION=
// =====================================
// F(x)
float D_1::Solve_Eq(float& x){
    return pow(x,3)+4*pow(x,2)-10;
};
// F'(x)
float D_1::Solve_Dq(float& x){
    return 3*pow(x,2)+8*x;
};
//______________________________________________________________________________
// =====================================
// DAUGHTER_2(D_2) CLASS IMPLEMENTATION=
// =====================================
// F(x)
float D_2::Solve_Eq(float& x){
    return pow(x,2)-1;
};
// F'(x)
float D_2::Solve_Dq(float& x){
    return 2*x;
};
//______________________________________________________________________________
// =====================================
// DAUGHTER_3(D_3) CLASS IMPLEMENTATION=
// =====================================
// F(x)
float D_3::Solve_Eq(float& x){
    return pow(x,2)+2*x+1;
};
// F'(x)
float D_3::Solve_Dq(float& x){
    return 2*x+2;
};
//______________________________________________________________________________
