#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sz = nums.size();
        vector<int> idx;

        for (int i = 0; i < sz; i++) {
            int findVal = target - nums[i];

            // search only in the remaining range (no extra space)
            auto it = find(nums.begin() + i + 1, nums.end(), findVal);

            if (it != nums.end()) {
                idx.push_back(i);
                idx.push_back(it - nums.begin());
                break;
            }
        }

        return idx;
    }
};

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> nums(n);
    cout << "Enter array elements:\n";
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int target;
    cout << "Enter target: ";
    cin >> target;

    Solution s;
    vector<int> result = s.twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices (0-indexed): "
             << result[0] << " " << result[1] << endl;
    } else {
        cout << "No pair found!" << endl;
    }

    return 0;
}
