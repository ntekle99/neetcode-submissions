#include <unordered_set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> st;
        int longest_len = 0;
        int l = 0;
        for (auto &ch: s){
            if (st.count(ch)!=0){
                while (st.count(ch)!=0){
                    st.erase(s[l]);
                    l++;
                }
                st.insert(ch);
            }
            else{
                st.insert(ch);
            }
            if (st.size() > longest_len) longest_len = st.size();
        }
        for (auto ch: st){
            std::cout << ch << " ";
        }
        return longest_len;
    }
};
