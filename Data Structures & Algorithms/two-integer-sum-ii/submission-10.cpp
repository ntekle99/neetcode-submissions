class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        auto l = numbers.begin();
        auto r = numbers.end();
        r--;
        while (l < r){
            if (*l + *r == target){
                return {(static_cast<int>(l-numbers.begin()))+1,
                (static_cast<int>(r-numbers.begin()))+1
                };
            }
            else if (*l + *r > target){
                r--;
            }
            else{
                l++;
            }
        }        
    }
};
