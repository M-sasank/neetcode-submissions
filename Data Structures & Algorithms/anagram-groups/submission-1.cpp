class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        
        // For each string, sort it to create the key
        
        for (const string& str : strs) {
            vector <int> count(26,0);
            string key;
            for (char c : str){
                count[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
            key += to_string(count[i]) + "#";  // Use delimiter
            }

            hash[key].push_back(str);
        }
        
        // Extract all groups from hash map
        vector<vector<string>> result;
        for (const auto& pair : hash) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};
