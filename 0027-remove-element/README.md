# 27. Remove Element

## Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the remaining elements may be changed. Return `k`, the number of elements in `nums` that are not equal to `val`. The first `k` elements of `nums` must hold the resulting elements.

## Approach
The submitted solution utilizes a two-pointer technique—specifically a reader-writer pointer approach—to filter the array in-place without allocating auxiliary memory:
- A write pointer `k` tracks the position where the next valid element (an element not equal to `val`) should be placed.
- A read pointer `i` traverses the array from index `0` to `nums.size() - 1`.
- When an element `nums[i]` is not equal to `val`, it is copied to `nums[k]`, and `k` is incremented.
- Elements equal to `val` are skipped by `i` without advancing `k`.

## How the Solution Works
1. An integer variable `k` is initialized to `0`. This serves as both the writer index and the counter of elements preserved.
2. A `for` loop iterates through the entire vector using index `i` from `0` up to `nums.size() - 1`.
3. In each iteration:
   - The condition `if (nums[i] != val)` evaluates whether the current element should be kept.
   - If `nums[i]` does not equal `val`:
     - `nums[k] = nums[i];` overwrites the element at index `k` with the current element `nums[i]`. If `k == i`, the element is simply assigned to itself.
     - `k++;` advances the write pointer to the next position.
   - If `nums[i] == val`:
     - The branch is skipped. `k` does not increment, meaning subsequent valid elements will overwrite this index.
4. After the loop terminates, the first `k` slots of `nums` contain all elements from the original array that are not equal to `val`.
5. The function returns `k`.

## Algorithm
1. Initialize `k = 0`.
2. For each index `i` from `0` to `nums.size() - 1`:
   1. Check if `nums[i] != val`.
   2. If true:
      1. Assign `nums[k] = nums[i]`.
      2. Increment `k` by `1`.
3. Return `k`.

## Why This Works
The correctness of this algorithm is established by the loop invariant:
- At the start of iteration `i`, the subarray `nums[0 ... k - 1]` contains all elements from `nums[0 ... i - 1]` that are not equal to `val`, maintaining their relative order.
- Since `k <= i` holds at all times, the write operation `nums[k] = nums[i]` will never overwrite an unread element from `nums[i ... n - 1]`.
- Upon loop termination (`i = nums.size()`), all elements in `nums` have been processed, and `nums[0 ... k - 1]` contains every non-`val` element. The integer `k` correctly represents the count of such elements.

## Complexity
### Time Complexity
`O(n)` — where `n` is the length of `nums` (`nums.size()`). The loop executes exactly `n` times. Inside the loop, the comparison `nums[i] != val`, the assignment `nums[k] = nums[i]`, and the increments run in `O(1)` constant time. Thus, the total time is linear with respect to the input size.

### Space Complexity
`O(1)` — The algorithm operates strictly in-place. It only allocates two integer variables (`k` and `i`) on the stack, requiring no additional dynamic memory regardless of `nums.size()`.

## Edge Cases
- **Empty Array (`nums.size() == 0`):** The loop condition `i < nums.size()` is false initially. The loop body does not execute, and `k = 0` is returned immediately.
- **All Elements Equal to `val`:** The condition `nums[i] != val` evaluates to false for all `i`. The pointer `k` is never incremented, leaving `k = 0`, which is correctly returned.
- **No Elements Equal to `val`:** The condition `nums[i] != val` evaluates to true for every element. Every element is written to `nums[k]` (where `k == i`), and `k` reaches `nums.size()`.
- **Single-Element Vector:**
  - If `nums[0] == val`, `k` remains `0`.
  - If `nums[0] != val`, `nums[0]` is written to `nums[0]`, `k` becomes `1`, and `1` is returned.

## Solution

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
};
```
