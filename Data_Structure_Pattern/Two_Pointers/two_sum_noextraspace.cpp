// return numbers we can sort, return indexes - do not sort at all
/*
1) Brute-Force (No Extra Space, Simple)
Time → O(n²)
Space → O(1)
Guaranteed correct
Works on unsorted arrays

2) Sort + Two-Pointer (Technically O(1) Extra)
This is the best optimized without hash map.
Time → O(n log n) (because of sorting)
Space → O(1) if in-place sort is allowed
Much faster than brute force
But original indices get lost

3) Sort + Two-Pointer While Preserving Indices
If interviewer insists on:
no extra space for main algorithm
but indices must be returned
Minimal extra memory trick:

4) Hash Map Solution (For Comparison Only)
This is the true optimal in practice:
Time → O(n)
Space → O(n)

*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;

        while (i < j) {
            int sum = numbers[i] + numbers[j];

            if (sum > target) {
                j--;
            } 
            else if (sum < target) {
                i++;
            } 
            else { // sum == target
                break;
            }
        }

        // as array is 1-indexed in the problem
        return {i + 1, j + 1};
    }
};

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> numbers(n);
    cout << "Enter sorted array elements:\n";
    for (int i = 0; i < n; i++) {
            cin >> numbers[i];
    }

    int target;
    cout << "Enter target: ";
    cin >> target;

    Solution s;
    vector<int> result = s.twoSum(numbers, target);

    cout << "Indices (1-indexed): " << result[0] << " " << result[1] << endl;

    return 0;
}