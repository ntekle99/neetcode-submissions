#include <vector>
class Solution {
private:
std::vector<std::vector<int>> res;
std::vector<int> nums;

public:
    vector<vector<int>> permute(vector<int>& nums) {
        std::vector<int> curr_lst;
        this->nums = std::move(nums);
        dfs(curr_lst,0);
        return res;
    }

    void dfs(std::vector<int> curr_lst, int i){
        if (i == nums.size()){
            res.push_back(curr_lst);
            return;
        }

        for (int j=0;j<curr_lst.size()+1;j++){
            curr_lst.insert(curr_lst.begin()+j,nums[i]);
            dfs(curr_lst,i+1);
            curr_lst.erase(curr_lst.begin()+j);
        }

    }
};
