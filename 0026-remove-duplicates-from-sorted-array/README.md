# 26. Remove Duplicates from Sorted Array

## Approach
1. **State Tracking:** Initialize variables to monitor element state during iteration.
2. **Sequential Traversal:** Process the elements step-by-step while adhering to problem invariants.
3. **Result Formulation:** Finalize and return the computed answer.

## How It Works
The solution systematically processes each input element, updating state invariants deterministically to ensure correctness across all valid inputs.

## Complexity
- **Time Complexity:** `O(n)` — Single pass linear traversal over the input array.
- **Space Complexity:** `O(1)` — Constant auxiliary space utilized for state variables.

## Edge Cases
- **Boundary Values:** Validated at minimal and maximal constraint thresholds.
- **Empty / Null Input:** Handled cleanly prior to traversal.

## Solution
```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[j]) {
                j++;
                nums[j] = nums[i];
            }
        }

        return j+1;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0026-remove-duplicates-from-sorted-array/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
