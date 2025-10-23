#include<stdio.h>
#include<stdlib.h>

// Declaration
int *twoSum(int* nums, int numsSize, int target, int* returnSize);
// Two sum function
int *twoSum(int* nums, int numsSize, int target, int* returnSize){
    // Return only two indices
    *returnSize = 2;
    // Allocate memory for the result array
    int *result = (int *)malloc(2*sizeof(int));
    // Error handling 
    if (result == NULL){
        *returnSize = 0;
        return NULL;
    }
    for (int i=0;i<numsSize; i++){
        for(int j = i + 1; j<numsSize; j++){
            if (nums[i]+nums[j]==target){
                result[0]=i;
                result[1]=j;
                return result; 
            }
        }
    }
    free(result);
    *returnSize = 0; 
    return NULL;
}
int TEST_CASES(){
    int returnSIZE = 0;
    //==============
    // TEST CASE 1 =
    //==============
    int num_list_1[] = {2,7,11,15};    
    int SIZE_LIST_1 = sizeof(num_list_1)/sizeof(num_list_1[0]); 
    int target_1 = 9;
    int *RESULT_1 = twoSum(num_list_1,SIZE_LIST_1,target_1,&returnSIZE);
    // PRINT TEST CASE 1
    printf("Input List 1: [");
    for (int i = 0; i < SIZE_LIST_1; i++) {
        printf("%d%s", num_list_1[i], (i == SIZE_LIST_1 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("THe target 1 is: %d\n",target_1);
    printf("The SIZE of the list is %d\n", SIZE_LIST_1);
    printf("Result List: [");
    for (int i = 0; i < 2; i++) {
        printf("%d%s", RESULT_1[i], (i == 2 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("=====================================\n");
    free(RESULT_1);
    //==============
    // TEST CASE 2 =
    //==============
    int num_list_2[] = {3,2,4};    
    int SIZE_LIST_2 = sizeof(num_list_2)/sizeof(num_list_2[0]); 
    int target_2 = 6;
    int *RESULT_2 = twoSum(num_list_2,SIZE_LIST_2,target_2,&returnSIZE);
    // PRINT TEST CASE 1
    printf("Input List 2: [");
    for (int i = 0; i < SIZE_LIST_2; i++) {
        printf("%d%s", num_list_2[i], (i == SIZE_LIST_2 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("THe target 2 is: %d\n",target_2);
    printf("The SIZE of the list is %d\n", SIZE_LIST_2);
    printf("Result List: [");
    for (int i = 0; i < 2; i++) {
        printf("%d%s", RESULT_2[i], (i == 2 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("=====================================\n");
    free(RESULT_2);
    //==============
    // TEST CASE 3 =
    //==============
    int num_list_3[] = {3,1,2,3};    
    int SIZE_LIST_3 = sizeof(num_list_3)/sizeof(num_list_3[0]); 
    int target_3 = 6;
    int *RESULT_3 = twoSum(num_list_3,SIZE_LIST_3,target_3,&returnSIZE);
    // PRINT TEST CASE 1
    printf("Input List 2: [");
    for (int i = 0; i < SIZE_LIST_3; i++) {
        printf("%d%s", num_list_3[i], (i == SIZE_LIST_3 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("THe target 3 is: %d\n",target_3);
    printf("The SIZE of the list is %d\n", SIZE_LIST_3);
    printf("Result List: [");
    for (int i = 0; i < 2; i++) {
        printf("%d%s", RESULT_3[i], (i == 2 - 1) ? "" : ", ");
    }
    printf("]\n");
    printf("=====================================\n");
    free(RESULT_3);
}

int main(){
    int TEST = TEST_CASES(); 
}