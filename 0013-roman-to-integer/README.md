# 13. Roman To Integer

## Problem
Given a string `s` representing a Roman numeral, convert it into its corresponding integer value. Roman numerals are represented by seven different symbols: `I` (1), `V` (5), `X` (10), `L` (50), `C` (100), `D` (500), and `M` (1000). While numerals are typically written from largest to smallest from left to right, specific combinations use subtractive notation (for example, `IV` is 4 and `IX` is 9).

## Approach
The code uses a hash table lookup combined with a single left-to-right pass over the string. It utilizes the subtractive rule of Roman numerals: if a symbol is followed by a symbol of strictly greater value, the current symbol's value is subtracted from the total; otherwise, it is added.

## How the Solution Works
1. An `unordered_map<char, int> mp` is initialized to store the standard integer mapping for each of the seven Roman numeral characters (`'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'`, `'M'`).
2. An integer accumulator `ans` is initialized to `0`.
3. A `for` loop iterates through the string using an index `i` from `0` to `s.length() - 1`.
4. In each iteration, the code evaluates the condition `i + 1 < s.length() && mp[s[i]] < mp[s[i + 1]]`:
   - If a subsequent character exists and its mapped value is strictly greater than the current character's value, the current character represents a subtractive prefix. Thus, `mp[s[i]]` is subtracted from `ans`.
   - Otherwise, the current character is an additive component, so `mp[s[i]]` is added to `ans`.
5. After the loop completes, the final accumulated value `ans` is returned.

## Algorithm
1. Initialize the character-to-integer hash map `mp` with the 7 Roman numeral base values.
2. Initialize `ans = 0`.
3. Loop variable `i` from `0` up to `s.length() - 1`:
   - If `i + 1 < s.length()` and `mp[s[i]] < mp[s[i + 1]]`, execute `ans = ans - mp[s[i]]`.
   - Otherwise, execute `ans = ans + mp[s[i]]`.
4. Return `ans`.

## Why This Works
In Roman numerals, a smaller value placed immediately before a larger value denotes subtraction (e.g., $IV = 5 - 1 = 4$). Algebraically, $5 - 1$ is equivalent to $-1 + 5$. By scanning left-to-right:
- Encountering `'I'` before `'V'` evaluates `'I' < 'V'`, subtracting $1$ from `ans`.
- When the iterator moves to `'V'`, it is either the last character or not followed by a strictly larger numeral, so $5$ is added to `ans`.
- The net effect is $-1 + 5 = 4$, correctly resolving subtractive pairs without requiring two-character lookups or skipping indices.
- All non-subtractive numerals satisfy `mp[s[i]] >= mp[s[i + 1]]` and are added sequentially.

## Complexity

### Time Complexity
$O(n)$ — where $n$ is the length of the string `s`. The algorithm executes a single `for` loop that runs exactly $n$ iterations. In each iteration, hash map lookups on `mp` with a fixed set of 7 keys take $O(1)$ time on average. Thus, the total time complexity is $O(n)$.

### Space Complexity
$O(1)$ — The `unordered_map` stores a fixed number of key-value pairs (exactly 7 elements), which does not scale with the length of the input string `s`. The auxiliary space used is constant.

## Edge Cases
- **Single Character Strings (e.g., `"O"` not possible, valid inputs like `"I"` or `"M"`)**: The lookahead check `i + 1 < s.length()` evaluates to `false`, correctly routing to the `else` branch to add the value.
- **Subtractive Combinations at the End (e.g., `"MCMXCIV"`)**: The last two characters `'I'` and `'V'` are handled sequentially: `'I'` is subtracted because `mp['I'] < mp['V']`, and `'V'` is added on the final iteration because `i + 1 < s.length()` evaluates to `false`.
- **Monotonically Decreasing or Repeated Symbols (e.g., `"III"`, `"MDCLXVI"`)**: For every adjacent pair where `mp[s[i]] >= mp[s[i + 1]]`, the condition `mp[s[i]] < mp[s[i + 1]]` evaluates to `false`, correctly adding each value.

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
