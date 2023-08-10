#include <iostream>
#include <string.h>
#include <stdio.h>
#include "clases.h"
#include "clases.cpp"


using namespace std;

    void ShowAll(sistema_electrico* main_system)
    {
        main_system -> despliegue_informacion();
    }

    void APP_load ()
        {
        // Se definen las instancias de las plantas generadoras
        planta_generadora* planta_1 = new planta_generadora("Toro Macho");
        planta_generadora* planta_2 = new planta_generadora("Pailas 1");
        planta_generadora* planta_3 = new planta_generadora("Pailas 2");
        planta_generadora* planta_4 = new planta_generadora("Paulias 3");
        planta_generadora* planta_5 = new planta_generadora("Cachí 1");
        planta_generadora* planta_6 = new planta_generadora("Cachí 2");
        planta_generadora* planta_7 = new planta_generadora("Toro Amarillo 4");


        // Lista de tipo planta
        list <planta_generadora *> contenedor_plantas = {planta_1, planta_2, planta_3, planta_4, planta_5, planta_6, planta_7};

        // Se definen las instancias de las unidades generadoras
        unidad_generadora* unidad_1 = new unidad_generadora("gen1", planta_1 -> get_ubicacion_planta(), "100W");
        unidad_generadora* unidad_2 = new unidad_generadora("gen2", planta_1 -> get_ubicacion_planta(), "510W");
        unidad_generadora* unidad_3 = new unidad_generadora("gen3", planta_1 -> get_ubicacion_planta(), "786W");
        unidad_generadora* unidad_4 = new unidad_generadora("gen1", planta_2 -> get_ubicacion_planta(), "100W");
        unidad_generadora* unidad_5 = new unidad_generadora("gen1", planta_3 -> get_ubicacion_planta(), "510W");
        unidad_generadora* unidad_6 = new unidad_generadora("gen1", planta_4 -> get_ubicacion_planta(), "786W");
        unidad_generadora* unidad_7 = new unidad_generadora("gen1", planta_5 -> get_ubicacion_planta(), "100W");
        unidad_generadora* unidad_8 = new unidad_generadora("gen1", planta_6 -> get_ubicacion_planta(), "510W");
        unidad_generadora* unidad_9 = new unidad_generadora("gen1", planta_7 -> get_ubicacion_planta(), "786W");
        unidad_generadora* unidad_10 = new unidad_generadora("gen2", planta_7 -> get_ubicacion_planta(), "1000W");

        // Se agrega el nombre de la fuente a las unidades
        unidad_1->Set_nombre("Hidroeléctrica");
        unidad_2->Set_nombre("Geotérmica");
        unidad_3->Set_nombre("Geotérmica");
        unidad_4->Set_nombre("Geotérmica");
        unidad_5->Set_nombre("Hidroeléctrica");
        unidad_6->Set_nombre("Hidroeléctrica");
        unidad_7->Set_nombre("Solar");
        unidad_8->Set_nombre("Solar");
        unidad_9->Set_nombre("Eólica");
        unidad_10->Set_nombre("Hidroeléctrica");

        // Se agregan las unidades generadoras
        planta_1->add_unidad_generadora(unidad_1);
        planta_1->add_unidad_generadora(unidad_2);
        planta_1->add_unidad_generadora(unidad_3);
        planta_2->add_unidad_generadora(unidad_4);
        planta_3->add_unidad_generadora(unidad_5);
        planta_4->add_unidad_generadora(unidad_6);
        planta_5->add_unidad_generadora(unidad_7);
        planta_6->add_unidad_generadora(unidad_8);
        planta_7->add_unidad_generadora(unidad_9);
        planta_7->add_unidad_generadora(unidad_10);

        // Se agregan las unidades generadoras
        string s1 ="Alto Coen";
        planta_1->Set_nombre_plantageneradora(s1);
        string s2 ="Bajo Coen";
        planta_1->Set_nombre_plantageneradora(s2);
        string s3 = "TangoBravo1";
        planta_1->Set_nombre_plantageneradora(s3);
        string s4 = "TangoBravo2";
        planta_2->Set_nombre_plantageneradora(s4);
        string s5 = "TangoBravo3";
        planta_3->Set_nombre_plantageneradora(s5);
        string s6 = "TangoBravo4";
        planta_4->Set_nombre_plantageneradora(s6);
        string s7 = "TangoBravo4";
        planta_5->Set_nombre_plantageneradora(s7);
        string s8 = "TangoBravo5";
        planta_6->Set_nombre_plantageneradora(s8);
        string s9 = "TangoBravo6";
        planta_7->Set_nombre_plantageneradora(s9);
        string s10 = "TangoBravo7";
        planta_7->Set_nombre_plantageneradora(s10);

        // Instancia del sistema electrico
        sistema_electrico* main_system = new sistema_electrico(contenedor_plantas);
        ShowAll(main_system);
    }

int main(){
   APP_load();

/**
   fuente_generadora F_G;
   F_G.Set_nombre("Eolica");
   cout << "La fuente generadora de energía es : " << F_G.Get_nombre() << endl;
   cout <<"----Utilizando función de desplegar información------"<< endl;
   F_G.despliegue_informacion();

   unidad_generadora U_N;
   U_N.Set_ubicacion_fuente("Parque Eólico Los Santos");
   cout << "Ubicación de fuente por polimorfismo es: " <<U_N.get_ubicacion_fuente()<<endl;
   U_N.Set_nombre_generador("gen1");
   cout << "El nombre de la unidad generadora es: " << U_N.Get_nombre_generador()<< endl;
   U_N.Set_potencia_placa(30);
   cout << "La potencia de la placa es: " << U_N.Get_potencia_placa() << "MW"<<endl;
   cout <<"----Utilizando función de desplegar información------"<< endl;
   U_N.despliegue_informacion();
   //unidad_generadora *unidad1 = new unidad_generadora("gen2",50, "Miravalles");
   //unidad_generadora *unidad2 = new unidad_generadora("gen3",55, "Miravalles1");
   //unidad_generadora *unidad3 = new unidad_generadora("gen4",60, "Miravalles2");

   mostrar_ubicacion mos;
   mos.set_sitio_unidad("Zona de Los Santos");
   cout << "El sitio de la ubicación por polimorfismo se encuentra en: " << mos.imprimir_sitio_ubicacion()<< endl;
      cout <<"----Utilizando función de desplegar información------"<< endl;
   mos.despliegue_informacion();

   planta_generadora planta1("Costa Rica");
   planta1.Set_nombre_plantageneradora("Toro 1");
   planta1.set_ubicacion_planta("En Cartago");
   //planta1.add_unidad_generadora(unidad_generadora* U_N);
   planta1.despliegue_informacion();
*/


return 0;

}