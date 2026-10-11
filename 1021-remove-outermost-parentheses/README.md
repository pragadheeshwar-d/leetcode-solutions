# 1021. Remove Outermost Parentheses

## Approach
The solution uses an integer counter `level` to track the nesting depth of parentheses without using an actual stack data structure. By maintaining the depth state as it iterates through the string, it identifies and skips the outermost parentheses of every primitive decomposition block.

## How It Works
1. Initialize an empty string `res` to store the output and an integer `level` set to `0` to track depth.
2. Iterate through each character `c` in the input string `s`:
   - If `c == '('`:
     - Check if `level > 0`. If `level` is greater than 0, `c` is an inner opening parenthesis, so append it to `res`.
     - Increment `level` by 1.
   - If `c == ')'`:
     - Decrement `level` by 1 first.
     - Check if `level > 0`. If `level` is still greater than 0, `c` is an inner closing parenthesis, so append it to `res`.
3. Return the accumulated string `res`.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm processes the string `s` in a single pass of length `n`, performing O(1) depth counter modifications and string append operations per character.
- **Space Complexity:** `O(n)` — O(n) space is required to store the resulting string `res` containing up to `n - 2` characters in the worst case (excluding the outermost parentheses). The auxiliary memory used is O(1) for the integer counter `level`.

## Edge Cases
- A single primitive parenthesized string like "(())", which removes the outermost layer leaving "()".
- Multiple adjacent primitive parenthesized strings like "()()", which strips the outer brackets of each to leave an empty string "".
- Deeply nested structure like "((()))", which retains inner pairs to result in "(())".

## Solution
```cpp
class Solution {
public:
    string removeOuterParentheses(string s) {
    string res; int level = 0;
    
    for (char c : s)
        if (c == '(') {
            if (level > 0)
                res += c;
            level++;
        } else {
            level--;
            if (level > 0)
                res += c;
        }

    return res;
}
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/1021-remove-outermost-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
