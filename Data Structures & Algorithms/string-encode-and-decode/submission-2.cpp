class Solution {
public:
    char delimiter = static_cast<char>(0xFF);

    string encode(vector<string>& strs) {
        string encodedString;
        for (const string& s : strs) {
            encodedString += s;
            encodedString += delimiter;
        }
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> decodedStrings;
        int prev = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == delimiter) {
                decodedStrings.push_back(s.substr(prev, i - prev));
                prev = i + 1;
            }
        }
        return decodedStrings;
    }
};
