class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_table = {}
        temp = headA
        while temp:
            hash_table[temp] = temp.val
            temp = temp.next
        temp = headB
        while temp:
            if temp in hash_table:
                return temp
            temp = temp.next
        return None
