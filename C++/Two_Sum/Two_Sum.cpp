#include <vector>
#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;


class Solution {
    protected:
        vector<int> twoSum(vector<int>& nums, int target) {
            // Result pointer
            vector<int> result(2);
            // Size of the vector
            size_t VECTOR_SIZE = nums.size();
            // Nested loop
            for(int i = 0; i<VECTOR_SIZE;i++){
                for(int j = i+1; j<VECTOR_SIZE;j++){
                    if(nums[i]+nums[j]==target){
                        // Set values to new vector
                        result[0]=i;
                        result[1]=j;  
                        return result;                 
                    } 
                }
            }
            return {};
        }
};
class TEST: protected Solution{
    protected:
        // Vector to test
        vector<int> _NUMS_1;
        // Targets to reach
        int _Target_1;
    public:
        void SET_VECTORs(const vector<int>& VECTOR_1){
            _NUMS_1 = VECTOR_1;
        }
        void SET_TARGETSs(const int Target_1){
            _Target_1 = Target_1;
        }
        vector<int> RUN_TEST(){
            vector<int> RESULT = twoSum(_NUMS_1,_Target_1);
            return RESULT;
        }
        void PRINT_INFO(vector<int>& nums){
            cout<< "Indices found: " << nums[0] << ","<< nums[1]<< endl;
        }
};



int main(){
    //========
    // TEST 1=
    //========
    // Vector
    vector<int> nums_1 = {2,7,11,15};
    // Target
    int target_1 = 9;
    // Instance of TEST
    TEST TEST_1;
    // Vector define
    TEST_1.SET_VECTORs(nums_1);
    // Target define
    TEST_1.SET_TARGETSs(target_1);
    // TEST RUN
    vector<int> RESULT = TEST_1.RUN_TEST();
    // PRINT RESULT
    TEST_1.PRINT_INFO(RESULT);
    //========
    // TEST 2=
    //========
    // Vector
    vector<int> nums_2 = {3,2,4};
    // Target
    int target_2 = 6;
    // Instance of TEST
    TEST TEST_2;
    // Vector define
    TEST_2.SET_VECTORs(nums_2);
    // Target define
    TEST_2.SET_TARGETSs(target_2);
    // TEST RUN
    vector<int> RESULT_1 = TEST_2.RUN_TEST();
    // PRINT RESULT
    TEST_1.PRINT_INFO(RESULT_1);
    //========
    // TEST 3=
    //========
    // Vector
    vector<int> nums_3 = {3,1,2,3};
    // Target
    int target_3 = 6;
    // Instance of TEST
    TEST TEST_3;
    // Vector define
    TEST_3.SET_VECTORs(nums_3);
    // Target define
    TEST_3.SET_TARGETSs(target_3);
    // TEST RUN
    vector<int> RESULT_2 = TEST_3.RUN_TEST();
    // PRINT RESULT
    TEST_3.PRINT_INFO(RESULT_2);
}

