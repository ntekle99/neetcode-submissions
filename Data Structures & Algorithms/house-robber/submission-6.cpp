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

        memo[idx] = std::max(dfs(nums,idx + 1),nums[idx] +dfs(nums,idx + 2));
        return memo[idx];
    }
};
