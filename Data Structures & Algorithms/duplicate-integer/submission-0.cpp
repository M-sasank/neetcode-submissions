class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> count;
        for (int i = 0; i<size(nums);i++){
            if(count[nums[i]]== 2){
                return true;
            }
            count[nums[i]] = 2;
        }
        return false;
    }
};