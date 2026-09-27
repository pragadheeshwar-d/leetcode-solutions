# 17. Letter Combinations of a Phone Number

🔗 [LeetCode Problem](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

**Author:** [@Pragadheeshwar-06](https://leetcode.com/u/Pragadheeshwar-06/) (Global Rank: #642,244)  
**Difficulty:** Medium  
**Pattern:** Backtracking (Hash Map, Hash Table, String)  

---

## Problem Statement

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

**Example 1:**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2:**

```
Input: digits = "2"
Output: ["a","b","c"]
```

 

**Constraints:**

	- `1 <= digits.length <= 4`

	- `digits[i]` is a digit in the range `['2', '9']`.

---

## Approach

We explore the decision tree by incrementally building candidates. If a candidate cannot lead to a valid solution, we backtrack by undoing the decision and restoring the previous state before attempting the next choice.

---

## Algorithm

1. Parse the input and initialize necessary state variables.
2. Traverse the elements and process required conditions.
3. Update the accumulated output or answer trackers.
4. Return the final calculated result.

---

## Why This Works

The solution systematically satisfies problem invariants with minimal overhead, maintaining correct bounds and optimal termination conditions throughout execution.

---

## Complexity Analysis

- **Time Complexity:** `O(n)` — Single pass through the input with O(1) operations per element.
- **Space Complexity:** `O(n)` — Stores elements or frequencies in a hash table proportional to the input size.

---

## Solution

```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        
        if (digits.empty()) {
            return res;
        }
        
        unordered_map<char, string> digitToLetters = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        
        backtrack(digits, 0, "", res, digitToLetters);
        
        return res;        
    }

    void backtrack(const string& digits, int idx, string comb, vector<string>& res, const unordered_map<char, 
    string>& digitToLetters) {
        if (idx == digits.length()) {
            res.push_back(comb);
```
