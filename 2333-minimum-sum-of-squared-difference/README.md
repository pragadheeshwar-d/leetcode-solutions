# 2333. Minimum Sum of Squared Difference

## Approach
The code uses a bucket count (frequency map) approach combined with a greedy strategy. Since element values in nums1 and nums2 are bounded, the absolute differences are at most 10^5. First, it computes the absolute difference between each pair of elements in nums1 and nums2 and records the frequency of each difference in a fixed-size vector. Then, combining k1 and k2 into a total budget of modifications, it greedily processes differences from the largest possible value (10^5) down to 0, decrementing differences by 1 as long as operations remain. Finally, it computes the sum of squares using the modified difference counts.

## How It Works
1. `vector<int> difference((int) 1e5 + 1)`: Initializes a frequency array of size 100,001 to store counts of absolute difference values.
2. Iterates over `nums1` and `nums2`, incrementing `difference[abs(nums1[i] - nums2[i])]` for each index `i`.
3. Sets `left = k1 + k2`, representing the total budget of decrements available across both arrays.
4. Iterates `i` downwards from `1e5` down to `0`:
   - `acc = difference[i]`: Retrieves the count of elements currently having absolute difference `i`.
   - If `acc <= left`:
     - If `i <= 1`, returning `0` early because any remaining operations can reduce all remaining non-zero differences to `0`.
     - Shifts all `acc` occurrences of difference `i` to `i - 1` by updating `difference[i - 1] += difference[i]` and setting `difference[i] = 0`.
     - Subtracts `acc` from `left` and continues.
   - Else (`acc > left`):
     - If `i == 0`, breaks/returns `0`.
     - Subtracts `left` from `difference[i]` and adds `left` to `difference[i - 1]`, consuming all remaining operations.
     - Breaks out of the loop.
5. Iterates `i` from `1` to `1e5` to accumulate `answer += (long long)difference[i] * ((long long)i * i)`.
6. Returns `answer`.

## Complexity
- **Time Complexity:** `O(N + M)` — Where N is the size of the input vectors `nums1` and `nums2`, and M is the maximum possible absolute difference (fixed at 10^5). Initializing and filling the frequency vector takes O(N) time. Greedily reducing differences from 10^5 down to 0 takes O(M) steps. Calculating the final answer takes O(M) steps. Thus, the total time complexity is O(N + M).
- **Space Complexity:** `O(M)` — Where M is the maximum possible absolute difference (10^5 + 1). The `difference` array requires a fixed extra space of size 100,001 integers.

## Edge Cases
- Total operations (k1 + k2) are sufficient to reduce all differences to 0, returning 0 early.
- All initial differences are 0 (i.e., nums1 and nums2 are identical), resulting in 0 total squared difference.
- Remaining operations (left) are fewer than the frequency of the current maximum difference (acc > left), requiring partial reduction at that level before breaking.

## Solution
```cpp
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        vector<int> difference( (int) 1e5+1);
        
        for(int i = 0; i<nums1.size();i++)
        {
            difference[abs(nums1[i] - nums2[i])]++;
        }
        
        int value = 0, left = k1+k2;
        int acc = 0;
        
        for(int i = (int) 1e5; i>=0; i--)
        {
            acc = difference[i];
            if(acc <= left)
            {
                if(i<=1)
                    return 0;
                
                difference[i-1] += difference[i];
                difference[i]=0;
                left -= acc;
            }
            else
            {
                if(i==0)
                    return 0;
                difference[i] -= left;
                difference[i-1] += left;
                break;
            }
        }
        long long answer = 0;
        
        for(int i = 1ll; i<=1e5; i++)
        {
            answer += (long long)difference[i] * ((long long)i*i);
        }
        
        return answer;
    }
};
```

## GitHub Source
🔗 [View original solution in `pragadheeshwar-d/LeetCode-Solutions`](https://github.com/pragadheeshwar-d/LeetCode-Solutions/blob/main/2333-minimum-sum-of-squared-difference/solution.cpp)

## LeetCode
🔗 [LeetCode Problem: Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/)
