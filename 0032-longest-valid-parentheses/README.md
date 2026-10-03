# 32. Longest Valid Parentheses

## Problem
Given a string `s` containing only the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

## Approach
The submitted solution utilizes a single-pass, stack-based approach to trace the indices of the parentheses. Instead of just storing characters on the stack, the algorithm stores the *indices* of the characters. 

To easily calculate the length of valid substrings without special-casing the boundaries, the stack is initialized with a sentinel/base value of `-1`. This value represents the index right before the starting boundary of any potentially valid substring. 

As we iterate through the string:
- An opening parenthesis `'('` has its index pushed onto the stack.
- A closing parenthesis `')'` triggers a pop operation. 
- After popping, if the stack is not empty, the top of the stack contains the index of the last unmatched character (either a closing parenthesis that acted as a boundary, or an open parenthesis that has not yet been matched). The difference between the current index and this new top index represents the length of the current valid substring.
- If the stack becomes empty, it means the popped element was the previous boundary index. We push the current index onto the stack to establish a new boundary/anchor point for future valid substrings.

## How the Solution Works
Let's walk through the variables and control flow of the code:

1. **`stack<int> st`**: An auxiliary stack used to keep track of the indices of unmatched parentheses and boundary sentinels.
2. **`st.push(-1)`**: Initializes the stack with `-1`. This acts as a virtual boundary index to handle valid substrings starting at index `0`.
3. **`ans = 0`**: An integer variable holding the maximum valid substring length found so far.
4. **Loop `for (int i = 0; i < s.size(); i++)`**: Iterates through each character of string `s` at index `i`.
   - **`if (s[i] == '(')`**: The current index `i` is pushed onto `st`.
   - **`else` (when `s[i] == ')'`)**: 
     - **`st.pop()`**: Pops the top element from the stack.
     - **`if (st.empty())`**: If the stack is empty, the popped element was the boundary anchor. We cannot form a valid substring ending at `i` that spans past this point. We push `i` onto the stack (`st.push(i)`) to act as the new anchor boundary.
     - **`else`**: If the stack is not empty, a valid matching substring has been found. The length of this valid substring is calculated as `i - st.top()`. The maximum length variable is updated: `ans = max(ans, i - st.top())`.
5. **`return ans`**: Returns the maximum accumulated valid length.

## Algorithm
1. Create an integer stack `st` and push `-1` onto it.
2. Initialize `ans = 0` to track the maximum length.
3. For each index `i` from `0` to `s.size() - 1`:
   - If `s[i]` is `'('`, push index `i` onto `st`.
   - If `s[i]` is `')'`:
     - Pop the top index from `st`.
     - If `st` is now empty, push `i` onto `st` (updating the boundary sentinel).
     - Otherwise, calculate the valid substring length as `i - st.top()` and update `ans` if this length is larger.
4. Return `ans`.

## Why This Works
A valid parenthesis substring must contain equal numbers of opening and closing parentheses in correct nested order. 
- By storing indices of unmatched opening parentheses, the stack maintains the exact starting point of current unmatched structures.
- By keeping a boundary index at the bottom of the stack (initially `-1` or the index of the most recent unmatched `')'`), any successful match of a `')'` with an `'('` can immediately determine its valid length by computing the distance from the current index `i` to the current top of the stack.
- Since the top of the stack always represents the index *just before* the start of the current contiguous valid block, `i - st.top()` mathematically guarantees the exact length of the valid segment ending at `i`.

## Complexity

### Time Complexity
`O(n)` — The algorithm processes the string of length $n$ in a single pass. For each character `s[i]`, the stack performs either a push or pop operation. Both `std::stack::push` and `std::stack::pop` are $O(1)$ amortized operations. Thus, the total time complexity is strictly linear with respect to the length of the string, yielding $\mathcal{O}(n)$.

### Space Complexity
`O(n)` — In the worst-case scenario (e.g., a string consisting entirely of `'('` characters, such as `"( ( ( ("`), no matching closing parentheses are encountered. The stack will grow proportionally to the size of the input string, storing up to $n + 1$ integer elements. This results in an auxiliary space complexity of $\mathcal{O}(n)$.

## Edge Cases
- **Empty String (`""`)**: The loop body is never executed because `i < 0`. The function returns `ans = 0` correctly.
- **No Valid Substring (e.g., `")("` or `")"`)**: 
  - For `")"`, at `i = 0`, the stack pops `-1`, becomes empty, and pushes `0` as the new sentinel. `ans` remains `0`.
- **Completely Valid String (e.g., `"(())"`)**: 
  - `i = 0`: stack = `[-1, 0]`
  - `i = 1`: stack = `[-1, 0, 1]`
  - `i = 2`: pops `1`, stack = `[-1, 0]`, `ans = max(0, 2 - 0) = 2`
  - `i = 3`: pops `0`, stack = `[-1]`, `ans = max(2, 3 - (-1)) = 4`. Correctly evaluates to `4`.

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
