#include <unordered_map>
class Solution {
private:
    unordered_map<char,vector<string>> num_to_letter;
    vector<string> res;
public:
    vector<string> letterCombinations(string digits) {
        if (digits == "") return {};
        num_to_letter['2'] = {"a","b","c"};
        num_to_letter['3'] = {"d","e","f"};
        num_to_letter['4'] = {"g","h","i"};
        num_to_letter['5'] = {"j","k","l"};
        num_to_letter['6'] = {"m","n","o"};
        num_to_letter['7'] = {"p","q","r","s"};
        num_to_letter['8'] = {"t","u","v"};
        num_to_letter['9'] = {"w","x","y","z"};

        string curr;
        dfs(curr,0, digits);
        return res;
    }

    void dfs(string &curr, int i, const string &digits){
        if (i==digits.size()){
            res.push_back(curr);
            return;
        }
        for (string &ch: num_to_letter.at(digits[i])){
            curr += ch;
            dfs(curr,i+1,digits);
            curr.pop_back();
        }
    }
};
