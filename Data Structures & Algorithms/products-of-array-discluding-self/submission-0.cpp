class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> results(size(nums),1);
        // left pass
        int left_prod = 1;
        for(int i = 1;i <size(nums);i++){
            left_prod *= nums[i-1]; 
            results[i] *= left_prod;
        }
        // return results;
        int right_prod = 1;
        for(int i = size(nums)-2;i>=0;i--){
            right_prod *= nums[i+1];
            results[i] *= right_prod;
        }
        
        return results;
    }
};
