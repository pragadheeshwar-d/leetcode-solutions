# 18. 4Sum

## Problem

Given the input constraints for 4Sum, compute the optimal result.

## Approach

The solution sorts the array in non-decreasing order to enable two-pointer convergence and duplicate elimination. It uses nested loops to fix leading anchors while skipping duplicate values. For each pair of anchors, it runs a two-pointer search on the remaining subarray, incrementing the left pointer or decrementing the right pointer based on the sum relative to the target.

## How the Solution Works

1. **Sort Array:** Sort `nums` to structure the search space monotonically.
2. **Anchor Loops:** Iterate outer indices `i` and `j`, skipping contiguous duplicates.
3. **Two-Pointer Search:** Initialize `k = j + 1` and `l = n - 1`. While `k < l`:
   - Compute 4-element sum using 64-bit integer (`long long`) to prevent overflow.
   - If `sum == target`: record quadruplet, advance `k++` and `l--`, and skip identical values.
   - If `sum < target`: increment `k`.
   - If `sum > target`: decrement `l`.
4. **Return Results:** Return accumulated unique tuples.

## Algorithm

1. Sort `nums` in ascending order.
2. For `i = 0` to `n - 1`: skip if `i > 0 && nums[i] == nums[i-1]`.
3.   For `j = i + 1` to `n - 1`: skip if `j > i + 1 && nums[j] == nums[j-1]`.
4.     Set `k = j + 1`, `l = n - 1`.
5.     While `k < l`: evaluate sum; if matched, record and advance past duplicates; else adjust `k` or `l`.
6. Return unique quadruplets.

## Why This Works

Sorting groups duplicate values together and creates a monotonic sequence where shifting boundary pointers deterministically increases or decreases the sum. This transforms an O(n⁴) brute force into an optimal O(n³) scan.

## Complexity

### Time Complexity

`O(n^3)` — Sorting takes O(n \log n). Two nested loops fix the first two anchors in O(n^2), and two pointers traverse the remaining elements in O(n), yielding an overall cubic O(n^3) time bound.

### Space Complexity

`O(1)` — Constant auxiliary space utilized in-place for pointer indexing (excluding sorting recursion stack).

## Edge Cases

- **Fewer Than 4 Elements:** Arrays with length < 4 return an empty list immediately.
- **32-Bit Signed Integer Overflow:** Summing extreme values is safely handled using 64-bit integers (`long long`).
- **Consecutive Duplicate Elements:** Skipped deterministically after sorting to prevent duplicate output sets.

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
