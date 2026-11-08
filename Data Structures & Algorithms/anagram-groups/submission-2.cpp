#include <unordered_map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::pair<std::string,std::string>> sorted_strs;
        for (auto &word: strs){
            auto og_word = word;
            std::sort(word.begin(),word.end());

            sorted_strs.push_back({word,og_word});
        }

        std::unordered_map<std::string,std::vector<string>> mp;
        for (auto &[x,y]: sorted_strs){
            mp[x].push_back(y);
        }

        std::vector<std::vector<std::string>> result;
        for (auto &vals: mp){
            result.push_back(vals.second);
        }
        return result;
    }
};
