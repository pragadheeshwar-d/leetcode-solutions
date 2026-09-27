# 13. Roman To Integer

## Problem

Given the input constraints for Roman To Integer, compute the optimal result.

## Approach

The solution maps the 7 standard Roman numerals to integer values. It iterates through the string with a lookahead of one position. If the current numeral has a smaller value than the subsequent numeral, it subtracts the current value from the running sum (subtractive case); otherwise, it adds the current value. It returns the accumulated total.

## How the Solution Works

1. **Symbol Mapping:** Define hash map `mp` mapping `'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'`, `'M'` to their values.
2. **Lookahead Check:** For each index `i`, compare `mp[s[i]]` with `mp[s[i + 1]]`.
3. **Subtractive Rule:** If `i + 1 < n` and `mp[s[i]] < mp[s[i + 1]]`, subtract `mp[s[i]]`.
4. **Additive Rule:** Otherwise, add `mp[s[i]]`.
5. **Return Total:** Return the accumulated integer answer.

## Algorithm

1. Define symbol map `mp` for standard Roman numerals.
2. Initialize `ans = 0`.
3. For `i = 0` to `s.length() - 1`:
4.   If `i + 1 < s.length()` and `mp[s[i]] < mp[s[i + 1]]`: `ans -= mp[s[i]]`.
5.   Else: `ans += mp[s[i]]`.
6. Return `ans`.

## Why This Works

Roman numerals are naturally additive except when a smaller value precedes a larger value (subtraction). Looking ahead by one character deterministically isolates subtractive pairs in a single pass without multi-character tokenization.

## Complexity

### Time Complexity

`O(n)` — Where n is the length of the Roman numeral string. Traversed once linearly with O(1) hash map lookups.

### Space Complexity

`O(1)` — Constant auxiliary space; the symbol hash table stores exactly 7 fixed Roman characters.

## Edge Cases

- **Single Numeral:** Strings of length 1 return the mapped value immediately.
- **Subtractive Combinations:** Correctly processes all standard subtractive pairs (`IV`, `IX`, `XL`, `XC`, `CD`, `CM`).
- **Consecutive Additive Symbols:** Evaluates identical repeating characters (`III`, `XXX`) additively.

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
