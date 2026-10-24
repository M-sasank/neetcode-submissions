class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        
        // For each string, sort it to create the key
        for (const string& str : strs) {
            string key = str;  // Make a copy to sort
            sort(key.begin(), key.end());
            hash[key].push_back(str);  // Add original string to group
        }
        
        // Extract all groups from hash map
        vector<vector<string>> result;
        for (const auto& pair : hash) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};
