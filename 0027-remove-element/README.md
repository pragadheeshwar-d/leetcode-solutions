# 27. Remove Element

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
    int removeElement(vector<int>& nums, int val) {
        int k = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0027-remove-element/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Remove Element](https://leetcode.com/problems/remove-element/)
