# 15. 3Sum

🔗 [LeetCode Problem](https://leetcode.com/problems/3sum/)

**Author:** [@Pragadheeshwar-06](https://leetcode.com/u/Pragadheeshwar-06/) (Global Rank: #642,244)  
**Difficulty:** Medium  
**Pattern:** Two Pointers (Array, Sorting)  

---

## Problem Statement

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

 

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

**Example 2:**

```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

**Example 3:**

```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

 

**Constraints:**

	- `3 <= nums.length <= 3000`

	- `-10^(5) <= nums[i] <= 10^(5)`

---

## Approach

We initialize two pointers at strategic positions (e.g. start and end boundaries). By inspecting elements at the pointer boundaries and adjusting them inward based on the problem criteria, we systematically reduce the search space in $O(n)$ time.

---

## Algorithm

1. Set up left pointer at the beginning and right pointer at the terminal index.
2. Enter a loop that continues while the left pointer is strictly less than the right pointer.
3. Evaluate the current state (e.g., sum, area, or element comparison) at both pointers.
4. If the target condition is satisfied, record or return the solution.
5. Advance the left pointer or decrement the right pointer towards the optimum direction.

---

## Why This Works

Because the problem features monotonic properties (or sorted ordering), narrowing down from extremes eliminates large sections of suboptimal pairs without having to explicitly test them.

---

## Complexity Analysis

- **Time Complexity:** `O(n log n)` — Dominated by the initial sorting of elements before linear traversal.
- **Space Complexity:** `O(1)` — Uses only a constant number of pointers and accumulator variables.

---

## Solution

```cpp
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```cpp []
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> ans;
        int n = nums.size();

        for (int i = 0; i < n - 2; i++) {
```
