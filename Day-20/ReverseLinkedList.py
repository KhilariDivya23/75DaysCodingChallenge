class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr, post = None, head, head
        while post:
            post = post.next
            curr.next = pre
            pre = curr
            curr = post
        return pre
