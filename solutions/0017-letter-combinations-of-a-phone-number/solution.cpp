class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        
        if (digits.empty()) {
            return res;
        }
        
        unordered_map<char, string> digitToLetters = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
