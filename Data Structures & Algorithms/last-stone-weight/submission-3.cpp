#include <queue>
#include <algorithm>
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> min_heap(stones.begin(),stones.end());
        while (min_heap.size() >1){
            auto element_1 = min_heap.top();
            min_heap.pop();
            auto element_2 = min_heap.top();
            min_heap.pop();
            if (element_1!=element_2) min_heap.push(element_1-element_2);
        }
        if (min_heap.size()==1) return min_heap.top();
        return 0;


    }
};
