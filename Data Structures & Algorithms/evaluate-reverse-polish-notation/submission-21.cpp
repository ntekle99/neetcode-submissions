#include <stack>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> st;
        int res=0;
        for (auto &token :tokens){
            if (token == "+" || token == "-" || token == "/" || token == "*"){
                int val_1 = st.top();
                st.pop();
                int val_2 = st.top();
                st.pop();
                if (token == "+") res = val_2 + val_1;
                if (token == "-") res = val_2 - val_1;
                if (token == "*") res = val_2 * val_1;
                if (token == "/") res = val_2 / val_1;
                st.push(res);
            }
            else{
                st.push(std::stoi(token));
            }
        }
        return st.top(); 
    }
};
