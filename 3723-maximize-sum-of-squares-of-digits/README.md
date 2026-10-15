# 3723. Maximize Sum of Squares of Digits

## Approach
Greedy approach. To maximize the sum of squares of digits for a target digit sum with a fixed length of `num` digits, larger digits (specifically 9s) are placed first. The code calculates the maximum number of 9s possible, appends the single remainder digit to achieve the exact target sum, and pads the remaining positions with 0s.

## How It Works
1. Check if `sum > 9 * num`. If true, the target sum cannot be formed with `num` digits, so it returns `""`.
2. Calculate `nines = sum / 9` to determine the count of '9' digits.
3. Calculate `rest = sum % 9` to find the single digit needed to complete the target sum.
4. Form a string by concatenating `nines` '9' characters, the character representation of `rest` (`char('0' + rest)`), and `num` '0' characters for safety padding.
5. Call `.substr(0, num)` on the concatenated string to truncate it to the exact required length `num`.

## Complexity
- **Time Complexity:** `O(num)` — Constructing the constituent strings of lengths proportional to `num` and taking a substring of length `num` performs $O(\text{num})$ operations.
- **Space Complexity:** `O(num)` — Constructing intermediate string instances (`string(nines, '9')`, `string(num, '0')`, and the concatenated string) requires $O(\text{num})$ auxiliary memory.

## Edge Cases
- When `sum > 9 * num`, it is impossible to satisfy the digit sum constraint, returning `""` immediately.
- When `sum` is an exact multiple of 9, `rest` is 0; taking `.substr(0, num)` seamlessly handles the trailing digits without exceeding `num` digits.
- When `sum` is 0, `nines` and `rest` are both 0, producing a string composed entirely of `num` '0's.

## Solution
```cpp
class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9 * num) 
            return "";  
        int nines = sum / 9, rest = sum % 9;
        return (string(nines, '9') + char('0' + rest) + string(num, '0')).substr(0, num); 
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/3723-maximize-sum-of-squares-of-digits/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Maximize Sum of Squares of Digits](https://leetcode.com/problems/maximize-sum-of-squares-of-digits/)
