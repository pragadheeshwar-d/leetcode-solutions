# 301. Remove Invalid Parentheses

## Approach
The solution uses recursive backtracking based on prefix bracket counting to remove the minimum number of invalid parentheses. It scans the string left-to-right using a counter to track the balance of open and close brackets. If an invalid excess closing bracket causes the balance to drop below zero, the algorithm branches by trying to delete each possible closing bracket encountered up to that point. Duplicate deletions within consecutive identical brackets are skipped to prevent redundant processing and duplicate result generation. After resolving excess closing brackets, the string is reversed and the exact same algorithm is executed to handle excess opening brackets.

## How It Works
The core helper function `remove` takes parameters `(s, scanStart, deleteStart, open, close, answers)`.
1. **Scanning**: It iterates `i` from `scanStart` to `s.size() - 1`, updating `balance` (+1 for `open`, -1 for `close`).
2. **Handling Imbalance**: If `balance < 0`, an excess `close` bracket exists in the prefix `s[0...i]`. To fix this, it iterates `j` from `deleteStart` to `i` looking for candidate `close` characters. To avoid generating duplicate combinations, it only removes `s[j]` if `j == deleteStart` or `s[j - 1] != close`.
3. **Branching**: For each valid candidate, it constructs a new string `s.substr(0, j) + s.substr(j + 1)` and recursively calls `remove` with `scanStart = i` and `deleteStart = j`. It then terminates the loop via `return` because further scanning without fixing the current prefix violation is invalid.
4. **Reversal & Dual Pass**: If the scan completes without `balance` dropping below 0, all excess `close` brackets are handled. The string `s` is then reversed. If `open == '('`, the algorithm calls `remove` again with `open = ')'` and `close = '('` to eliminate excess opening brackets. If `open == ')'`, both passes are complete and the valid string `s` is added to `answers`.

## Complexity
- **Time Complexity:** `O(N · 2ᴺ)` — In the worst-case scenario (e.g., a string consisting entirely of identical parentheses like `"((((("` or `")))))"`), the algorithm branches for every possible removal position. The duplicate-checking condition reduces duplicate search paths, but the total number of states explored remains bounded by O(2ᴺ). At each recursive call, string concatenation and substring operations take O(N) time, leading to an overall worst-case time complexity of O(N · 2ᴺ).
- **Space Complexity:** `O(N²)` — The maximum depth of the recursion tree is bounded by the string length O(N). At each recursive frame, pass-by-value string operations (`s.substr`) create string copies of size up to O(N). Across O(N) active call stack frames, the peak auxiliary memory usage is O(N²), excluding the output vector.

## Edge Cases
- An empty input string s = "".
- A string with no parentheses containing only non-bracket characters (e.g., "abc").
- A string consisting only of unmatched opening brackets (e.g., "(((") or closing brackets (e.g., ")))").
- A string that is already fully balanced (e.g., "()()").
- A string with consecutive identical invalid parentheses (e.g., "(())") to test duplicate suppression.

## Solution
```cpp
class Solution {
    void remove(string s, int scanStart, int deleteStart, char open, char close,
                vector<string>& answers) {
        int balance = 0;

        for (int i = scanStart; i < (int)s.size(); i++) {
            if (s[i] == open) {
                balance++;
            } else if (s[i] == close) {
                balance--;
            }

            if (balance >= 0) {
                continue;
            }

            for (int j = deleteStart; j <= i; j++) {
                if (s[j] == close && (j == deleteStart || s[j - 1] != close)) {
                    remove(s.substr(0, j) + s.substr(j + 1), i, j, open, close,
                           answers);
                }
            }

            return;
        }

        reverse(s.begin(), s.end());

        if (open == '(') {
            remove(s, 0, 0, ')', '(', answers);
        } else {
            answers.push_back(s);
        }
    }

public:
    vector<string> removeInvalidParentheses(string s) {
        vector<string> answers;
        remove(s, 0, 0, '(', ')', answers);
        return answers;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/0301-remove-invalid-parentheses/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)
