#include <vector>
#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int,int> mp;
        int mx=0;
        for (auto &num: nums){
            mp[num]++;
            mx = std::max(mx,mp[num]);
        }
        std::vector<std::vector<int>> vec(mx+1);
        for (auto &p: mp){
            vec[p.second].push_back(p.first);
        }
        std::vector<int> ans;
        for (auto it=vec.end(); it!=vec.begin();){
            it--;
            for (auto num:*it){
                if (k!=0) {
                    ans.push_back(num);
                    k--;
                }
            }
        }
        return ans;
    }  
};
