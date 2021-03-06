# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        result = tmp
        while True:
            if l1 :
                tmp.val += l1.val
                l1 = l1.next

            if l2 :
                tmp.val += l2.val
                l2 = l2.next

            if tmp.val > 9:
                tmp.val = tmp.val - 10
                tmp.next = ListNode(1)
            else:
                if( l1 or l2):
                    tmp.next = ListNode(0)
                else:
                    return result
            tmp = tmp.next

        return result
