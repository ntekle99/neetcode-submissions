class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> left_arr(nums.size());
        std::vector<int> right_arr(nums.size());
        std::vector<int> res_arr(nums.size());

        left_arr[0] = nums[0];
        right_arr.back() = nums.back();
        int rev_idx = nums.size()-1;
        for (int i=1;i<nums.size();i++){
            left_arr[i] = nums[i]*left_arr[i-1];
            rev_idx-=1;
            right_arr[rev_idx] = nums[rev_idx] * right_arr[rev_idx+1];

        }

        res_arr[0] = right_arr[1];
        for (int i=1;i<nums.size()-1;i++){
            res_arr[i] = left_arr[i-1] * right_arr[i+1];
        }
        res_arr.back() = (left_arr[nums.size()-2]);
        return res_arr;
    }
};
