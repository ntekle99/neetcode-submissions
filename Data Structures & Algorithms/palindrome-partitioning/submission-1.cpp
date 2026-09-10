#include <vector>
class Solution {
    vector<vector<string>> res;
public:
    vector<vector<string>> partition(string s) {
        vector<string> curr;
        dfs(s,curr);
        return res;
    }

    void dfs(string s, vector<string> &curr){
        if (s.size()==0){
            res.push_back(curr);
        }

        for (int i=1;i<=s.size();i++){
            string curr_str = s.substr(0,i);
            if (is_Palindrome(curr_str)==true){
                curr.push_back(curr_str);
                dfs(s.substr(i,s.size()-i),curr);
                curr.pop_back();
            }
        }

    }


    bool is_Palindrome(const string &s){
        auto rev = s.end();
        rev--;
        for (auto it=s.begin();it<rev;it++){
            if (*it != *rev) return false;  
            rev--; 
        } 
        return true;
    }
};
