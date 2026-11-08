#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> mp;
        std::unordered_map<char,int> mp_2;


        for (auto &ch: s){
            mp[ch]++;
        }
        for (auto &ch: t){
            mp_2[ch]++;
        }


        for (auto &ch: s){
            if (mp[ch]!=mp_2[ch]) return false;
        }
        for (auto &ch: t){
            if (mp[ch]!=mp_2[ch]) return false;
        }
        return true;

    }
};
