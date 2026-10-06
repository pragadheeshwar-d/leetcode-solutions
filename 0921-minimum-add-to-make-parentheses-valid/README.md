# 921. Minimum Add to Make Parentheses Valid

## Approach
The solution uses a greedy single-pass counter approach (simulating a stack without extra memory) to count unmatched opening and closing parentheses.

## How It Works
Two integer variables, `l` and `r`, are initialized to `0`. Variable `r` tracks the number of unmatched opening parentheses `(`, while `l` tracks unmatched closing parentheses `)`. The code iterates through each character `c` in string `s`: if `c == '('`, `r` is incremented. If `c == ')'`, the code checks if `r > 0` (meaning a previous `(` is available to pair with this `)`); if so, `r` is decremented. Otherwise, if `r == 0`, the `)` is unmatched, so `l` is incremented. At the end of the loop, `l + r` gives the total number of missing parentheses needed to make the string valid.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm processes the input string `s` of length `n` in a single pass. Each character inspection and counter update occurs in O(1) constant time, leading to a linear time complexity of O(n).
- **Space Complexity:** `O(1)` — Only two integer counters (`l` and `r`) are used for state tracking. No auxiliary data structures or dynamic memory allocations are performed, keeping space usage constant at O(1).

## Edge Cases
- Empty string (`s = ""`): The loop does not execute and returns `0` correctly.
- All opening parentheses (`s = "((("`): `r` accumulates to 3 and `l` stays 0, returning `3` additions required.
- All closing parentheses (`s = ")))"`): `l` accumulates to 3 and `r` stays 0, returning `3` additions required.
- Reverse valid order (`s = ")("`): The closing parenthesis increments `l` to 1, and the opening parenthesis increments `r` to 1, correctly yielding `2` additions required.

## Solution
```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int l=0,r=0;
        for(char c:s){
            if(c=='('){
                r++;
            }
            else if(c==')'){
                if(r>0) r--;
                else l++;
            }
        }
        return l+r;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0921-minimum-add-to-make-parentheses-valid/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
