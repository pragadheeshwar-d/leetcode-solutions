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