# 13. Roman To Integer

## Problem

Given the input constraints for Roman To Integer, compute the optimal result.

## Approach

The solution utilizes an auxiliary hash map to store previously visited elements and their metadata, allowing instant O(1) lookups instead of an O(n²) nested loop.

## How the Solution Works

1. Instantiate an empty hash table.
2. Traverse the input sequentially.
3. For each element, check if the required counterpart exists in the table.
4. If found, return the match; otherwise, insert the current element.

## Algorithm

1. Initialize an empty hash table `seen`.
2. For each index `i` and element in the input:
3. Compute required counterpart (e.g. `complement = target - nums[i]`).
4. If counterpart is in `seen`, return the solution pair.
5. Insert current element into `seen`.

## Why This Works

Because the hash table retains all previously seen elements, checking for the required complement occurs in average O(1) time, ensuring that the second element of the pair will instantly detect the first.

## Complexity

### Time Complexity

`O(n)` — Where n is the number of elements. Performs a single linear traversal with average O(1) hash table insertions and lookups.

### Space Complexity

`O(n)` — Auxiliary hash map storing up to n key-value mappings in the worst case.

## Edge Cases

- **Duplicate Values:** Handling repeated values with distinct indices.
- **Negative & Zero Elements:** Values summing to zero or negative targets.
- **Same Element Re-use:** Preventing an element from pairing with itself.

## Solution

```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int ans = 0;

        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && mp[s[i]] < mp[s[i + 1]])
                ans -= mp[s[i]];
            else
                ans += mp[s[i]];
        }

        return ans;
    }
};
```
