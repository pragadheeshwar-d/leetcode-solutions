# 20. Valid Parentheses

## Problem
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the string is valid. A string is valid if open brackets are closed by the exact same type of closing brackets in the correct order, and every closing bracket has an associated open bracket preceding it.

## Approach
The submitted solution utilizes a Last-In, First-Out (LIFO) stack of characters (`std::stack<char> st`) to track opening brackets. As the string is parsed character by character:
- Whenever an opening bracket (`'('`, `'{'`, or `'['`) is encountered, it is pushed onto the stack.
- Whenever a closing bracket (`')'`, `'}'`, or `']'`) is encountered, the algorithm checks if there is a matching opening bracket at the top of the stack. If the stack is empty or the top character does not correspond to the current closing bracket, the string is immediately determined to be invalid.
- At the end of the iteration, if the stack is completely empty, all opened brackets were properly matched and closed.

## How the Solution Works
1. A stack `st` of type `char` is initialized: `stack<char> st;`.
2. A range-based `for` loop iterates through each character `c` in the string `s`:
   - If `c` is `'('`, `'{'`, or `'['`, `st.push(c)` is executed, storing the opening bracket for future pairing.
   - Otherwise, `c` must be a closing bracket:
     - The code checks `if (st.empty()) return false;`. If true, there is a closing bracket without any preceding unmatched opening bracket, so it returns `false`.
     - The top bracket is retrieved into variable `t` using `char t = st.top();` and immediately removed with `st.pop();`.
     - The code verifies matching pairs:
       - `(c == ')' && t != '(')`
       - `(c == '}' && t != '{')`
       - `(c == ']' && t != '[')`
       If any of these conditions are met, there is a bracket mismatch, and the function returns `false`.
3. After the loop completes, the function evaluates `return st.empty();`. If opening brackets remain on the stack without matching closing brackets, `st.empty()` evaluates to `false`. If all brackets were matched, it evaluates to `true`.

## Algorithm
1. Initialize an empty stack `st`.
2. For each character `c` in `s`:
   1. If `c` is `'('`, `'{'`, or `'['`, push `c` onto `st`.
   2. Else:
      1. If `st` is empty, return `false`.
      2. Set `t` to `st.top()` and pop the top element from `st`.
      3. If `c` and `t` do not form a matching bracket pair (`'('` with `')'`, `'{'` with `'}'`, or `'['` with `']'`), return `false`.
3. Return `true` if `st` is empty; otherwise, return `false`.

## Why This Works
The grammar of balanced parentheses requires that the most recently opened bracket must be the first one closed (a strictly nested, recursive structure). A stack inherently enforces this LIFO order. By pushing open brackets and popping them only when the matching closing bracket appears, any improper interleaving (such as `([)]`) or missing closing bracket will be caught either during the mismatch check or during the final `st.empty()` check.

## Complexity

### Time Complexity
$O(n)$ — where $n$ is the length of string `s`. The algorithm iterates through the string of length $n$ exactly once. Each character triggers either a `push` operation or a `top` and `pop` operation. Both push and pop operations on `std::stack` run in $O(1)$ amortized time, leading to an overall runtime directly proportional to $n$.

### Space Complexity
$O(n)$ — In the worst-case scenario (such as a string consisting entirely of open brackets `((((...`), all $n$ characters are pushed onto the stack `st`, requiring linear auxiliary memory.

## Edge Cases
- **Empty Stack on Closing Bracket:** A string like `"]"` or `"())"` encounters a closing bracket when `st.empty()` is `true`, returning `false` correctly without attempting an invalid top/pop operation.
- **Unclosed Opening Brackets:** A string like `"("` or `"(()"` finishes iteration with leftover elements in `st`. The final check `st.empty()` correctly evaluates to `false`.
- **Mismatched Bracket Types:** A string like `"(]"` or `"([)]"` encounters a mismatch between `c` and `t`, triggering the mismatch `return false`.

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
                    (c == ']' && t != '

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
