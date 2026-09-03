#include <vector>
class Solution {
private:
    std::vector<std::vector<int>> res;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs({},0,nums);
        return res;
    }

    void dfs(std::vector<int> curr_lst,int i,std::vector<int> &nums){
        if (i==nums.size()) {
            res.push_back(curr_lst);
            return;
        }

        curr_lst.push_back(nums[i]);
        dfs(curr_lst,i+1,nums);
        curr_lst.pop_back();

        dfs(curr_lst,i+1,nums);
        return;
    }
};
