#ifndef CLASS_H
#define CLASS_H

// Libraries
#include <list>
#include <string>
#include <stdio.h>
#include <list>

using namespace std;

//=============
// BASE CLASS =
//=============

class GENERATOR_SOURCE{
    protected:
        string _UBICATION;
        string _NAME_SOURCE;
    public:
        //===========================
        // Constructor & Destructor =
        //===========================
        GENERATOR_SOURCE(const string& NAME_SOURCE, const string& UBICATION);
        virtual ~GENERATOR_SOURCE();
        //====================
        // Getters & Setters =
        //====================
        // Name
        string  GET_NAME()const;
        void SET_NAME(const string& NAME_SOURCE);
        // Ubication
        string  GET_UBICATION()const;
        void SET_UBICATION(const string& UBICATION);    
        virtual void SHOW_UBICATION();
        // Show information
        void PRINT_INFO();    
};//_______________________________________________
    class GENERATION_UNIT: public GENERATOR_SOURCE{
        private:
            string _NAME_GENERATOR;
            string _PLATE_POWER;
        public:
            //===========================
            // Constructor & Destructor =
            //===========================
            GENERATION_UNIT(const string& NAME_GENERATOR, const string& UBICATION, const string& PLATE_POWER);
            virtual ~GENERATION_UNIT();
            //====================
            // Getters & Setters =
            //====================
            // Name
            string GET_NAME_GENERATOR() const;
            void SET_NAME_GENERATOR(const string& NAME_GENERATOR) const;
            // POWER
            void SET_PLATE_POWER(const string& PLATE_POWER);
            string GET_PLATE_POWER() const;
            // Show information
            void PRINT_INFO();   
    };//___________________________________________


#endif