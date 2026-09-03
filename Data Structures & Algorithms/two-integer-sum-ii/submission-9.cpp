class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        auto l = 0;
        int r = numbers.size();
        r--;
        while (l < r){
            if (numbers[l] + numbers[r] == target){
                return {l+1,r+1};
            }
            else if (numbers[l] + numbers[r] > target){
                r--;
            }
            else{
                l++;
            }
        }        
    }
};
