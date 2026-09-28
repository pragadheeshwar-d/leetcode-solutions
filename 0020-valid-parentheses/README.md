# 20. Valid Parentheses

## Problem
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the input string is valid. A string is considered valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every closing bracket has a corresponding open bracket of the exact same type.

## Approach
The submitted solution utilizes a Last-In, First-Out (LIFO) stack data structure (`std::stack<char> st`). 

Because matching bracket pairs require that the most recently opened bracket must be the first one closed, the code iterates sequentially through each character `c` of string `s`:
- When an opening bracket (`'('`, `'{'`, or `'['`) is encountered, it is pushed onto `st`.
- When a closing bracket (`')'`, `'}'`, or `']'`) is encountered, the algorithm checks if the stack is empty (which indicates an unmatched closing bracket). If not empty, it pops the top element `t` and checks whether `t` matches the corresponding opening bracket for `c`. If it does not match, the string is invalid.
- After processing all characters, the string is valid if and only if the stack is completely empty.

## How the Solution Works
1. `stack<char> st;` is initialized to store unmatched opening bracket characters.
2. A range-based `for` loop iterates through each character `c` in the string `s`:
   - `if (c == '(' || c == '{' || c == '[')`: If `c` is an opening bracket, `st.push(c);` places it onto the stack.
   - `else`: When `c` is a closing bracket:
     - `if (st.empty()) return false;`: If the stack has no open brackets to match against, the string is invalid, immediately returning `false`.
     - `char t = st.top();`: Reads the most recently pushed opening bracket.
     - `st.pop();`: Removes that bracket from the stack.
     - The code validates bracket compatibility using:
       ```cpp
       if ((c == ')' && t != '(') ||
           (c == '}' && t != '{') ||
           (c == ']' && t != '[')) {
           return false;
       }
       ```
       If the popped character `t` does not match the closing bracket `c`, `false` is returned immediately.
3. `return st.empty();`: After scanning all characters in `s`, the function checks if any opening brackets remain unclosed. If `st` is empty, it returns `true`; otherwise, it returns `false`.

## Algorithm
1. Initialize an empty stack of characters `st`.
2. For each character `c` in `s`:
   1. If `c` is `'('`, `'{'`, or `'['`, push `c` onto `st`.
   2. Otherwise (when `c` is a closing bracket):
      1. If `st` is empty, return `false`.
      2. Retrieve the top character `t = st.top()` and pop it using `st.pop()`.
      3. If `c` is `')'` and `t != '('`, return `false`.
      4. If `c` is `'}'` and `t != '{'`, return `false`.
      5. If `c` is `']'` and `t != '['`, return `false`.
3. After the loop terminates, return `true` if `st.empty()` evaluates to `true`, otherwise return `false`.

## Why This Works
Bracket matching follows a strictly nested structure. Whenever an opening bracket appears, any subsequent brackets nested inside it must be completely matched and closed before this outer bracket can close. 

A stack naturally enforces this LIFO constraint:
- Every time a closing bracket appears, it must correspond directly to the most recently opened, unclosed bracket. That bracket is guaranteed to be at the top of the stack (`st.top()`).
- If an incompatible bracket type is found at the top, or if the stack is empty when a closing bracket arrives, the nesting order is violated.
- If all closing brackets match their corresponding open brackets, the stack will be emptied. If leftover opening brackets exist at the end, `st.empty()` correctly evaluates to `false`.

## Complexity

### Time Complexity
$O(n)$ — where $n$ is the length of the string `s`. The algorithm iterates through the string of length $n$ exactly once. In each iteration, stack operations (`push`, `top`, `pop`, and `empty`) take $O(1)$ constant time. Thus, the total time complexity is linear in terms of the input length $n$.

### Space Complexity
$O(n)$ — In the worst-case scenario (e.g., when the string consists entirely of opening brackets like `(((((`), all $n$ characters are pushed onto the stack `st`, requiring auxiliary memory proportional to $n$.

## Edge Cases
- **Single Character String (e.g., `"("` or `")"`):** If it is an opening bracket `"("`, it is pushed to `st`, loop finishes, and `st.empty()` returns `false`. If it is a closing bracket `")"`, `st.empty()` is true on the first iteration and returns `false`.
- **Closing Bracket First (e.g., `"]("`):** The first character is `']'`. `st.empty()` triggers an immediate return of `false`.
- **Mismatched Bracket Types (e.g., `"(]"`):** `'('` is pushed, then on `']'`, `t` is `'('`. The condition `(c == ']' && t != '[')` evaluates to true, correctly returning `false`.
- **Properly Nested Brackets (e.g., `"([])"`):** `'('` and `'['` are pushed. When `']'` is read, it matches `t = '['` and pops it. Next, `')'` matches `t = '('` and pops it. The stack is empty at the end, correctly returning `true`.
- **Incomplete Pairs / Unclosed Brackets (e.g., `"()("`):** The final `'('` remains on the stack. `st.empty()` returns `false`.

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
