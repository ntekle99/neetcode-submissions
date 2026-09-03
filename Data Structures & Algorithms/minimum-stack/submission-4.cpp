#include <stack>
class MinStack {
private:
    std::stack<int> st;
    std::stack<int> min_val;
public:
    MinStack() {
    }
    
    void push(int val) {
        st.push(val);
        if (min_val.size()==0){
            min_val.push(val);
            return;
        } 

        if (val < min_val.top()){
            min_val.push(val);
        }
        else{
            auto top_val = min_val.top();
            min_val.push(top_val);
        }
    }
    
    void pop() {
        st.pop();
        min_val.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return min_val.top();
    }
};
