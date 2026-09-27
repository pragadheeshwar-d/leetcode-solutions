# 2. Add Two Numbers

🔗 [LeetCode Problem](https://leetcode.com/problems/add-two-numbers/)

- **Author:** [@pragadheeshward](https://leetcode.com/u/pragadheeshward/) (Global Rank: #5,000,001)
- **Difficulty:** Medium
- **Pattern:** Linked List (Math, Recursion)
- **Runtime:** 0 ms (Beats 100.0%)
- **Memory:** 77.2 MB (Beats 45.7%)

---

## Problem Statement

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

**Example 1:**

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

 

**Constraints:**

	- The number of nodes in each linked list is in the range `[1, 100]`.

	- `0 <= Node.val <= 9`

	- It is guaranteed that the list represents a number that does not have leading zeros.

---

## Intuition

We analyze the input structure and apply an optimal traversal, maintaining key state variables to compute the target result cleanly.

---

## Approach

We implement an efficient linear iteration strategy, leveraging Linked List to compute the required result cleanly.

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
- **Space Complexity:** `O(1)` — Constant auxiliary memory used for pointer and state tracking.

---

## Solution

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* curr = &dummy;
        int carry = 0;

        while (l1 != NULL || l2 != NULL || carry) {
            int a = (l1 != NULL) ? l1->val : 0;
            int b = (l2 != NULL) ? l2->val : 0;

            int sum = a + b + carry;

            carry = sum / 10;
            int digit = sum % 10;

            curr->next = new ListNode(digit);
            curr = curr->next;

            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
        }

        return dummy.next;
    }
};
```
