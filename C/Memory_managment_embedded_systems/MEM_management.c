// Implement mem administrator for circularr memory for embedded systems
#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define BUFFER_SIZE 256

// "Object"
typedef struct{
    // Memory block size
    uint8_t buffer[BUFFER_SIZE];
    // Write index
    uint8_t head;
    // Read index
    uint8_t tail;
    // Items counter
    uint8_t count;
} Circ_BUFF;

// Method to modify the object. Pointer points to an object
//  pointer in object points to head, tail and count to write default value
void cb_init(Circ_BUFF *cb){
    cb->head = 0;
    cb->tail = 0;
    cb->count = 0;
    memset(cb->buffer,0,BUFFER_SIZE);
}

int cb_push(Circ_BUFF *cb, uint8_t data){
    if (cb->count == BUFFER_SIZE){
        // BUFF full
        printf("Full capacity reached: ", BUFFER_SIZE);
        return -1;
    }
    // Acces to buffer and store value on position pointed to by head
    cb->buffer[cb->head] = data;
    // Update head pointer to the next position
    //  %BUFFER_SIZE is used to wrap at the end
    cb->head = (cb->head + 1) % BUFFER_SIZE;
    cb->count++;
    return 0;
}

int cb_pop(Circ_BUFF *cb, uint8_t *data){
    if (cb->count == 0){
        return -1; // Empty BUFF
    }
    // Points to value in the tail
    *data = cb->buffer[cb->tail];
    // Update tail to next value
    cb->tail = (cb->tail +1) % BUFFER_SIZE;
    // Decrement size
    cb->count--;
    return 0;
}


// Test case

int main(){
    // Object instance 
    Circ_BUFF CB;
    // address-of CB instance
    cb_init(&CB);

    // Write: Push values
    for (int i = 0; i < 10; i++) {
        cb_push(&CB, i);
    }   

    // Read. Empty value to read after
    uint8_t data;
    while(cb_pop(&CB,&data) == 0){
        printf("\nDATA READ: %d\n",data);
    }
    return 0;
}