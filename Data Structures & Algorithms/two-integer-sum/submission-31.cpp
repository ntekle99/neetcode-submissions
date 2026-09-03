#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> dct;

        for (int i=0;i<nums.size();i++){
            if (dct.count(nums[i])!=0){
                return {dct[nums[i]],i};
            }
            else{
                dct[target-nums[i]]=i;
            }
        }
    }
};
