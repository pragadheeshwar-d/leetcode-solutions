# 9. Palindrome Number

## Problem
Given an integer `x`, determine whether it is a palindrome. An integer is a palindrome when it reads the same backward as forward (e.g., `121` is a palindrome, while `-121` and `10` are not).

## Approach
The algorithm checks whether `x` is a palindrome by reversing only the second half of its digits and comparing that reversed half directly to the remaining first half. 

Reversing only half of the digits avoids potential 32-bit signed integer overflow that could occur if the entire integer were reversed.

## How the Solution Works
1. **Initial Validation Guard:**
   ```cpp
   if (x < 0 || (x % 10 == 0 && x != 0)) {
       return false;
   }
   ```
   - Negative numbers cannot be palindromes due to the leading negative sign (`-`).
   - Any positive number that ends in `0` cannot be a palindrome because no positive number starts with `0`. The number `0` itself is an exception and is treated as a palindrome.

2. **Half-Number Reversal Loop:**
   ```cpp
   int revertedNumber = 0;
   while (x > revertedNumber) {
       revertedNumber = revertedNumber * 10 + x % 10;
       x /= 10;
   }
   ```
   - A variable `revertedNumber` is initialized to `0`.
   - The loop runs while `x > revertedNumber`. In each iteration:
     - The last digit of `x` is obtained via `x % 10` and appended to `revertedNumber` using `revertedNumber * 10 + x % 10`.
     - The last digit is removed from `x` using integer division `x /= 10`.
   - When `x <= revertedNumber`, exactly half (or slightly more than half, for numbers with an odd number of digits) of the digits have been moved to `revertedNumber`.

3. **Equality Check:**
   ```cpp
   return x == revertedNumber || x == revertedNumber / 10;
   ```
   - If the total number of digits is even, `x` and `revertedNumber` will be equal if the input is a palindrome (e.g., `1221` results in `x = 12` and `revertedNumber = 12`).
   - If the total number of digits is odd, the middle digit ends up as the least significant digit of `revertedNumber`. Dividing `revertedNumber` by `10` discards this middle digit, allowing direct comparison with `x` (e.g., `12321` results in `x = 12` and `revertedNumber = 123`; `123 / 10 == 12`).

## Algorithm
1. Check if `x < 0` or if `x` ends in `0` while not being `0`. If either condition is true, return `false`.
2. Initialize `revertedNumber` to `0`.
3. While `x > revertedNumber`:
   a. Extract the least significant digit of `x` (`x % 10`) and shift it into `revertedNumber`.
   b. Divide `x` by `10`.
4. Return `true` if `x == revertedNumber` or `x == revertedNumber / 10`; otherwise, return `false`.

## Why This Works
A decimal integer of $d$ digits can be split into two halves: the upper $\lfloor d/2 \rfloor$ digits and the lower $\lfloor d/2 \rfloor$ digits (with an optional single middle digit when $d$ is odd). 

By successively extracting digits from the least significant side of `x` and appending them to `revertedNumber`, `revertedNumber` builds the lower half in reverse order. The loop condition `x > revertedNumber` terminates precisely when at least half of the digits have been processed. 

- For even-length palindromes, both halves must match identically: `x == revertedNumber`.
- For odd-length palindromes, the middle digit does not affect symmetry; dividing `revertedNumber` by `10` discards it, after which the remaining halves must match: `x == revertedNumber / 10`.

## Complexity

### Time Complexity
$O(\log_{10} x)$ — The total number of decimal digits in $x$ is $\lfloor \log_{10} x \rfloor + 1$. In each iteration of the `while` loop, $x$ is divided by $10$ and `revertedNumber` is multiplied by $10$. The loop terminates when approximately half the digits have been processed, running in $\approx \frac{1}{2} \log_{10} x$ iterations. Each iteration performs $O(1)$ arithmetic operations.

### Space Complexity
$O(1)$ — The algorithm uses a fixed amount of auxiliary memory: a single integer variable `revertedNumber`, requiring constant additional space.

## Edge Cases
- **Negative numbers (e.g., `-121`):** Caught by `x < 0` and immediately returns `false`.
- **Zero (`0`):** Bypasses the condition `(x % 10 == 0 && x != 0)`. The `while` loop condition `0 > 0` is false, and it returns `0 == 0`, which evaluates to `true`.
- **Multiples of 10 (e.g., `10`, `100`):** Caught by `x % 10 == 0 && x != 0` and returns `false`.
- **Single-digit positive numbers (e.g., `7`):** Does not trigger the initial guard. In the loop, `7 > 0`, so `revertedNumber` becomes `7` and `x` becomes `0`. The loop terminates because `0 > 7` is false. The return condition evaluates `0 == 7 / 10` ($0 == 0$), which evaluates to `true`.

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
