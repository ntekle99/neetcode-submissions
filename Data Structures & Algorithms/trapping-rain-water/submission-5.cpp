#include <unordered_map>
#include <algorithm>
class Solution {
public:
    int trap(vector<int>& height) {
        int l=0;
        int r=0;
        int max_l = 0;
        int max_r = 0;
        int total = 0;
        int prev = 0;
        while (l < height.size()){
            if (r < l) r = l;
            if (max_l == 0){
                max_l = std::max(max_l,height[l]);
                l++;
                r++;
                continue;
            } 
            if (max_l <= height[l])
            {
                max_l = height[l];
                l++;
                if (r < l) r++;
                continue;
            }
            if (l==r){
                max_r=0;
                prev=0;
                while (r < height.size() && height[r] <= height[r-1]){
                    r++;
                }
                while (max_r < max_l && r < height.size()){
                    if (height[r] > max_r) prev = r;
                    max_r = std::max(max_r,height[r]);
                    r++;
                }
                if (r == height.size() && prev!=0) {
                    r = prev;
                }
            }
            if (r >= l){
                total+= std::max(std::min(max_l,max_r)-height[l],0);
                l++;
            }
        }
        return total;
        
    }
};
