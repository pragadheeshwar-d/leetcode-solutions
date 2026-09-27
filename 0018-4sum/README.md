# 18. 4Sum

## Problem

Given the input constraints for 4Sum, compute the optimal result.

## Approach

The solution maintains two boundary pointers initialized at opposite ends of the input. At each iteration, it evaluates the candidate configuration and greedily advances the pointer that limits the optimal outcome inward.

## How the Solution Works

1. **Initialize Boundaries:** Set `left = 0` and `right = n - 1` spanning the widest configuration.
2. **Evaluate State:** Compute metrics using the current boundaries.
3. **Inward Step:** Advance the limiting boundary pointer towards the center.
4. **Loop:** Repeat until pointers converge (`left < right`).

## Algorithm

1. Initialize `left = 0` and `right = n - 1`.
2. While `left < right`: evaluate current candidate value.
3. Advance the pointer with the limiting value (`left++` or `right--`).
4. Return the optimal recorded metric.

## Why This Works

Because the width is maximized initially, pairing the shorter boundary with any interior line will strictly decrease the width without being able to exceed the shorter boundary's height. Thus, interior pairs involving the shorter boundary are mathematically dominated and can be discarded.

## Complexity

### Time Complexity

`O(n)` — Where n is the size of the array. The two boundary pointers advance inward at each step, evaluating each element at most once.

### Space Complexity

`O(1)` — Constant auxiliary space; only pointer variables (`left`, `right`) are maintained in-place.

## Edge Cases

- **Minimum Input Length:** Array with exactly 2 elements.
- **Uniform Heights:** All elements having the same magnitude.
- **Strictly Monotonic:** Strictly ascending or descending values.

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        int n = nums.size();

        // Sort to use two pointers and easily skip duplicates
        sort(nums.begin(), nums.end());

        for(int i = 0; i < n; i++) {
            // Skip duplicate first elements
            if(i > 0 && nums[i] == nums[i-1]) continue;

            for(int j = i + 1; j < n; j++) {
                // Skip duplicate second elements
                if(j > i + 1 && nums[j] == nums[j-1]) continue;

                int k = j + 1;
                int l = n - 1;

                // Find the remaining two elements using two pointers
                while(k < l) {
                    long long sum = nums[i];
                    sum += nums[j];
                    sum += nums[k];
                    sum += nums[l];

                    if(sum == target) {
                        // Found a valid quadruplet
                        vector<int> temp = {
                            nums[i], nums[j], nums[k], nums[l]
                        };

                        ans.push_back(temp);

                        k++;
                        l--;

                        // Skip duplicate third elements
                        while(k < l && nums[k] == nums[k-1]) k++;

                        // Skip duplicate fourth elements
                        while(k < l && nums[l] == nums[l+1]) l--;
                    }
                    else if(sum < target) {
                        // Need a larger sum
                        k++;
                    }
                    else {
                        // Need a smaller sum
                        l--;
                    }
                }
            }
        }

        return ans;
    }
};
```
