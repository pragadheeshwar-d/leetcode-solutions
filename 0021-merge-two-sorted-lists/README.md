# 21. Merge Two Sorted Lists

## Problem
Given the heads of two sorted singly-linked lists, `list1` and `list2`, merge them into a single sorted linked list by splicing the existing nodes together, and return the head of the merged list.

## Approach
The submitted solution uses an iterative two-pointer technique utilizing a stack-allocated sentinel (dummy) node. 

Instead of dynamically allocating a dummy node or handling the head of the new list as a special case, the function declares a local `ListNode d(0)`. A tracking pointer `c` points to the tail of the newly formed merged list (initially pointing to `&d`). Pointers `a` and `b` iterate through their respective linked lists, linking the node with the smaller or equal value to `c->next` until one list is exhausted. The remaining non-empty list is then linked to the end.

## How the Solution Works
1. `ListNode d(0);`: Allocates a dummy node `d` on the stack with value `0` to serve as a fixed anchor for the merged list.
2. `ListNode* c = &d;`: Initializes a pointer `c` to track the current tail of the merged list.
3. `while (a && b)`: Iterates as long as both pointers `a` and `b` point to valid nodes:
   - If `a->val <= b->val`, `c->next` is set to `a`, and `a` is advanced to `a->next`.
   - Otherwise, `c->next` is set to `b`, and `b` is advanced to `b->next`.
   - `c` is updated to `c->next` to point to the newly appended node.
4. `c->next = a ? a : b;`: Once one list is exhausted, the loop terminates. The ternary operator checks if `a` is non-null; if so, `a` is appended to `c->next`. Otherwise, `b` (which is either a valid list or `nullptr`) is appended.
5. `return d.next;`: Returns the node following the dummy sentinel, which is the head of the merged list.

## Algorithm
1. Initialize a sentinel node `d` on the stack and set a tail pointer `c = &d`.
2. While both `a` and `b` are not null:
   1. If `a->val <= b->val`, set `c->next = a` and update `a = a->next`.
   2. Otherwise, set `c->next = b` and update `b = b->next`.
   3. Advance the tail pointer: `c = c->next`.
3. Connect the remaining nodes by assigning `c->next = a ? a : b`.
4. Return `d.next`.

## Why This Works
Because both input lists are already sorted in non-decreasing order, comparing the current front nodes of each list (`a->val` and `b->val`) guarantees that the smaller of the two is the globally smallest element remaining across both lists. Splicing this node onto the tail `c` maintains the non-decreasing order of the merged list. When one list is exhausted, all remaining elements in the other list are greater than or equal to all elements merged so far and are already sorted among themselves, making a single pointer reassignment sufficient to complete the merge.

## Complexity

### Time Complexity
$O(n + m)$ — where $n$ is the number of nodes in list `a` and $m$ is the number of nodes in list `b`. Each iteration of the `while` loop advances either `a` or `b` by one node. The loop executes at most $\min(n, m)$ times, and the remaining nodes ($|n - m|$) are attached in $O(1)$ time. Thus, the total number of operations is proportional to the total number of nodes, $n + m$.

### Space Complexity
$O(1)$ — The algorithm performs an in-place merge by rewiring the `next` pointers of the existing nodes. The auxiliary space consists only of the stack-allocated node `d` and the pointer `c`, requiring constant extra memory.

## Edge Cases
- **Both lists are empty (`a == nullptr`, `b == nullptr`):** The `while` loop does not execute. `c->next` is assigned `b` (which is `nullptr`), and `d.next` returns `nullptr`.
- **One list is empty (`a == nullptr` or `b == nullptr`):** The `while` loop does not execute. `c->next` attaches the non-empty list directly via `a ? a : b`, correctly returning the non-empty list.
- **Lists of different lengths:** The loop stops when the shorter list is exhausted, and the remaining sublist of the longer list is attached in a single step without traversing it.
- **Lists with identical values:** Handled by the `<=` condition, which arbitrarily favors list `a` to preserve stability.

## Solution

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* a, ListNode* b) {
        ListNode d(0);
        ListNode* c = &d;

        while (a && b) {
            if (a->val <= b->val) {
                c->next = a;
                a = a->next;
            } else {
                c->next = b;
                b = b->next;
            }
            c = c->next;
        }

        c->next = a ? a : b;

        return d.next;
    }
};
```
