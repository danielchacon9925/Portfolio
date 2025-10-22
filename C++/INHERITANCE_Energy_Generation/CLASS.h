#ifndef CLASS_H
#define CLASS_H

// Libraries
#include <list>
#include <string>
#include <stdio.h>
#include <iostream>


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
            void SET_NAME_GENERATOR(const string& NAME_GENERATOR);
            // POWER
            void SET_PLATE_POWER(const string& PLATE_POWER);
            string GET_PLATE_POWER() const;
            // Show information
            void PRINT_INFO();   
    };//___________________________________________
//__________________________________________________________________________________________
//=============
// BASE CLASS =
//=============
class GENERATOR_PLANT{
    private:
        string _NAME_GENERATOR_PLANT;
        string _UBICATION_PLANT;
        list <GENERATION_UNIT*>_GENERATOR_UNITS;
    public:
            //===========================
            // Constructor & Destructor =
            //===========================
            GENERATOR_PLANT(string UBICATION_PLANT);
            virtual ~GENERATOR_PLANT();
            //====================
            // Getters & Setters =
            //====================
            // Name
            string GET_NAME_GENERATION_PLANT() const;
            void SET_NAME_GENERATION_PLANT(const string& NAME_GENERATION_PLANT);  
            // Location
            string GET_LOCATION_PLANT()const;
            void SET_LOCATION_PLANT(const string& UBICATION_PLANT);     
            // Add UNIT
            void ADD_GENERATION_UNIT(GENERATION_UNIT* UNIT);
            // Show information
            void PRINT_INFO();            
};
//__________________________________________________________________________________________
//=============
// BASE CLASS =
//=============
class ELECTRICAL_SYSTEM{
    private:
        list <GENERATOR_PLANT*> _GENERATION_PLANTS;
    public:
        //===========================
        // Constructor & Destructor =
        //===========================
        ELECTRICAL_SYSTEM(list <GENERATOR_PLANT*> GENERATION_PLANTS);
        virtual ~ELECTRICAL_SYSTEM();
        // Show information
        void PRINT_INFO();   
    };

#endif