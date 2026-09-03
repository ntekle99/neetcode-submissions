#include <string>
#include <vector>
class Solution {
public:

    string encode(std::vector<std::string>& strs) {
        std::string encoded_string;
        for (auto &str: strs){
            encoded_string += std::to_string(str.size()) + "#" + str;
        }
        return encoded_string;
    }

    std::vector<std::string> decode(string s) {
        int loop_idx = 0;
        int i=0;
        std::vector<std::string> decoded_strs;
        while (i!=s.size()){
            loop_idx = 0;
            while (s[i] != '#') {
                loop_idx = loop_idx * 10 + (s[i] - '0');
                i++;
            }

            i++;
            decoded_strs.push_back(s.substr(i,loop_idx));
            i+=loop_idx;
        }
        return decoded_strs;
    }
};
