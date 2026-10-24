class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int, int> freqMap;

        for(int num : nums) {
            freqMap[num]++;
        }

        vector<vector<int>> buckets(size(nums)+1);
        for( auto &entry: freqMap){
            buckets[entry.second].push_back(entry.first);
        }

        vector<int> result;
        for (int i = size(nums);i>=0&&size(result)<k;i--){
            for(int num: buckets[i]){
                result.push_back(num);
                if(result.size() == k) break;}
        }
        return result;
    }
};
