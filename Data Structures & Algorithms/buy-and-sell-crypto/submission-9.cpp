class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int mx_profit = 0;
        int curr_cheapest = prices[0];
        for (auto num: prices){
            if (num-curr_cheapest > mx_profit){
                mx_profit = num-curr_cheapest;
            }
            if (curr_cheapest > num){
                curr_cheapest = num;
            }
        }
        return mx_profit;
    }
};
