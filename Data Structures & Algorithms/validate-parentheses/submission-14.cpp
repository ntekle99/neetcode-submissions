#include <stack>
#include <iostream>
class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st;
        
        for (int i=0;i<s.size();i++){
            if (s[i] == '[' || s[i] == '(' || s[i] == '{'){
                st.push(s[i]);
            }
            else{
                if (st.size()!=0){
                    char popped_char = st.top();
                    st.pop();
                    if (s[i] == ')' && popped_char != '(') return false;
                    if (s[i] == ']' && popped_char != '[') return false;
                    if (s[i] == '}' && popped_char != '{') return false;
                }
                else{
                    return false;
                }
            }
        }
        if (st.size() != 0) return false;
        return true;
    
    }
};
