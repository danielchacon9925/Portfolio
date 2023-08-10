#ifndef FUENTE_GENERADORA_H
#define FUENTE_GENERADORA_H

#include <string.h>
#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;

class fuente_generadora
{
         
    protected:
        string  _ubicacion;
        string  _nombre_fuente;
    public:
    fuente_generadora(string nombre_fuente, string& ubicacion);    //Constructor de clase
    virtual ~fuente_generadora();   //Destructor de clase
    string  Get_nombre()const;
    void    Set_nombre(const string& nombre_fuente);
    void    Set_ubicacion(const string& ubicacion);
    string  Get_ubicacion()const;
    virtual void mostrar_ubicacion();
    void    despliegue_informacion();
    
};//_______________________________________________

class unidad_generadora: public fuente_generadora{
    private:
        string _nombre_generador;
        string _potencia_placa;
    public:
        unidad_generadora(string nombre_generador, string ubicacion, string potencia_placa);
        virtual ~unidad_generadora();
        string  Get_nombre_generador()const;
        void    Set_nombre_generador(const string& nombre_generador);
        void    Set_potencia_placa(const string& potencia_placa);
        string     Get_potencia_placa()const;
        void    despliegue_informacion();


};//_______________________________________________

/**
class mostrar_ubicacion: protected unidad_generadora{
    public:
        mostrar_ubicacion();
        virtual ~mostrar_ubicacion();
        string imprimir_sitio_ubicacion();
        void set_sitio_unidad(string ub);
        void despliegue_informacion();
        //void Set_ubicacion_poli(string poliu);
        //string imprimir_poli_ubicacion();
        
};//_______________________________________________
**/

class planta_generadora{
    private:
        string nombre_planta_generadora;
        string _ubicacion_planta;
        list <unidad_generadora*>_unidades_generadoras;
    public:
        planta_generadora(string ubicacion_planta);
        virtual ~planta_generadora();

        void Set_nombre_plantageneradora(string & nombre_de_planta);
        string Get_nombre_plantageneradora()const;

        void set_ubicacion_planta(string & ubicacion_planta);
        string get_ubicacion_planta()const;

        void add_unidad_generadora(unidad_generadora* unidad);
        void despliegue_informacion();

};//_________________________________________________________

class sistema_electrico{
    private:
        list <planta_generadora*>_plantas_generadoras;
    public:
        sistema_electrico(list<planta_generadora*> plantas_generadoras);
        void despliegue_informacion();
};

#endif




