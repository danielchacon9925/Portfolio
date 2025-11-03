#include <stdio.h>
#include <stdbool.h>

//////////////////////////////////
// Function to find lowest value//
////////////////////////////////// 
int Find_Lowest(int *nums, int size){
    // Find index different than 0
    int index = 0;
    for (int j=0; j<size; j++){
        if (nums[j] != 0)
        {
            index = j;
        }
    }
    //printf("Index selected: %d\n", index);
    // Initialize lowest value at start of list
    int LOWEST_VALUE = nums[index];
    for (int i = 0; i<size-1;i++){
        if (nums[i]<LOWEST_VALUE && nums[i] != 0){
            LOWEST_VALUE = nums[i];
        }
    }
    return LOWEST_VALUE;
}
//_________________________________________
/////////////////////////////////////////////////
// Function to evaluate if array is full of 0's//
/////////////////////////////////////////////////
bool IS_ARRAY_ZEROED(int *nums, int size){
    for(int i = 0; i<size;i++){
        if(nums[i]!=0){
            return false;
        }
    }
    return true;
}
//_________________________________________
////////////////////////////
// Function to print array//
//////////////////////////// 
int PRINT_ARRAY(int *nums, int size){
    printf("{");
    for (int i = 0; i < size; i++)
    {
        printf("%d,",nums[i]);
    }
    printf("}\n");
}
int Make_Array_Zero(int *nums, int size){
    // Finds smaller
    int SMALLEST = Find_Lowest(nums, size);
    // Counter
    int count = 0;
    printf("The smallest value found is: %d\n",SMALLEST);
    // Empty array
    bool EMPTY_ARRAY = IS_ARRAY_ZEROED(nums, size);

    while (EMPTY_ARRAY != true)
    {
        for (int i = 0; i < size; i++){
            // Substract the value from each position
            if(nums[i] != 0){
                nums[i] = nums[i]-SMALLEST;
                //printf("The value now is: %d\n",nums[i]);
                EMPTY_ARRAY = IS_ARRAY_ZEROED(nums, size);
            }
        }
        int PRINT = PRINT_ARRAY(nums, size); 
        SMALLEST = Find_Lowest(nums, size);
        printf("The smallest value found left is: %d\n",SMALLEST);
        printf("===================\n");
        count++;       
    }
    return count;
}







int main(){
    int test_array[5]={1,5,0,3,5};
    int SIZE_ARRAY = sizeof(test_array)/sizeof(test_array[0]);
    printf("SIZE: %d\n", SIZE_ARRAY);

    int COUNT_UNTIL_ZERO = Make_Array_Zero(test_array,SIZE_ARRAY);
    printf("The amount of iteration until 0 is: %d\n",COUNT_UNTIL_ZERO);

}
