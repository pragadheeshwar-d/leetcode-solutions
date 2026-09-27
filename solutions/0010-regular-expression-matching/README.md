# 10. Regular Expression Matching

🔗 [LeetCode Problem](https://leetcode.com/problems/regular-expression-matching/)

**Author:** [@Pragadheeshwar-06](https://leetcode.com/u/Pragadheeshwar-06/) (Global Rank: #642,244)  
**Difficulty:** Hard  
**Pattern:** Dynamic Programming (String, Recursion)  

---

## Problem Statement

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

	- `'.'` Matches any single character.​​​​

	- `'*'` Matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string (not partial).

 

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

 

**Constraints:**

	- `1 <= s.length <= 20`

	- `1 <= p.length <= 20`

	- `s` contains only lowercase English letters.

	- `p` contains only lowercase English letters, `'.'`, and `'*'`.

	- It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

---

## Approach

We break down the problem into optimal overlapping subproblems. By establishing recurrence relations and tabulating states, we build up the global optimal solution without redundant recalculation.

---

## Algorithm

1. Define the DP state representation and initialize base cases.
2. Iterate through the state space using bottom-up tabulation or memoized recursion.
3. Apply the transition formula based on optimal subproblem solutions.
4. Return the final target state.

---

## Why This Works

By caching the solutions to subproblems, we ensure that no overlapping state is computed more than once, transforming exponential recursion trees into polynomial-time table lookups.

---

## Complexity Analysis

- **Time Complexity:** `O(n²)` — Nested iterations over input elements.
- **Space Complexity:** `O(m × n)` — Allocates an m × n grid table to store subproblem results.

---

## Solution

```cpp
        memset(dp, false, sizeof(dp));
        dp[0][0] = true;
        
        for(int i=0; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(p[j-1] == '*'){
                    dp[i][j] = dp[i][j-2] || (i > 0 && (s[i-1] == p[j-2] || p[j-2] == '.') && dp[i-1][j]);
                }
                else{
                    dp[i][j] = i > 0 && dp[i-1][j-1] && (s[i-1] == p[j-1] || p[j-1] == '.');
                }
            }
        }
        
        return dp[n][m];
    }
};
```
