#include <queue>
#include <algorithm>
class KthLargest {
private:
std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
int cap;
public:
    KthLargest(int k, vector<int>& nums) {
        cap = k;
        for (auto &num: nums){
            add(num);
        }
    }
    
    int add(int val) {
        min_heap.push(val);

        if (min_heap.size() > cap) min_heap.pop();

        return min_heap.top();
    }
};
