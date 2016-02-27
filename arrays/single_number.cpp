#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {
	    std::unordered_set<int> encountered;
	    encountered.reserve(nums.size());
	    for (const auto& num: nums) {
		    auto result = encountered.insert(num);
		    if (!result.second) {
			    encountered.erase(num);
		    }
	    }
	    return *encountered.begin();
    }
};

int main() {
	std::vector<int> v = {3, 3, 4, 4, 5};
	Solution s = Solution();
	std::cout << s.singleNumber(v);

	std::vector<int> v2 = {3, 8, 3, 4, 4};
	Solution s2 = Solution();
	std::cout << s2.singleNumber(v2);
}
