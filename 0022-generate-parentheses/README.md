# 22. Generate Parentheses

## Approach
1. **Stack Initialization:** Maintain a LIFO stack (`st`) to store encountered opening brackets.
2. **Character Inspection:** Iterate over each character `c` in the string `s`.
3. **Push Opening Brackets:** If `c` is an opening bracket (`'('`, `'{'`, or `'['`), push it onto the stack.
4. **Validate Closing Brackets:** If `c` is a closing bracket, verify that the stack is non-empty and that the top element matches the corresponding opening bracket type (`st.top()`, `st.pop()`). If empty or mismatched, return `false`.
5. **Final Balance Check:** After scanning all characters, return `st.empty()` to verify no unclosed opening brackets remain.

## How It Works
The algorithm enforces bracket nesting rules using a Last-In, First-Out (LIFO) stack:
- **LIFO Invariant:** The most recently opened bracket must be the first one closed. A stack naturally preserves this temporal ordering.
- **Push Phase:** Every opening character (`'('`, `'{'`, `'['`) is pushed onto the stack to await its closing partner.
- **Pop & Match Phase:** When a closing character (`')'`, `'}'`, `']'`) arrives, the algorithm inspects the top element (`st.top()`). If the stack is empty (closing bracket without an opener) or the top element does not match the expected type, the expression violates syntactic nesting and returns `false` immediately.
- **Final Validation:** Returning `st.empty()` ensures no opening brackets were left unclosed at the end of the string.

## Complexity
- **Time Complexity:** `O(n)` — Where n is the length of the string. Each character is pushed onto and popped from the stack at most once.
- **Space Complexity:** `O(n)` — Auxiliary stack memory. In the worst case (e.g. all opening brackets), the stack stores up to n elements.

## Edge Cases
- **Premature Closing Bracket:** An input starting with a closing bracket (e.g. `"]"` or `")("`) detects an empty stack on the first pop attempt and returns `false` immediately.
- **Mismatched Types:** Nested brackets of different types (e.g. `"(]"` or `"{[}]"`) fail the top-of-stack equality check and return `false`.
- **Unclosed Brackets:** Trailing unmatched opening brackets (e.g. `"(("` or `"()("`) leave elements on the stack, causing `st.empty()` to evaluate to `false`.
- **Odd String Length:** A balanced sequence must have an even number of delimiters; an odd length can never be valid.

## Solution
```cpp
class Solution {
public:
    vector<string> ans;
    void preOrder(int lp, int rp, int level, string&& fromRoot, int n){
        if (lp==n && rp==n && level==0) 
            ans.push_back(fromRoot);
        if (lp<n) 
            preOrder(lp+1, rp,  level+1 ,fromRoot+"(", n);
        if (rp<n && level>=1) 
            preOrder(lp, rp+1,  level-1 ,fromRoot+")", n);     
    }
    vector<string> generateParenthesis(int n) {
        ans.reserve(n<<1);
        preOrder(1, 0, 1, "(", n);
        return ans;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0022-generate-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
