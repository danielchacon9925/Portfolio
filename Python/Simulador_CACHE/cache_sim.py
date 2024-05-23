from optparse import OptionParser
import gzip
from cache import *

parser = OptionParser()
parser.add_option("-s", dest="cache_capacity")
parser.add_option("-a", dest="cache_assoc")
parser.add_option("-b", dest="block_size")
parser.add_option("-r", dest="repl_policy")
parser.add_option("-t", dest="TRACE_FILE")

(options, args) = parser.parse_args()

# Se crea caché
cache = cache(int(options.cache_capacity), int(options.cache_assoc),
              int(options.block_size), str(options.repl_policy))

i = 0
with gzip.open(options.TRACE_FILE, 'rt') as trace_fh:
    for line in trace_fh:
        line = line.rstrip()
        access, direction = line.split(" ")
        #################################
        # Direction, offset, tag, index #
        #################################
        # Hex to decimal 
        direction = int(direction, 16) 
        # Offset son los m LSB
        offset = int(direction % (2**cache.offsetBits)) 
        # Index son los n LSB quitando los bits de offset
        index = int((direction >> cache.offsetBits) % (2**cache.indexBits))
        # TAG bits restantes 
        tag = int(direction >> (cache.indexBits + cache.offsetBits)) 
        # Replace
        cache.replace(access, index, tag, options.repl_policy)
        # Mem update
        cache.update(tag, index)
        # i+=1
        # if i == 25:
        #    break
cache.print_info()
cache.print_stats()
