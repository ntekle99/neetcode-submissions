#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> st(nums.begin(), nums.end());
        return st.size() != nums.size();
    }
};