class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> count;
        for (int num :nums){
            if(count.find(num) != count.end()){
                return true;
            }
            count[num]++;
        }
        return false;
    }
};