# 14. Longest Common Prefix

## Problem

Given the input constraints for Longest Common Prefix, compute the optimal result.

## Approach

The solution performs vertical scanning across the string array by comparing characters column by column. It iterates through each character index of the first string, verifying that every other string matches at that same position. On the first mismatch or when reaching the end of any string, it returns the common prefix accumulated so far.

## How the Solution Works

1. **Column Iteration:** Iterate character index `i` of `strs[0]`.
2. **Cross-Word Check:** For each string `strs[j]` from `j = 1` to `strs.size() - 1`:
   - If `i >= strs[j].size()` or `strs[j][i] != strs[0][i]`: return `strs[0].substr(0, i)`.
3. **Complete Match:** If all columns match, return `strs[0]`.

## Algorithm

1. If `strs` is empty, return empty string.
2. For column index `i = 0` to `strs[0].length() - 1`:
3.   Let `c = strs[0][i]`.
4.   For string index `j = 1` to `strs.length() - 1`:
5.     If `i >= strs[j].length()` or `strs[j][i] != c`: return `strs[0].substr(0, i)`.
6. Return `strs[0]`.

## Why This Works

Vertical scanning inspects characters column by column across all words simultaneously, allowing instant early termination the very moment a discrepancy is detected rather than scanning unnecessary string tails.

## Complexity

### Time Complexity

`O(S)` — Where S is the total number of characters across all strings. In the worst case, all n strings of length m are identical, executing n × m comparisons.

### Space Complexity

`O(1)` — Constant auxiliary space; only index counters and boundary registers are maintained in-place.

## Edge Cases

- **Empty Array:** Empty input returns `""` immediately.
- **Single String:** Array with one string returns `strs[0]` directly.
- **No Common Prefix:** Discrepancy at column 0 immediately terminates returning `""`.
- **Unequal Word Lengths:** Guarded by `i >= strs[j].size()`, preventing out-of-bounds indexing.

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
