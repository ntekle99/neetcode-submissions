#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string,std::vector<string>> mp;
        for (auto &word: strs){
            auto og_word = word;
            std::sort(word.begin(),word.end());
            mp[word].push_back(og_word);
        }

        std::vector<std::vector<std::string>> result;
        for (auto &vals: mp){
            result.push_back(vals.second);
        }
        return result;
    }
};
