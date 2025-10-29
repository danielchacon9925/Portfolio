#include <iostream>
#include <cstdlib>   // For rand, srand
#include <ctime>     // For time
#include <algorithm> // For std::max: NOT USED


using namespace std;

//==================
// CLASS DEFINITION=
//==================
class node{
    public:
        int data;
        node *next;
        // Constructor
        // DIFFERENT FROM C: Member initializer list
        node(int x=0): data(x),next(nullptr){}
};
//____________________________
//=============================
// Create a random X size list=
//=============================
node* RANDOM_LIST(int SIZE){
    // Error handling
    if (SIZE <= 0){
        cout << "Cant crete a list equal or less than 0"<< endl;
        return nullptr;
    }
    // Head pointer
    // DIFFERENT FROM C: NEW pointer  
    node *head = new node(rand()%10);
    // Pointer to travese the list   
    node *current = head;
    ///////////////////
    // Node creations//
    ///////////////////
    for (int i = 0; i<SIZE; i++){
        // New node allocation using member initializer
        node *new_node = new node(rand()%10); 
        ///////////////////////
        // Linked to the list//
        ///////////////////////
        // Linked the next node
        current->next = new_node;
        // Update current pointer
        current = new_node;      
    }
    // Return head pointer
    return head;
}
//____________________________
//=============
// Count nodes=
//=============
int COUNT_NODES(node *head){
    // Counter 
    int count = 0;
    // Pointer to hold head pointer 
    node *current = head; 
    ///////////////////////
    // Traverse link list//
    ///////////////////////
    while(current != nullptr){
        // Increment count
        count++;
        // Update current pointer
        current=current->next;
    }  
    // Return count
    return count; 
}
//____________________________
//=====================
// Evalaute alloc size=
//=====================
int ALLOC_SIZE(int L1_COUNT, int L2_COUNT){
    // Ternary operator
    int MAX_NODES = (L1_COUNT>L2_COUNT) ? L1_COUNT : L2_COUNT;

    int SIZE = MAX_NODES + 1;

    cout<<"The size to alloc is:  "<< SIZE << endl;
    
    return SIZE;
}
//____________________________
//==============
// Add two nums=
//==============
node* addTwoNumbers(node* L1, node* L2) {
    //=============
    // Count nodes=
    //=============
    // Node count L1
    int L1_COUNT = COUNT_NODES(L1);
    // Node count L2
    int L2_COUNT = COUNT_NODES(L2);
    // Alloc size
    int SIZE_TO_ALLOC = ALLOC_SIZE(L1_COUNT, L2_COUNT);
    //==============
    // DEBUG PRINTS=
    //==============
    cout<<"Node count L1 "<< L1_COUNT << endl;
    cout<<"Node count L2 "<< L2_COUNT << endl;
    cout<<"SIZE_TO_ALLOC "<< SIZE_TO_ALLOC << endl;
    //======================
    // FIELD INITIALIZATION=
    //======================
    // SUM RESULT
    node *SUM_RESULT = new node(0);
    // No error handling becasue new() implements bad_alloc

    // Pointer to traverse the list
    node *current = SUM_RESULT;
    // Carry
    int carry = 0;
    ///////////////////
    // Node creations//
    ///////////////////
    for(int i = 0; i<SIZE_TO_ALLOC-1; i++){

        if(current != nullptr || carry != 0){

        // Check if space if empty, if so, add a 0
        int VALUE_1 = (L1 != nullptr) ? L1->data : 0;
        int VALUE_2 = (L2 != nullptr) ? L2->data : 0;

        cout<<"Data en L1 "<< VALUE_1 << endl;
        cout<<"Data en L2 "<< VALUE_2 << endl;

        // Data calculation
        int SUMA_index =  VALUE_1 + VALUE_2 + carry;
        // Carry calculation
        carry = SUMA_index/10;
        // Digit
        int digit = SUMA_index % 10;

        cout<<"EL resultado es: "<< digit << endl;
        //////////////////////////
        // Fields initialization//
        //////////////////////////       
        node *NEW_NODE= new node(digit);

        ///////////////////
        // NODE INSERTION//
        ///////////////////        
        // Perform insertion at the end of the list
        current->next = NEW_NODE;
        // Update pointer
        current=current->next;
        ///////////////////////////
        // Update pointers for LL//
        ///////////////////////////
            if (L1 != nullptr){
                L1=L1->next;
            }
            if (L2 != nullptr){
                L2=L2->next;
            }
        }
        //printf("Salió de loop en if\n");

    }
    // To avoid return the head (has a 0)
    return SUM_RESULT->next;
}
//____________________________
//============
// PRINT LIST=
//============
void PRINT_LIST(node* head){
    // Pointer to store original head address
    node *VALUE_TO_PRINT = head;

    // Print every element until find NULL
    while (VALUE_TO_PRINT != nullptr){
        // Point to data space
        cout << VALUE_TO_PRINT->data << endl;
        // Update pointer to next node
        VALUE_TO_PRINT = VALUE_TO_PRINT->next; 
    }
    printf("\n"); 
}
//____________________________
//===========
// FREE_LIST=
//===========
void FREE_LIST(node *head){
    // Pointer to traverse the list
    node *current = head;
    // Temporary variable to save next node
    node *next_node;
    while(current != nullptr){
        // Pointer pointing to next node
        next_node = current->next;
        // Free current node
        delete(current);
        // Update current to next node
        current = next_node; 
    }
}

int main(){

    // Seed for random numbers
    srand(time(NULL));

    cout<<"---------------------------"<<endl;
    cout<<"-----TESTING FUNCTIONS-----"<<endl;
    cout<<"---------------------------"<<endl;
    ////////////////////
    // 1. Create list //
    ////////////////////
    cout<<"------1. LIST CREATION------"<<endl; 
    cout<<"First list created: "<<endl;
    node *LIST_CREATED_L1 = RANDOM_LIST(5);
    PRINT_LIST(LIST_CREATED_L1); 
    cout<<"------2. LIST CREATION------"<<endl; 
    cout<<"Second list created: "<<endl;
    node *LIST_CREATED_L2 = RANDOM_LIST(3);
    PRINT_LIST(LIST_CREATED_L2);
    cout<<"---------------------------"<<endl;

    node *PROTO_FUN = addTwoNumbers(LIST_CREATED_L1,LIST_CREATED_L2);

    PRINT_LIST(PROTO_FUN); 

    FREE_LIST(LIST_CREATED_L1);
    FREE_LIST(LIST_CREATED_L2);
    FREE_LIST(PROTO_FUN);


}