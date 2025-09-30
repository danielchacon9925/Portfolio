// Define a circular buffer

#define BUFF_SIZE 8

char buffer[BUFF_SIZE];
int head = 0, tail = 0, count = 0;

int buffer_put(char c){
    // FULL BUFF
    if (count == BUFF_SIZE) return -1;
    // Data on first position
    buffer[head] = c;
    // Head updated
    // % Core of circular buffer: when reaches end, wraps around 0
    head = (head + 1) % BUFF_SIZE;
    // Update counter
    count ++;
    return 0; 
}

int buffer_get(char *c){
    // Empty BUFF
    if (count == 0 ) return -1; 
    // Retrieve data on tail position
    *c = buffer[tail]; 
    // Update tail
    tail = (tail + 1) % BUFF_SIZE;
    count--;
    return 0;
}