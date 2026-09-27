# 9. Palindrome Number

## Problem

Given the input constraints for Palindrome Number, compute the optimal result.

## Approach

The solution arithmetically reverses the decimal digits of the integer without converting it to a string. It checks for negative numbers (which cannot be palindromic due to the minus sign), extracts the least significant digit via modulo `% 10`, accumulates it into a reversed accumulator by multiplying by 10, and strips the digit via integer division `/= 10` until exhaustion.

## How the Solution Works

1. **Negative Guard:** If `x < 0`, returns `false` immediately because leading negative signs break symmetry.
2. **State Setup:** Tracks a copy of the input (`n`) and a reversal accumulator (`r`).
3. **Digit Reversal:** Evaluates `n % 10` to isolate the rightmost digit, appends it to `r` via `r = r * 10 + n % 10`, and shrinks `n` via `n /= 10`.
4. **Comparison:** Once `n == 0`, compares original `x` with `r` (`x == r`).

## Algorithm

1. Check if `x < 0`; if true, return `false`.
2. Initialize working variable `n = x` and accumulator `r = 0`.
3. While `n != 0`: update `r = r * 10 + n % 10` and `n /= 10`.
4. Return boolean comparison `x == r`.

## Why This Works

A palindrome reads identically forwards and backwards. By arithmetically reconstructing the integer in reverse order using base-10 positional weighting, `r` represents the exact numerical value read backward. If `x == r`, the decimal digits are strictly symmetrical.

## Complexity

### Time Complexity

`O(log₁₀ x)` — Where x is the input integer. The number is divided by 10 in each iteration, executing at most ⌊log₁₀ x⌋ + 1 times (the number of decimal digits).

### Space Complexity

`O(1)` — Constant auxiliary space; only scalar integer variables are maintained without allocating external containers.

## Edge Cases

- **Negative numbers (`x < 0`):** Always return `false` (e.g. `-121` reversed is `121-`).
- **Zero (`x = 0`):** Single digit, correctly returns `true`.
- **Multiples of 10 (`x > 0 && x % 10 == 0`):** Trailing zeros cannot match leading digits; returns `false`.
- **Integer Overflow:** Using a 64-bit integer (`long long`) for the accumulator prevents 32-bit signed arithmetic overflow.

## Solution

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        int revertedNumber = 0;
        while (x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        return x == revertedNumber || x == revertedNumber / 10;
    }
};
```
