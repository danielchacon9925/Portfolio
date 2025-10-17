#ifndef NEWTON_RAPHSON_METHOD_H
#define NEWTON_RAPHSON_METHOD_H
// Libraries
#include <cmath>
#include <iostream>
#include <iomanip>
#include <stdlib.h>

using namespace std;
///////////////
// Base class//
///////////////
class METHOD{
    public:
        // Declaration: virtual methods
        virtual float Solve_Eq(float& x) = 0;
        virtual float Solve_Dq(float& x) = 0;

        // Print Header method
        void PRINT_HEADER (const string& Eq, const string& Dq) const;

        // Newton_Raphson method
        void Newton_Raphson(float& xi,float& Tolerance);
};
// Daughter_1(D_1)
class D_1 : public METHOD{
    // F(x) = x^3 + 4x^2 -10
    public:
        float Solve_Eq(float& x) override;
        float Solve_Dq(float& x) override;
};
//_______________________________________
// Daughter_2(D_2)
class D_2 : public METHOD{
    // F(x) = x^2 - 1
    public:
        float Solve_Eq(float& x) override;
        float Solve_Dq(float& x) override;
};
//_______________________________________
// Daughter_3(D_3)
class D_3 : public METHOD{
    // F(x) = x^2 + 2x + 1
    public:
        float Solve_Eq(float& x) override;
        float Solve_Dq(float& x) override;
};
//______________________________________________________________________________
#endif