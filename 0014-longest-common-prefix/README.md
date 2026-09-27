# 14. Longest Common Prefix

## Problem

Given the input constraints for Longest Common Prefix, compute the optimal result.

## Approach

The solution sequentially iterates through the input elements, updating state variables according to the problem constraints.

## How the Solution Works

Processes elements step-by-step, maintaining invariants until completion.

## Algorithm

1. Initialize state tracking variables.
2. Iterate through input elements and evaluate conditions.
3. Return the computed result.

## Why This Works

The sequential evaluation guarantees that every element is inspected and processed deterministically.

## Complexity

### Time Complexity

`O(n)` — Traversing the input elements linearly in a single pass.

### Space Complexity

`O(1)` — Constant auxiliary space used for loop state tracking.

## Edge Cases

- **Empty / Minimal Input:** Constraints at minimum threshold.
- **Boundary Extremes:** Maximum allowed input values.

## Solution

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i = 0; i < strs[0].size(); i++) {
            char c = strs[0][i];

            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0];
    }
};
```
