# 678. Valid Parenthesis String

## Approach
Greedy Range Tracking / Variable Bounds Approach

## How It Works
The algorithm tracks the range of possible counts of open parentheses that could be left unmatched at any point in the string. It maintains two integer variables: `low` (the minimum possible number of open parentheses) and `high` (the maximum possible number of open parentheses).

1. It iterates through each character `c` in the string `s`:
   - If `c == '('`: Increments both `low` and `high` by 1, as an open bracket increases the open bracket count.
   - If `c == ')'`: Decrements both `low` and `high` by 1, as a closed bracket matches an open bracket.
   - If `c == '*'`: Decrements `low` by 1 (assuming `*` acts as `)`) and increments `high` by 1 (assuming `*` acts as `(`).
2. If `high < 0` at any point, it means even under the most optimistic scenario (treating all `*` as `(`), there are too many closing parentheses `)`, so the string is invalid and `false` is returned.
3. `low = max(low, 0)` ensures `low` never drops below 0 because `*` can also be treated as an empty string (meaning we never need less than 0 open brackets).
4. After processing the entire string, the function checks `low == 0`, returning `true` if it is possible to have 0 unmatched open parentheses.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm uses a single pass (`for (char c : s)`) over the string of length `n`. Each iteration performs constant time `O(1)` conditional checks, arithmetic operations, and calls `std::max`, leading to a total linear runtime.
- **Space Complexity:** `O(1)` — Only two integer state variables (`low` and `high`) are allocated. Memory usage remains constant regardless of the length of the input string `s`.

## Edge Cases
- String starting with `)`: `high` becomes -1 on the first iteration, immediately returning `false`.
- String consisting only of `*`: `high` increases while `low` stays clamped at 0, returning `true` at the end.
- Unmatched `(` at the end (e.g., `"((("`): `low` remains greater than 0 at the end of the loop, returning `false`.
- Excess `)` that cannot be compensated by `*` (e.g., `"*))"`): `high` drops below 0, returning `false`.

## Solution
```cpp
class Solution {
public:
    bool checkValidString(string s) {
        int low = 0, high = 0;

        for (char c : s) {
            if (c == '(') {
                low++;
                high++;
            }
            else if (c == ')') {
                low--;
                high--;
            }
            else {
                low--;
                high++;
            }

            if (high < 0)
                return false;

            low = max(low, 0);
        }

        return low == 0;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0678-valid-parenthesis-string/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)
