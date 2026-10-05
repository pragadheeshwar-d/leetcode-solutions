# 32. Longest Valid Parentheses

## Approach
The solution uses a stack to maintain the indices of parentheses to determine the length of valid substrings. It initializes the stack with a dummy boundary index of -1, which helps calculate valid substring lengths right from the beginning of the string. As the string is traversed, the index of every open parenthesis '(' is pushed onto the stack. When a closing parenthesis ')' is encountered, the top index is popped from the stack. If the stack becomes empty after popping, it signifies an unmatched closing bracket, and the current index is pushed onto the stack to set a new base boundary. If the stack is not empty, the current valid substring length is calculated as the difference between the current index and the index currently at the top of the stack.

## How It Works
1. Initialize `stack<int> st` and push `-1` to serve as the initial reference boundary.
2. Initialize `ans = 0` to store the maximum length of valid parentheses found.
3. Loop through each character `s[i]` in string `s` using index `i` from `0` to `s.size() - 1`:
   - If `s[i] == '('`, push `i` onto `st`.
   - If `s[i] == ')'`, pop the top element from `st`.
   - Check if `st.empty()`:
     - If empty, push `i` to act as the new boundary for future valid substrings.
     - If not empty, compute `i - st.top()` to get the length of the valid substring ending at `i`, and update `ans = max(ans, i - st.top())`.
4. Return `ans` after traversing the entire string.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm processes each character of the string `s` of length `n` exactly once in a single loop. Each character's index is pushed onto and popped from the stack `st` at most once, making all stack operations O(1). Hence, the overall time complexity is linear, O(n).
- **Space Complexity:** `O(n)` — In the worst-case scenario (e.g., a string consisting entirely of open parentheses like "((((("), the stack `st` will hold up to `n + 1` integer elements (including the initial `-1`). Therefore, the auxiliary space complexity is O(n).

## Edge Cases
- Empty string: The loop does not execute, returning the initial value of `ans`, which is 0.
- No valid parentheses (e.g., ")))" or "((("): Stack pushes boundaries or unclosed open brackets without updating `ans` beyond 0.
- Entire string is valid (e.g., "()()" or "((()))"): Correctly uses the base `-1` or nested boundary indices to compute the full length `n`.
- Mismatched and redundant closing brackets (e.g., ")()()"): The initial ')' resets the boundary to index 0, allowing subsequent valid pairs to correctly measure length from index 0.

## Solution
```cpp
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;
    st.push(-1);

    int ans = 0;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '(') {
            st.push(i);
        } else {
            st.pop();

            if (st.empty()) {
                st.push(i);
            } else {
                ans = max(ans, i - st.top());
            }
        }
    }
    return ans;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0032-longest-valid-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
