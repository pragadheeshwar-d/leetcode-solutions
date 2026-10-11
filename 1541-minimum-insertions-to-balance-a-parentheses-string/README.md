# 1541. Minimum Insertions to Balance a Parentheses String

## Approach
The algorithm uses a greedy approach with a single linear scan to count the required insertions. It maintains variable `p`, which represents the number of missing closing parentheses `)` currently needed to achieve balance, and variable `k`, which tracks the total number of insertions made during the iteration. Each open parenthesis `(` adds 2 to `p`. If an open parenthesis is encountered when `p` is odd, a `)` must be inserted immediately before it to complete a pair. If a closing parenthesis `)` causes `p` to become negative, a `(` is inserted immediately.

## How It Works
1. Initialize `p = 0` (count of needed `)` closing parentheses), `n = s.size()`, and `k = 0` (count of insertions).
2. Iterate through each character `c` in `s` using index `i`:
   - If `c == '('`:
     - Add 2 to `p` (`p += 2`), as each `(` requires two `)`.
     - Check if `p` was odd prior to adding 2 using `if (p & 1 == 1)`. In C++, `==` has higher precedence than `&`, so `1 == 1` evaluates to `true` (1), turning the expression into `p & 1` which tests if `p` is odd. An odd `p` means an isolated `)` was waiting for its pair. We insert a `)` by incrementing `k++` and decrementing `p--`.
   - If `c == ')'`:
     - Decrement `p` by 1 (`p--`).
     - If `p < 0` (meaning `p` hit -1, an unmatched `)`), insert a `(` before it: increment insertion count `k++` and balance `p` by adding 2 (`p += 2`), making `p = 1` (since one `)` of the newly inserted `(`'s required pair is fulfilled by the current character).
3. After the loop, return `p + k`, where `p` accounts for any remaining `)` insertions needed at the end of the string.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm processes the input string `s` of length `n` in a single `for` loop. Inside the loop, all arithmetic, bitwise, and conditional operations run in O(1) constant time.
- **Space Complexity:** `O(1)` — The implementation only uses a constant number of integer and character variables (`p`, `n`, `k`, `i`, `c`) and modifies no external memory, using O(1) auxiliary space.

## Edge Cases
- Isolated closing parenthesis `)` with no preceding open parenthesis, triggering `p < 0` to insert a `(` and leaving `p = 1` for the final answer.
- Unmatched open parentheses at the end of the string, e.g., `"((("`, where `p` accumulates the needed `)` insertions which are added to `k` at the end.
- A single `)` right before a `(`, e.g., `")( "`, where the odd state of `p` before processing `(` triggers an immediate `)` insertion.

## Solution
```cpp
class Solution {
public:
    int minInsertions(string& s) {
        int p=0, n=s.size(), k=0;
        for(int i=0; i<n; i++){
            char c=s[i];
            if (c=='('){
                p+=2;
                if (p&1==1){
                    k++;
                    p--;
                }
            }
            else{
                p--;
                if (p<0){
                    k++;
                    p+=2;
                }
               
            }
        }
        return p+k;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/1541-minimum-insertions-to-balance-a-parentheses-string/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)
