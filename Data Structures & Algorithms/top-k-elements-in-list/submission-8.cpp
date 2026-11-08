#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int,int> mp;
        for (auto &num: nums){
            mp[num]++;
        }
        std::unordered_map<int,std::vector<int>> freq;
        int mx_freq=0;
        for (auto &[x,y]:mp){
            freq[y].push_back(x);
            mx_freq = std::max(mx_freq,y);
        }

        std::vector<int> result;
        while (mx_freq>0){
            if (freq.count(mx_freq) > 0 && k!=0){
                for (auto &num:freq[mx_freq]){
                    result.push_back(num);
                    k--;
                }
            }
            mx_freq--;
        }
        return result;
    }
};
