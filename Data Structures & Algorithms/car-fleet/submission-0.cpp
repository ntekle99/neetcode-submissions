#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>
class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        std::vector<std::pair<int, double>> cars;
        for (int i = 0; i < position.size(); i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }

        std::sort(cars.begin(), cars.end());
        int fleet = 0;
        double slowestTimeAhead = 0;

        for (int i=cars.size()-1;i>=0;i--){
            double time = cars[i].second;

            if (time > slowestTimeAhead){
                slowestTimeAhead = time;
                fleet++;
            }

        }
        return fleet;
    }
};
