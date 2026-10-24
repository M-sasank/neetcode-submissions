class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        if (size(nums)==2){
            return {0,1};
        }
        int left=0;
        int right = nums.size()-1;

        unordered_map <int, int> diff;

        for(int i = 0; i<size(nums); i++){
            int comp = target - nums[i];

            if (diff.find(comp)!=diff.end()){
                return {diff[comp], i};
            }

            diff[nums[i]] = i;

        }
        return {};
    }
};
