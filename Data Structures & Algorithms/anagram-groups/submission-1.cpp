#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string,std::vector<std::string>> dct;
        for (auto word: strs){
            auto sorted_word = word;
            std::sort(sorted_word.begin(),sorted_word.end());
            dct[sorted_word].push_back(word);
        }
        std::vector<std::vector<std::string>> res;
        for (auto &lst: dct){
            res.push_back(lst.second);
        }
        return res;
    }
};
