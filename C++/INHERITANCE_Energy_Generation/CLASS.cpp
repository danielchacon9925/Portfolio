#include"CLASS.h"

//================
//= POLYMORPHISM =
//================

// BASE CLASS 1
//===========================
// Constructor & Destructor =
//===========================
GENERATOR_SOURCE::GENERATOR_SOURCE(const string& NAME_SOURCE, const string& UBICATION){
    // Name 
    _NAME_SOURCE = NAME_SOURCE;
    // Location
    _UBICATION = UBICATION;
};
//===========================================
// Getters & Setters for private attributes =
//===========================================
// Name
string GENERATOR_SOURCE :: GET_NAME() const{
    return _NAME_SOURCE;
};
void GENERATOR_SOURCE :: SET_NAME(const string& NAME_SOURCE){
    _NAME_SOURCE = NAME_SOURCE;
};
// Location
string GENERATOR_SOURCE :: GET_UBICATION() const{
    return _UBICATION;
};
void GENERATOR_SOURCE :: SET_UBICATION(const string& UBICATION){
    _UBICATION = UBICATION;
};
// SHOW LOCATION
void GENERATOR_SOURCE :: SHOW_UBICATION(){
    cout << "Location"<< GET_UBICATION() << endl;
};
// PRINT INFO
void GENERATOR_SOURCE :: PRINT_INFO(){
    cout <<"The generation unit is: " << GET_NAME() << endl;
    cout <<"The location of the generation unit is: " << GET_NAME() << endl;
};
//_______________________________________________
// DAUGHTER CLASS 
//===========================
// Constructor & Destructor =
//===========================
GENERATION_UNIT::GENERATION_UNIT(const string& NAME_GENERATOR, const string& UBICATION, const string& PLATE_POWER):GENERATOR_SOURCE("",UBICATION){
    // Name 
    _NAME_GENERATOR = NAME_GENERATOR;
    // Location
    _UBICATION = UBICATION;
};
//===========================================
// Getters & Setters for private attributes =
//===========================================
// Name
string GENERATION_UNIT::GET_NAME_GENERATOR() const{
    return _NAME_GENERATOR;
};
void GENERATION_UNIT::SET_NAME_GENERATOR(const string& NAME_GENERATOR){
    _NAME_GENERATOR = NAME_GENERATOR;
};
// Power
string GENERATION_UNIT::GET_PLATE_POWER() const{
    return _PLATE_POWER;
};
void GENERATION_UNIT::SET_PLATE_POWER(const string& PLATE_POWER){
    _PLATE_POWER = PLATE_POWER;
};
// PRINT INFO
void GENERATION_UNIT::PRINT_INFO(){
    cout << "The name of the generator unit is:  " << GET_NAME_GENERATOR()<< endl;
    cout << "The power plate is: " << GET_PLATE_POWER() << "MW" << endl;
}
//__________________________________________________________________________________________
// BASE CLASS 2
//===========================
// Constructor & Destructor =
//===========================
GENERATOR_PLANT::GENERATOR_PLANT(string UBICATION_PLANT){
    _UBICATION_PLANT = UBICATION_PLANT;
}
//===========================================
// Getters & Setters for private attributes =
//===========================================
// Name
string GENERATOR_PLANT::GET_NAME_GENERATION_PLANT()const{
    return _NAME_GENERATOR_PLANT;
}
void GENERATOR_PLANT::SET_NAME_GENERATION_PLANT(const string& NAME_GENERATION_PLANT){
    _NAME_GENERATOR_PLANT = NAME_GENERATION_PLANT;
};
// Location
string GENERATOR_PLANT::GET_LOCATION_PLANT()const{
    return _UBICATION_PLANT;
};
void GENERATOR_PLANT::SET_LOCATION_PLANT(const string& UBICATION_PLANT){
    _UBICATION_PLANT = UBICATION_PLANT;
};
// ADD TO LIST
void GENERATOR_PLANT::ADD_GENERATION_UNIT(GENERATION_UNIT* UNIT){
     if(_GENERATOR_UNITS.size()<= 3)
        {
            _GENERATOR_UNITS.push_back(UNIT);
        }
    else
    {
        cout << "Unable to add more UNITS" << endl;
    }
};
void GENERATOR_PLANT::PRINT_INFO(){
    cout << "The name of the plant is: " << GET_NAME_GENERATION_PLANT() << endl;
    cout << "The location of the plant is: " << GET_LOCATION_PLANT() << endl;
    cout << "GENERATION UNITS INFO: " << endl;
    for(GENERATION_UNIT* UNIT:_GENERATOR_UNITS){
        UNIT->PRINT_INFO();
    }
};
//__________________________________________________________________________________________
// BASE CLASS 3
//===========================
// Constructor & Destructor =
//===========================
ELECTRICAL_SYSTEM::ELECTRICAL_SYSTEM(list <GENERATOR_PLANT*> GENERATION_PLANTS){
    _GENERATION_PLANTS = GENERATION_PLANTS;
}
void ELECTRICAL_SYSTEM::PRINT_INFO(){
    for(GENERATOR_PLANT* PLANT:_GENERATION_PLANTS){
        PLANT->PRINT_INFO();
    }
};//__________________________________________________________________________________________
//==============
// Destructors =
//==============
GENERATOR_SOURCE::~GENERATOR_SOURCE(){
    //Destruye y libera memoria
};
GENERATION_UNIT::~GENERATION_UNIT(){
    //Destruye y libera memoria
};
GENERATOR_PLANT::~GENERATOR_PLANT(){
    //Destruye y libera memoria
};
ELECTRICAL_SYSTEM::~ELECTRICAL_SYSTEM(){
    //Destruye y libera memoria
};