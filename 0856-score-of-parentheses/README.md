# 856. Score of Parentheses

## Approach
The algorithm computes the total score of balanced parentheses by tracking the current nesting depth rather than using an explicit stack memory structure. When an opening parenthesis '(' is encountered, the nesting depth increases. When a closing parenthesis ')' is encountered, the depth decreases. A score contribution of 2^depth (calculated efficiently using the bitwise left shift `1 << depth`) is added to the total score only at the core of a nested structure—specifically when a ')' directly follows an '(' (forming an immediate pair '()'). Outer parentheses multiply inner scores by 2, which mathematically corresponds to summing 2^depth for every base '()' unit at its given depth.

## How It Works
1. Initialize `score = 0` to store the final result and `depth = 0` to keep track of the current level of parenthesis nesting.
2. Iterate through each character `s[i]` of the string from index `0` to `s.size() - 1`:
   a. If `s[i] == '('`, increment `depth` by 1.
   b. If `s[i] == ')'`, decrement `depth` by 1. Then, check if `s[i - 1] == '('`. If true, an immediate '()' pair is detected at the current `depth`. Add `1 << depth` (which equals 2^depth) to `score`.
3. After traversing the string, return `score`.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm performs a single pass over the input string of length n. Inside the loop, all operations (increment, decrement, array index lookup, and bitwise shift) execute in O(1) constant time, yielding a linear time complexity of O(n).
- **Space Complexity:** `O(1)` — Only two integer scalar variables (`score` and `depth`) are created and updated throughout execution. No dynamic data structures like vectors or explicit stacks are used, resulting in constant auxiliary space complexity.

## Edge Cases
- Minimal input string '()', where depth reaches 1 and adds 1 << 0 = 1, returning 1.
- Flat sequential nested pairs like '()()()', where depth increases to 1 and decreases back to 0 repeatedly, summing 1 + 1 + 1 = 3.
- Deeply nested parentheses like '((()))', where depth reaches 3 before closing, adding 1 << 2 = 4 to the score.

## Solution
```cpp
class Solution {
public:
    int scoreOfParentheses(string s) {
        int score = 0, depth = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                ++depth;
            } else {
                --depth;
                if (s[i - 1] == '(') {
                    score += 1 << depth;
                }
            }
        }
        return score;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0856-score-of-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)
