# 14. Longest Common Prefix

## Problem
Given an array of strings `strs`, find the longest common prefix string amongst all strings in the array. If there is no common prefix, return an empty string `""`.

## Approach
The submitted code uses a **vertical scanning** approach. It selects the first string, `strs[0]`, as the baseline reference and iterates through its characters column by column (index by index). For every character position `i` in `strs[0]`, it checks all subsequent strings `strs[j]` to confirm that index `i` is within bounds and contains the identical character. At the first character mismatch or string termination, the common prefix found up to that point is extracted and returned.

## How the Solution Works
1. The outer loop runs with index `i` ranging from `0` to `strs[0].size() - 1`.
2. For each index `i`, it caches the reference character `char c = strs[0][i]`.
3. The inner loop iterates with index `j` from `1` to `strs.size() - 1` across the remaining strings in the vector.
4. Inside the inner loop, the condition `if (i >= strs[j].size() || strs[j][i] != c)` evaluates whether:
   - String `strs[j]` is shorter than the current index `i` (`i >= strs[j].size()`).
   - The character in `strs[j]` at index `i` differs from `c` (`strs[j][i] != c`).
5. If either condition is true, the common prefix ends at index `i - 1`. The method returns `strs[0].substr(0, i)`, which extracts the substring from index `0` of length `i`.
6. If the outer loop finishes completely without triggering a return, every character of `strs[0]` was successfully validated across all strings. The function returns `strs[0]`.

## Algorithm
1. Loop index `i` from `0` up to `strs[0].size() - 1`.
2. Set `c = strs[0][i]`.
3. Loop index `j` from `1` up to `strs.size() - 1`:
   - If `i >= strs[j].size()` or `strs[j][i] != c`:
     - Return `strs[0].substr(0, i)`.
4. If the loop completes, return `strs[0]`.

## Why This Works
A common prefix must be a prefix of every string in `strs`, including `strs[0]`. By checking each character position `i` across all strings simultaneously, the algorithm ensures that all strings match up to index `i - 1`. The moment any string either runs out of characters or contains a character that does not match `strs[0][i]`, the longest valid prefix cannot extend to index `i` or beyond. Hence, the prefix of length `i` (`strs[0].substr(0, i)`) is strictly the longest common prefix. If all characters of `strs[0]` are matched across all strings, then `strs[0]` itself is the common prefix.

## Complexity

### Time Complexity
$O(S)$ where $S$ is the sum of all characters across all strings in `strs`. 
In the worst case (where all strings are identical), the algorithm performs character comparisons for every character in every string: up to $M \times N$ operations, where $N$ is the number of strings (`strs.size()`) and $M$ is the length of `strs[0]`. In the best case, it terminates on the first comparison $O(1)$ if the first character of the second string does not match `strs[0][0]`. The final substring extraction takes $O(L)$ time, where $L \le M$ is the length of the prefix.

### Space Complexity
$O(1)$ auxiliary space.
The comparison logic operates in-place using only a couple of scalar index variables (`i`, `j`) and a single character variable (`c`). The returned string `strs[0].substr(0, i)` allocates memory for the output prefix, which takes $O(L)$ space where $L$ is the length of the longest common prefix.

## Edge Cases
- **Single string in vector (`strs.size() == 1`)**: The inner loop condition `j < strs.size()` (i.e., `1 < 1`) is immediately false, the outer loop completes, and `strs[0]` is correctly returned.
- **Empty first string (`strs[0] == ""`)**: The outer loop condition `i < strs[0].size()` (i.e., `0 < 0`) is false, the loop does not execute, and `strs[0]` (`""`) is returned.
- **First string longer than subsequent strings**: Handled by `i >= strs[j].size()`, which prevents out-of-bounds access and returns the prefix matching the shorter string.
- **No common prefix**: The condition `strs[j][0] != c` triggers on `i = 0`, returning `strs[0].substr(0, 0)`, which correctly evaluates to `""`.
- **All strings identical**: The checks never fail, and `strs[0]` is returned at the end.

## Solution

```cpp
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i = 0; i < strs[0].size(); i++) {
            char c = strs[0][i];

            for (int j = 1; j < strs.size(); j++) {
                if (i >= strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i);
                }
            }
        }

        return strs[0];
    }
};
```
