# 2778. Sum of Squares of Special Elements 

## Approach
The algorithm calculates the sum of squares of special elements in a given vector by linearly iterating through all 0-indexed positions. A element at 0-based index `i` is defined as special if the length of the array `n` is divisible by its 1-based position `i + 1`. The algorithm converts each 0-based index to a 1-based position, performs a modulo check against `n`, and if divisible, squares the element at `nums[i]` and accumulates it into a running total variable.

## How It Works
1. Initialize `index = 0` to serve as the accumulator variable for storing the final sum of squares.
2. Store the size of the input vector `nums` in variable `n`.
3. Execute a `for` loop starting from `i = 0` up to `n - 1`.
4. Within each iteration, compute the 1-based index position `i + 1` and evaluate `n % (i + 1) == 0`.
5. If `n` is evenly divisible by `i + 1`, multiply `nums[i]` by itself (`nums[i] * nums[i]`) and add the result to `index`.
6. Once the loop terminates, return `index` as the final result.

## Complexity
- **Time Complexity:** `O(n)` — The algorithm uses a single `for` loop that iterates `n` times, where `n` is the size of the input array `nums`. Inside the loop, all arithmetic operations (modulo, multiplication, and addition) take O(1) constant time, yielding an overall time complexity of O(n).
- **Space Complexity:** `O(1)` — The solution only allocates a fixed number of integer variables (`index`, `n`, `i`) regardless of the input size. No additional dynamic memory or memory-allocating data structures are used, leading to O(1) auxiliary space complexity.

## Edge Cases
- Minimum array length (n = 1): The loop runs once for i = 0 where 1 % (0 + 1) == 0 is true, correctly adding nums[0] squared.
- Array length n is a prime number: Only the first element (position 1, index 0) and the last element (position n, index n-1) satisfy the modulo condition.
- Negative numbers in nums: Squaring negative integer values yields positive products, ensuring accurate addition to the sum accumulator.

## Solution
```cpp
class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int index = 0;
        int n = nums.size();

        // i = index, counting from 0  ->  position = i + 1
        for (int i = 0; i < n; i++) {
            if (n % (i + 1) == 0) {
                index += nums[i] * nums[i];
            }
        }
        return index;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/2778-sum-of-squares-of-special-elements/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Sum of Squares of Special Elements ](https://leetcode.com/problems/sum-of-squares-of-special-elements/)
