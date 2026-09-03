#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> dct;
        for (int i=0;i<nums.size();i++){
            dct[target-nums[i]]=i;
        }

        for (int i=0;i<nums.size();i++){
            if (dct.count(nums[i])!=0 && i!=dct[nums[i]]){
                return {i,dct[nums[i]]};
            }
        }
    }
};
