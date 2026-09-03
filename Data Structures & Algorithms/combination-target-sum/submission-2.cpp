class Solution {
private:
    std::vector<std::vector<int>> res;
    std::vector<int> nums;
    int target;
    
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        this->nums = std::move(nums);
        this->target = target;
        std::vector<int> curr_lst;
        dfs(curr_lst,0,0);
        return res;
    }

    void dfs(std::vector<int> &curr_lst,int i, int total){
        if (total == target){
            res.push_back(curr_lst);
            return;
        }
        if (total > target || i >= nums.size()) return;

        curr_lst.push_back(nums[i]);
        dfs(curr_lst,i,total+nums[i]);
        curr_lst.pop_back();

        dfs(curr_lst,i+1,total);
        
        return;
    }
};
