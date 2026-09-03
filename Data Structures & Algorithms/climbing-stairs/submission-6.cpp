#include <unordered_map>
class Solution {
private:
    std::unordered_map<int,int> dct;
public:
    int climbStairs(int n) {
        int curr = 0;
        return dfs(curr,n);
    }

    int dfs(int curr,int target){
        if (dct.count(curr) == 1){
            return dct[curr];
        }
        if (curr == target) return 1;
        
        if (curr > target) return 0;

        dct[curr] = dfs(curr+1,target) + dfs(curr+2,target);
        return dct[curr];
    }
};
