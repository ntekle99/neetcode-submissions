#include <stack>
#include <utility>
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<std::pair<int,int>> st;
        std::vector<int> res(temperatures.size());
        int i=0;
        while (i < temperatures.size()){
            if (st.size()==0) st.push({temperatures[i],i});
            else if (temperatures[i] <= st.top().first){
                st.push({temperatures[i],i});
            }
            else{
                while (st.size() > 0 && temperatures[i] > st.top().first){
                    auto [val,idx] = st.top();
                    st.pop();
                    res[idx] = i-idx;
                }
                st.push({temperatures[i],i});
            }
            i++;
        }
        return res;
    }
};
