# 2778. Sum of Squares of Special Elements 

## Approach
The solution performs a single-pass linear iteration over the array to compute the sum of squares of special elements. An element is defined as 'special' if its 1-based position divides the length of the array `n` without a remainder. The implementation uses a simple loop and modulo arithmetic to test this condition and accumulates the squared values.

## How It Works
1. The function determines the array size `n = nums.size()` and initializes an accumulator variable named `index` to `0` to store the running total.
2. It iterates through the vector using a zero-based index `i` from `0` up to `n - 1`.
3. In each iteration, it checks if `i + 1` (the 1-based position) divides `n` evenly using the modulo operator: `n % (i + 1) == 0`.
4. If the condition evaluates to true, `nums[i]` is squared (`nums[i] * nums[i]`) and added to the accumulator variable `index`.
5. Once the loop completes, the function returns `index` as the final sum.

## Complexity
- **Time Complexity:** `O(n)` —  layout: The loop executes precisely `n` times, where `n` is the number of elements in `nums`. Inside the loop, computing `i + 1`, the modulo operation `n % (i + 1)`, integer multiplication, and addition all take O(1) constant time, leading to an overall linear time complexity of O(n).
- **Space Complexity:** `O(1)` — The algorithm only uses a fixed number of scalar integer variables (`index`, `n`, and `i`) regardless of the size of the input vector, requiring constant extra memory.

## Edge Cases
- Single-element vector (n = 1): `i + 1 = 1` always divides `1`, so `nums[0] * nums[0]` is correctly computed and returned.
- Array length `n` is a prime number: Only the first element (position 1) and the last element (position `n`) will satisfy the divisibility condition.
- Array contains duplicate or zero elements: Modulo indexing relies solely on the array length `n` and loop index `i`, unaffected by element values.

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
