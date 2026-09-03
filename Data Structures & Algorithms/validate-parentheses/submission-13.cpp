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
                    std::cout << popped_char << s[i];
                    if ((popped_char == '(' && s[i] == ')') || 
                    (popped_char == '{' && s[i] == '}') || 
                    (popped_char == '[' && s[i] == ']'))
                    {
                        continue;
                    } 
                    else{
                        return false;
                    }
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
