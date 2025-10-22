#include "CLASS.h"


using namespace std;

    void ShowAll(ELECTRICAL_SYSTEM* main_system)
    {
        main_system -> PRINT_INFO();
    }

    void APP_load ()
        {
        // Se definen las instancias de las Plants generadoras
        GENERATOR_PLANT* Plant_1 = new GENERATOR_PLANT("Toro Macho");
        GENERATOR_PLANT* Plant_2 = new GENERATOR_PLANT("Pailas 1");
        GENERATOR_PLANT* Plant_3 = new GENERATOR_PLANT("Pailas 2");



        // Lista de tipo Plant
        list <GENERATOR_PLANT *> contenedor_Plants = {Plant_1, Plant_2, Plant_3};

        // Se definen las instancias de las UNITes generadoras
        GENERATION_UNIT* UNIT_1 = new GENERATION_UNIT("gen1", Plant_1 -> GET_LOCATION_PLANT(), "100W");
        GENERATION_UNIT* UNIT_2 = new GENERATION_UNIT("gen2", Plant_2 -> GET_LOCATION_PLANT(), "510W");
        GENERATION_UNIT* UNIT_3 = new GENERATION_UNIT("gen3", Plant_3 -> GET_LOCATION_PLANT(), "786W");
        
        // Se agrega el nombre de la fuente a las UNITes
        UNIT_1->SET_NAME_GENERATOR("Hidroeléctrica");
        UNIT_2->SET_NAME_GENERATOR("Geotérmica");
        UNIT_3->SET_NAME_GENERATOR("Geotérmica");

        // Se agregan las UNITes generadoras
        Plant_1->ADD_GENERATION_UNIT(UNIT_1);
        Plant_2->ADD_GENERATION_UNIT(UNIT_2);
        Plant_3->ADD_GENERATION_UNIT(UNIT_3);


        // Se agregan las UNITes generadoras
        string s1 ="Alto Coen";
        Plant_1->SET_NAME_GENERATION_PLANT(s1);
        string s2 ="Bajo Coen";
        Plant_2->SET_NAME_GENERATION_PLANT(s2);
        string s3 = "TangoBravo1";
        Plant_3->SET_NAME_GENERATION_PLANT(s3);

        // Instancia del sistema electrico
        ELECTRICAL_SYSTEM* main_system = new ELECTRICAL_SYSTEM(contenedor_Plants);
        ShowAll(main_system);
    }

int main(){
   APP_load();
}