# 26. Remove Duplicates from Sorted Array

## Problem
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements must be kept the same. 

After modifying the array, return the number of unique elements, $k$. The first $k$ elements of the array `nums` must contain the unique elements in their original sorted order. The elements beyond the first $k$ positions do not matter.

## Approach
The code implements a **Two-Pointer** approach to modify the vector in-place. 
* A write-pointer `j` is used to keep track of the index of the last placed unique element in the vector. It is initialized to `0` because the first element of a sorted array is always unique.
* A read-pointer `i` is used to scan through the array starting from index `1` to identify new unique elements.
* When a value at the read-pointer `i` is different from the value at the write-pointer `j` (`nums[i] != nums[j]`), a new unique element has been found. The write-pointer `j` is incremented, and the value at `nums[i]` is copied to `nums[j]`.

## How the Solution Works
Let us trace the execution with an input array `nums = [1, 1, 2]`.

1. **Initialization**:
   * `j` is initialized to `0`.
   * The size of `nums` is `3`.

2. **Iteration `i = 1`**:
   * The loop condition `i < nums.size()` (`1 < 3`) is true.
   * Compare `nums[i]` with `nums[j]`: `nums[1]` is `1` and `nums[0]` is `1`.
   * Since `nums[1] != nums[0]` is false, no changes are made.

3. **Iteration `i = 2`**:
   * The loop condition `2 < 3` is true.
   * Compare `nums[2]` with `nums[j]`: `nums[2]` is `2` and `nums[0]` is `1`.
   * Since `nums[2] != nums[0]` is true:
     * `j` is incremented to `1`.
     * `nums[j]` (which is `nums[1]`) is assigned the value of `nums[i]` (which is `2`).
     * The array `nums` becomes `[1, 2, 2]`.

4. **Termination**:
   * The loop counter `i` increments to `3`. The loop condition `3 < 3` is false, and the loop terminates.
   * The function returns `j + 1`, which is `1 + 1 = 2`. The first $2$ elements of `nums` are indeed the unique elements `[1, 2]`.

## Algorithm
1. Initialize the pointer `j = 0`, which represents the index of the current last unique element.
2. Run a `for` loop with a loop variable `i` starting from `1` up to `nums.size() - 1`.
3. Inside the loop, check if the current element `nums[i]` is not equal to the last recorded unique element `nums[j]`.
4. If they are not equal:
   * Increment `j` by `1` to prepare the next available position.
   * Assign `nums[j] = nums[i]`.
5. After the loop completes, return `j + 1`, which represents the count of unique elements in the array.

## Why This Works
The array is sorted in non-decreasing order. This sorting guarantee ensures that all duplicate values of any element are located adjacent to each other. 

By comparing the scanning element `nums[i]` with the last confirmed unique element `nums[j]`, we can determine if `nums[i]` is a duplicate. If it differs from `nums[j]`, it must be strictly greater than `nums[j]` and thus a brand-new unique value. Copying it to `nums[j + 1]` shifts all unique elements to the front of the array while maintaining their relative sorted order.

## Complexity

### Time Complexity
`O(n)` — where $n$ is the number of elements in the vector `nums`. 
The algorithm uses a single loop where the index `i` starts at `1` and increments sequentially to `nums.size() - 1`. Inside the loop, all operations (comparisons, increments, and assignments) execute in $O(1)$ constant time. Thus, the total number of operations is directly proportional to $(n-1)$, resulting in a linear time complexity of $O(n)$.

### Space Complexity
`O(1)` — No auxiliary memory is allocated that scales with the input size. The algorithm modifies the input vector `nums` in-place and only uses two scalar integer variables (`i` and `j`) to track the array indices, requiring constant $O(1)$ auxiliary space.

## Edge Cases
- **Single Element Array (`nums.size() == 1`)**:
  The loop condition `i < nums.size()` starting at `i = 1` immediately fails because `1 < 1` is false. The loop is skipped

## Solution

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[j]) {
                j++;
                nums[j] = nums[i];
            }
        }

        return j+1;
    }
};
```
