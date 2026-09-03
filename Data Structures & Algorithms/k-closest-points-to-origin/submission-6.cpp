#include <queue>
#include <utility>
#include <algorithm>
#include <cmath>
#include <vector>
#include <functional>
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<std::pair<double,int>,    std::vector<std::pair<double, int>>, 
    std::greater<std::pair<double, int>>> closest_points;

        int i=0;
        for (int i=0;i<points.size();i++){
            auto num = points[i];
            double distance = std::sqrt(std::pow((num[0]-0),2)+ std::pow((num[1]-0),2));
            closest_points.push({distance,i});
        }
        std::vector<std::vector<int>> res; 
        for (int i=0;i<k;i++){
            auto [x,y] = closest_points.top();
            closest_points.pop();
            res.push_back(points[y]);
        }

        return res;


    }
};
