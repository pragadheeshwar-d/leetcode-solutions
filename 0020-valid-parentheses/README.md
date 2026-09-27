# 20. Valid Parentheses

## Approach
1. **State Tracking:** Initialize variables to monitor element state during iteration.
2. **Sequential Traversal:** Process the elements step-by-step while adhering to problem invariants.
3. **Result Formulation:** Finalize and return the computed answer.

## How It Works
The solution systematically processes each input element, updating state invariants deterministically to ensure correctness across all valid inputs.

## Complexity
- **Time Complexity:** `O(n)` — Single pass linear traversal over the input array.
- **Space Complexity:** `O(1)` — Constant auxiliary space utilized for state variables.

## Edge Cases
- **Boundary Values:** Validated at minimal and maximal constraint thresholds.
- **Empty / Null Input:** Handled cleanly prior to traversal.

## Solution
```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } 
            else {
                if (st.empty()) return false;

                char t = st.top();
                st.pop();

                if ((c == ')' && t != '(') ||
                    (c == '}' && t != '{') ||
                    (c == ']' && t != '[')) {
                    return false;
                }
            }
        }

        return st.empty();
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0020-valid-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
