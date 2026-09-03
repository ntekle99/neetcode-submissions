#include <unordered_map>
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char,int> need;
        std::unordered_map<char,int> curr_have;

        for (auto &ch:s1){
            need[ch]++;
        } 

        int l=0;
        for (int i=0;i<s2.size();i++){
            if (i < s1.size()){
                curr_have[s2[i]]++;
                continue;
            }
            if (curr_have == need){
                return true;
            }
            else{
                if (curr_have[s2[l]] == 1) curr_have.erase(s2[l]);
                else curr_have[s2[l]]--;
                l++;
                curr_have[s2[i]]++;
            }
        }
        if (curr_have == need){
            return true;
        }
        for (auto &[x,y]:curr_have){
            std::cout << x << " " << y << std::endl;
        }
        return false;
    }
};
