#include <unordered_map>
#include <algorithm>
class Solution {
private:
std::unordered_map<int,int> memo;
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        std::vector<int> clone = nums;
        clone.pop_back();
        int res_1 = dfs(nums,1);
        memo.clear();
        int res_2 = dfs(clone,0);
        return std::max(res_1,res_2);
    }
    int dfs(const std::vector<int> &nums, int idx){
        if (memo.count(idx)==1){
            return memo[idx];
        }
        if (idx >= nums.size()){
            return 0;
        }
        

        memo[idx] = std::max(dfs(nums,idx+1),nums[idx]+dfs(nums,idx+2));
        return memo[idx];
    }
};
