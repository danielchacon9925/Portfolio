#include <iostream>
#include "clases.h"
#include <string.h>
#include <stdio.h>

using namespace std;

//Constructor de clase fuente_generadora
fuente_generadora::fuente_generadora(string nombre_fuente, string& ubicacion){
    _nombre_fuente = nombre_fuente;
    _ubicacion = ubicacion;
}
void fuente_generadora::Set_nombre(const string& nombre_fuente){
    _nombre_fuente = nombre_fuente;
}
string fuente_generadora::Get_nombre()const{
    return _nombre_fuente;
}
void fuente_generadora::Set_ubicacion(const string& ubicacion){
    _ubicacion = ubicacion;
}
string fuente_generadora::Get_ubicacion()const{
    return _ubicacion;
}
void fuente_generadora::mostrar_ubicacion(){
    cout << "Ubicacion: " << Get_ubicacion() << endl;
}
void fuente_generadora::despliegue_informacion(){
    cout << "La fuente generadora es: " << Get_nombre() << endl;
    cout << "Ubicación de la unidad: " << Get_ubicacion() << endl;
}//_____________________________________________________

//Constructor de clase unidad_generadora
unidad_generadora::unidad_generadora(string nombre_generador, string ubicacion, string potencia_placa):fuente_generadora("", ubicacion){
    _nombre_generador= nombre_generador;
    _potencia_placa = potencia_placa;
}
string unidad_generadora::Get_nombre_generador()const{
    return _nombre_generador;
}
void unidad_generadora::Set_nombre_generador(const string& nombre_generador){
    _nombre_generador = nombre_generador;
}
void unidad_generadora::Set_potencia_placa(const string& potencia_placa){
    _potencia_placa = potencia_placa;
}
string unidad_generadora::Get_potencia_placa()const{
    return _potencia_placa;
}
//Método polimórfico para definir ubicación de fuente
//void unidad_generadora:: Set_ubicacion_fuente(string ubf){ 
//    return Set_ubicacion(ubf);    
//}//Método polimórfico para imprimir ubicación de fuente
//string unidad_generadora::get_ubicacion_fuente(){
//    return ubicacion;   
//}
void unidad_generadora::despliegue_informacion(){
    cout << "El nombre de la unidad generadora es:  " << _nombre_generador << endl;
    cout << "La potencia de la placa es: " << _potencia_placa << "MW" << endl;
}
//void unidad_generadora::lista(){
//    list<unidad_generadora*>unidadA;
//    unidadA.push_front(unidadA);
//}
//________________________________________

/**
//Constructor de clase de mostrar ubicación
mostrar_ubicacion::mostrar_ubicacion(){

}//Método polimórfico para obtener el sitio_ubicación
string mostrar_ubicacion::imprimir_sitio_ubicacion(){
    return sitio_ubicacion;
}//Método polimórifco para definir el sitio_ubicación
void mostrar_ubicacion::set_sitio_unidad(string ubi){
    set_sitio_ubicacion(ubi);
}
void mostrar_ubicacion::despliegue_informacion(){
    cout << "La ubicación es: " << sitio_ubicacion << endl;
}
//___________________________________________
**/

//Constructor de clase planta_generadora
planta_generadora::planta_generadora(string ubicacion_planta){
    _ubicacion_planta = ubicacion_planta;
}
void planta_generadora::Set_nombre_plantageneradora(string & nombre_de_planta){
    nombre_planta_generadora = nombre_de_planta;
}
string planta_generadora::Get_nombre_plantageneradora()const{
    return nombre_planta_generadora;
}
void planta_generadora::set_ubicacion_planta(string & ubicacion_planta){
    _ubicacion_planta = ubicacion_planta;
}
string planta_generadora::get_ubicacion_planta()const{
    return _ubicacion_planta;
}
void planta_generadora::add_unidad_generadora(unidad_generadora* unidad){
     if(_unidades_generadoras.size()<= 3)
        {
            _unidades_generadoras.push_back(unidad);
        }
    else
    {
        cout << "No se pueden añadir más unidades generadoras a la lista" << endl;
    }
}
void planta_generadora::despliegue_informacion(){
    cout << "El nombre de la planta es: " << nombre_planta_generadora << endl;
    cout << "La ubicación de la planta es: " << _ubicacion_planta << endl;
    cout << "Información de unidades generadoras: " << endl;
    for(unidad_generadora* unidad:_unidades_generadoras){
        unidad->despliegue_informacion();
    }
}//__________________________________________________________________

//Constructor para sistema eléctrico
sistema_electrico::sistema_electrico(list <planta_generadora*> plantas_generadoras){
    _plantas_generadoras = plantas_generadoras;
}
void sistema_electrico::despliegue_informacion(){
    for(planta_generadora* planta:_plantas_generadoras){
        planta->despliegue_informacion();
    }
}//__________________________________________________________

fuente_generadora::~fuente_generadora(){
    //Destruye y libera memoria
}
unidad_generadora::~unidad_generadora(){
    //Destruye y libera memoria
}
/**
mostrar_ubicacion::~mostrar_ubicacion(){
    //Destruye y libera memoria
}
**/
planta_generadora::~planta_generadora(){
    //Destruye y libera memoria
}