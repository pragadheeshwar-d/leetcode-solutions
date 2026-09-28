# 20. Valid Parentheses

## Problem
Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid. A string is valid if every opening bracket is closed by the same type of bracket, brackets are closed in the correct order, and every closing bracket matches an opening bracket.

## Approach
The submitted solution uses a stack-based matching approach (`std::stack<char> st`). Because valid parentheses follow a Last-In, First-Out (LIFO) order of nesting, a stack is used to keep track of unclosed opening brackets:
- As the string is scanned character by character, opening brackets (`'('`, `'{'`, `'['`) are pushed onto `st`.
- When a closing bracket (`')'`, `'}'`, `']'`) is encountered:
  1. The code verifies that the stack is not empty (which would mean a closing bracket appeared without any prior opening bracket).
  2. The most recent opening bracket is inspected and removed using `st.top()` and `st.pop()`.
  3. The closing bracket `c` is checked against the popped bracket `t` to verify that they are of matching types.
- At the end of the iteration, the string is valid if and only if all opening brackets have been matched, which corresponds to `st.empty()`.

## How the Solution Works
1. An auxiliary stack of characters, `st`, is initialized to store opening brackets.
2. A range-based for loop iterates through each character `c` in the string `s`:
   - If `c == '(' || c == '{' || c == '['`:
     - The bracket `c` is pushed onto `st` via `st.push(c)`.
   - Else (meaning `c` is one of `')'`, `'}'`, or `']'`):
     - `if (st.empty()) return false;`: If there are no open brackets in `st` to match with `c`, the string is immediately invalid.
     - `char t = st.top(); st.pop();`: The most recently added open bracket is retrieved into `t` and removed from `st`.
     - The condition checks if the pairs do not match:
       - `(c == ')' && t != '(')`
       - `(c == '}' && t != '{')`
       - `(c == ']' && t != '[')`
       If any of these conditions are true, `return false;`.
3. After the loop completes, the function returns the evaluation of `st.empty()`. If unclosed opening brackets remain in `st`, it evaluates to `false`; otherwise, it evaluates to `true`.

## Algorithm
1. Initialize an empty stack of characters `st`.
2. For each character `c` in the string `s`:
   1. If `c` is `'('`, `'{'`, or `'['`, push `c` onto `st`.
   2. Otherwise (`c` is a closing bracket):
      1. If `st` is empty, return `false`.
      2. Set `t` to the top element of `st`, then pop `st`.
      3. If `c` does not match the corresponding type of `t` (i.e., `')'` with `'('`, `'}'` with `'{'`, or `']'` with `'['`), return `false`.
3. Return `true` if `st` is empty, or `false` if `st` still contains unmatched opening brackets.

## Why This Works
Bracket balancing exhibits an optimal substructure governed by LIFO ordering: any closing bracket must match the most recently seen unmatched opening bracket. 
- By pushing opening brackets to `st`, the top element `st.top()` always represents the innermost active scope.
- When a closing bracket is processed, comparing it against `st.top()` guarantees that brackets close in the correct nested order.
- Checking `st.empty()` when a closing bracket appears prevents underflow and detects unmatched closing brackets.
- Checking `st.empty()` at the end ensures that strings with leftover opening brackets (e.g., `"("` or `"(()"`) evaluate to `false`.

## Complexity

### Time Complexity
$O(n)$ — Let $n$ be the length of the string `s`. The algorithm iterates through the string of length $n$ exactly once via `for (char c : s)`. In each iteration, the operations performed (stack `push`, `pop`, `top`, `empty`, and character equality checks) take $O(1)$ time. Thus, the total time complexity is $O(n)$.

### Space Complexity
$O(n)$ — In the worst-case scenario (e.g., when the string consists entirely of opening brackets like `"((((("`), all $n$ characters are pushed onto the stack `st`. Therefore, the auxiliary memory used by `st` is at most $n$ characters, resulting in $O(n)$ auxiliary space complexity.

## Edge Cases
- **Single character string (e.g., `"("` or `")"`):** 
  - If `s = "("`, the loop finishes and returns `st.empty()`, which evaluates to `false`.
  - If `s = ")"`, `st.empty()` is true on the first iteration, immediately returning `false`.
- **Closing bracket before any opening bracket (e.g., `")("`):**
  - On the first character `')'`, `st.empty()` evaluates to `true`, causing an early exit returning `false`.
- **Mismatched types (e.g., `"(]"`):**
  - `'('` is pushed. When `']'` is encountered, `t` is `'('`. The condition `(c == ']' && t != '[')` evaluates to `true`, returning `false`.
- **Interleaved/misordered brackets (e.g., `"([)]"`):**
  - `'('` and `'['` are pushed. When `')'` is encountered, `t` is `'['`. Since `t != '(' `, it returns `false`.
- **Unclosed brackets at the end (e.g., `"(()"`):**
  - All matching steps succeed, but one `'('` remains in `st`. The final check `st.empty()` correctly evaluates to `false`.

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
