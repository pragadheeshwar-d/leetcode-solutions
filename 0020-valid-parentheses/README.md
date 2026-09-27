# 20. Valid Parentheses

## Problem

# 20. Valid Parentheses

- **Difficulty:** Easy
- **URL:** https://leetcode.com/problems/valid-parentheses/
- **Language:** C++

## Problem Description

<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input s...

## Approach

The solution maintains a LIFO stack to validate bracket nesting. It iterates through the string, pushing opening brackets onto the stack. When encountering a closing bracket, it verifies that the stack is non-empty and that the top element matches the corresponding opening bracket type before popping it. Finally, it confirms that all brackets were matched by verifying the stack is empty.

## How the Solution Works

1. **Stack Initialization:** Maintain a LIFO stack (`st`) to store encountered opening brackets.
2. **Character Inspection:** Iterate over each character `c` in string `s`.
3. **Push Phase:** If `c` is an opening bracket (`(`, `{`, `[`), push it onto `st`.
4. **Match & Pop Phase:** If `c` is a closing bracket, verify `!st.empty()` and check if `st.top()` matches `c`. If matched, pop `st`; otherwise return `false`.
5. **Final Validation:** Return `st.empty()` ensuring no unclosed opening brackets remain.

## Algorithm

1. Initialize an empty character stack `st`.
2. For each character `c` in string `s`:
3.   - If `c` is `'('`, `'{'`, or `'['`: push `c` onto `st`.
4.   - Else: if `st.empty()`, return `false`; get `top = st.top()`; `st.pop()`; if `top` does not match `c`, return `false`.
5. Return `st.empty()`.

## Why This Works

In any well-formed bracket sequence, opening and closing delimiters obey strict hierarchical nesting: the most recently opened bracket must be the first one closed. A LIFO stack preserves this temporal order with O(1) push and pop operations, enabling a single-pass O(n) validation with zero backtracking.

## Complexity

### Time Complexity

`O(n)` — Where n is the length of the string. Each character is pushed onto and popped from the stack at most once.

### Space Complexity

`O(n)` — Auxiliary stack memory. In the worst case (e.g. all opening brackets), the stack stores up to n elements.

## Edge Cases

- **Closing Bracket First:** An input starting with a closing bracket (e.g. `"]"` or `")("`) detects an empty stack on the first pop attempt and returns `false` immediately.
- **Mismatched Types:** Nested brackets of different types (e.g. `"(]"` or `"{[}]"`) fail the top-of-stack equality check and return `false`.
- **Unclosed Opening Brackets:** Inputs with leftover opening brackets (e.g. `"("`, `"(()"`) leave items on the stack, causing `st.empty()` to evaluate to `false`.
- **Odd String Length:** A balanced sequence must have an even number of delimiters; an odd length can never be valid.

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
