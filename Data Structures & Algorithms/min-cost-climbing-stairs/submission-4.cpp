#include <unordered_map>
#include <algorithm>
class Solution {
private:
    std::unordered_map<int,int> memo;
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int res_1 = dfs(0,cost);
        memo.clear();
        int res_2 = dfs(1,cost);
        return std::min(res_1,res_2);
    }

    int dfs(int idx, const std::vector<int>& cost){
        if (memo.count(idx)==1){
            return memo[idx];
        }
        if (idx >= cost.size()){
            return 0;
        }

        memo[idx] = cost[idx] + std::min(dfs(idx+1,cost),dfs(idx+2,cost));
        return memo[idx];
    }

};
