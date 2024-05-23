from sympy.solvers import solve
from sympy import Symbol
import math
import random
from math import log2, floor


# Clase para los bloques de memoria en cache
class Bloque:
    def __init__(self):
        self.tag = None  # Tag que almacena el bloque
        self.edad = 0  # Edad inicia como 0.


class cache:
    def __init__(self, cache_capacity, cache_assoc, block_size, repl_policy):
        self.c_capacity = cache_capacity
        self.c_blocksize = block_size
        self.rep_policy = repl_policy
        # Número de sets según asociatividad
        self.numSets = int(
            math.ceil(((cache_capacity*1024)/block_size)/cache_assoc))
        # Número de ways
        self.associativity = cache_assoc
        # Bits de offset
        self.offsetBits = int(math.ceil(math.log(block_size, 2)))
        # Bits de index
        self.indexBits = int(math.ceil(math.log(self.numSets, 2)))
        # Se inicializa memoria vacía
        self.memoria = []

        # ** Cantidad de bloques de memoria **
        # Se inicia adjuntando bloques de memoria vacía según set
        for i in range(self.numSets):
            vacio = []
            self.memoria.append(vacio)
        # Se adjuntan j bloques de memoria según set
        for i in range(self.numSets):
            for j in range(cache_assoc):
                self.memoria[i].append(Bloque())

        # Escriba aquí el init de la clase
        self.total_reads = 0
        self.total_read_misses = 0
        self.total_writes = 0
        self.total_write_misses = 0

    # Método para reemplazar bloques en memoria cache

    def replace(self, acceso, index, tag, repl_policy):

        #################
        #   Result= HIT #
        #################
        # Se plantea únicamente el caso cuando se produce un HIT

        for i in range(self.associativity):
            # Si encuentra el TAG, se marca nuevo ingreso (edad=0)
            if self.memoria[index][i].tag == tag:
                self.memoria[index][i].edad = 0
                # Se incrementan los acceso
                if acceso == "w":
                    self.total_writes += 1
                elif acceso == "r":
                    self.total_reads += 1
                return
            #  Si los TAGs no coinciden, es porque se está produciendo un MISS.

        ####################
        #   Replace policy #
        ####################
        # Al no coincidir TAG, se debe utilizar política de reemplazo
        #  ** LRU **
        if repl_policy == "l":
            # Valor de bloque más antiguo
            mayor = 0
            # ¿Cuantos ways? La asociatividad lo indica
            # Se recorren los ways
            for i in range(self.associativity):
                if self.memoria[index][i].edad > mayor:
                    # El valor del mayor  se actualiza según edades de ways
                    mayor = self.memoria[index][i].edad
            # Se recorren los ways
            # ** Reemplazo **
            for i in range(self.associativity):
                # Busca en memoria el bloque mayor, le cambia el TAG y marca nuevo acceso (edad=0)
                if self.memoria[index][i].edad == mayor:
                    self.memoria[index][i].tag = tag
                    self.memoria[index][i].edad = 0
                    # Se incrementan los accesos y misses
                    if acceso == "w":
                        self.total_writes += 1
                        self.total_write_misses += 1
                    elif acceso == "r":
                        self.total_reads += 1
                        self.total_read_misses += 1
                    # Termina el método una vez que se reemplaza un bloque.
                    return
        # ** Random replace **
        if repl_policy == "r":
            # Ramdom way
            random_way = random.randint(0, self.associativity-1)
            # Cambio de TAG y registra ingreso nuevo (edad=0)
            self.memoria[index][random_way].tag = tag
            self.memoria[index][random_way].edad = 0
            # Se incrementan los accesos y misses
            if acceso == "w":
                self.total_writes += 1
                self.total_write_misses += 1
            elif acceso == "r":
                self.total_reads += 1
                self.total_read_misses += 1
            return

    # Método para actualizar las edades de los bloques de un set en la memoria cache
    def update(self, tag, index):
        # Se recorren ways. Si bloque de mem no tiene tag actual y no es el más viejo:
        #   se incrementa la edad.
        for i in range(self.associativity):  # Se recorren los ways
            if ((self.memoria[index][i].tag != tag)):
                self.memoria[index][i].edad += 1
        return

    def print_info(self):
        print("Parámetros del caché:")
        print("\tCapacidad:\t\t\t"+str(self.c_capacity)+"kB")
        print("\tAssociatividad:\t\t\t"+str(self.associativity))
        print("\tTamaño de Bloque:\t\t\t"+str(self.c_blocksize*1024)+"B")
        print("\tPolítica de Reemplazo:\t\t\t" +
              str(self.rep_policy))
        if (self.rep_policy == "l"):
            print("\tPolítica de Reemplazo:\t\t\tLRU")
        else:
            print("\tPolítica de Reemplazo:\t\t\tAleatoria")

    def print_stats(self):
        total_misses = self.total_read_misses+self.total_write_misses
        total_access = self.total_reads+self.total_writes
        print("Resultados de la simulación")
        miss_rate = (100.0*total_misses) / total_access
        miss_rate = "{:.3f}".format(miss_rate)
        read_miss_rate = (100.0*self.total_read_misses) / self.total_reads
        read_miss_rate = "{:.3f}".format(read_miss_rate)
        write_miss_rate = (100.0*self.total_write_misses) / self.total_writes
        write_miss_rate = "{:.3f}".format(write_miss_rate)
        result_str = "Total_misses "+str(total_misses)+","+"Total_miss_rate "+miss_rate + \
            "%,"+"Total_read_misses "+str(self.total_read_misses)+","
        result_str += "Total_read_miss_rate "+read_miss_rate+"%," + \
            "Total_write_misses " + \
            str(self.total_write_misses)+"," + \
            "Total_write_miss_rate "+write_miss_rate+"%"
        print(result_str)
