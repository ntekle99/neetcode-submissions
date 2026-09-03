#include <unordered_map>
class Solution {
private:
    std::unordered_map<int,int> memo;

public:
    int rob(vector<int>& nums) {      
        return std::max(dfs(nums,0),dfs(nums,1));
    }

    int dfs(std::vector<int> &nums, int idx){
        if (memo.count(idx)==1){
            return memo[idx];
        }
        if (idx >= nums.size()){
            return 0;
        }

        memo[idx] = nums[idx] + std::max(dfs(nums,idx+2),dfs(nums,idx+3));
        return memo[idx];
    }
};
