# 21. Merge Two Sorted Lists

## Problem
Given the heads of two sorted singly linked lists, `list1` and `list2`, merge them into a single sorted linked list. The merge must be done in-place by splicing together the nodes of the original lists. Return the head of the merged linked list.

## Approach
The submitted solution implements an elegant, iterative, in-place merge algorithm using a **dummy (sentinel) node** and two pointers. 

Instead of dynamically allocating a dummy node on the heap (which would require manual deallocation to prevent memory leaks), the solution instantiates a local dummy node `d` on the stack. A traversal pointer `c` is initialized to point to `d`. The algorithm then compares the current nodes of both lists, links the node with the smaller value to the merged list, and advances the corresponding pointer. Once one of the lists is exhausted, the remaining nodes of the other list are appended directly to the end of the merged list in $O(1)$ time.

## How the Solution Works
1. **Initialization**: 
   - A stack-allocated sentinel node `ListNode d(0)` is declared. This simplifies the edge cases associated with initializing the head of the merged list.
   - A pointer `ListNode* c` is initialized to the address of `d` (`&d`). `c` acts as the tail of the newly merged list.
2. **Iterative Comparison**:
   - The `while (a && b)` loop runs as long as both pointers `a` (representing the current node of the first list) and `b` (representing the current node of the second list) are non-null.
   - Inside the loop, `a->val` and `b->val` are compared:
     - If `a->val <= b->val`, the tail pointer's next pointer `c->next` is linked to `a`, and `a` is advanced to `a->next`.
     - Otherwise, `c->next` is linked to `b`, and `b` is advanced to `b->next`.
   - In both cases, the tail pointer `c` is advanced to its new tail, `c->next`.
3. **Appending Remainder**:
   - Once the loop terminates, at least one of the lists is fully exhausted.
   - The expression `c->next = a ? a : b;` checks which list still has remaining elements and appends the remainder of that list directly to the merged list.
4. **Return**:
   - The function returns `d.next`, which points to the actual head of the merged sorted list (skipping the dummy node `d`).

## Algorithm
1. Initialize a dummy `ListNode` named `d` with value `0`, and a pointer `c` pointing to `d`.
2. While both `a` and `b` are not `nullptr`:
   1. If `a->val <= b->val`, set `c->next` to `a` and advance `a` to `a->next`.
   2. Otherwise, set `c->next` to `b` and advance `b` to `b->next`.
   3. Advance the tracking pointer `c` to `c->next`.
3. Once the loop terminates, check which pointer (`a` or `b`) is not null, and assign it to `c->next`.
4. Return `d.next`.

## Why This Works
The algorithm relies on the loop invariant that at the start of each iteration of the `while` loop, the merged list ending at `c` is sorted, and all nodes in the merged list are strictly less than or equal to the nodes remaining in the lists pointed to by `a` and `b`. 

Since both input lists are already sorted in non-decreasing order:
- The minimum element of the remaining unmerged nodes must reside at either the head of list `a` or the head of list `b`.
- By choosing $\min(\text{head}(a), \text{head}(b))$ and appending it to `c->next`, the non-decreasing order of the merged list is preserved.
- When one list is completely traversed, all elements in the remaining non-empty list are guaranteed to be greater than or equal to all elements currently in the merged list. Thus, we can safely append the entire remaining sublist in $O(1)$ time.

## Complexity

### Time Complexity
`O(N + M)` — where $N$ and $M$ are the number of nodes in lists `a` and `b`, respectively. 
- In each iteration of the `while` loop, exactly one node from either list `a` or list `b` is processed and the corresponding pointer is advanced.
- The maximum number of loop iterations is $\min(N, M)$.
- After the loop, the remaining elements of the non-empty list (which can be at most $|N - M|$ elements) are linked in $O(1)$ constant time.
- Therefore, the total time complexity scales linearly with the total number of nodes, $O(N + M)$.

### Space Complexity
`O(1)` — The algorithm merges the lists in-place by updating the pointer offsets (`next` pointers) of the existing nodes. 
- No new dynamic nodes are allocated on the heap.
- The dummy node `d` is allocated on the stack frame of the function call, using $O(1)$ auxiliary stack space.
- The pointer `c` uses $O(1)$ memory.

## Edge Cases
- **Both lists are empty (`a == nullptr` and `b == nullptr`)**: The `while` loop does not execute. `c->next = a ? a : b` evaluates to `c->next = nullptr`. `d.next` returns `nullptr`. Correct.
- **One list is empty (e.g., `a == nullptr` and `b != nullptr`)**: The `while` loop is bypassed. `c->next` is assigned to `b`. `d.next` correctly returns the head of `b`.
- **Lists with identical elements**: The stable comparison `a->val <= b->val` ensures nodes from list `a` are appended before nodes from list `b`, maintaining stability and correctness.

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
