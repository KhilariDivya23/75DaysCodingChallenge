class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans, h1, h2 = None, list1, list2
        curr = ans
        if h1 is None:
            return h2
        elif h2 is None:
            return h1
        while h1 and h2:
            if h1.val < h2.val:
                new_node = ListNode(h1.val)
                if ans is None:
                    ans = new_node
                    curr = ans
                else:
                    curr.next = new_node
                    curr = curr.next
                h1 = h1.next
            else:
                new_node = ListNode(h2.val)
                if ans is None:
                    ans = new_node
                    curr = ans
                else:
                    curr.next = new_node
                    curr = curr.next
                h2 = h2.next
        if h1:
            curr.next = h1
        if h2:
            curr.next = h2
        return ans
