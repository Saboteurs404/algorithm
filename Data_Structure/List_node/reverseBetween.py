'''
给你单链表的头指针 head 和两个整数 left 和 right ，
其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head:ListNode, left: int, right: int) -> ListNode:
        if head == None:
            return ListNode()

        # 反转整个列表
        reverseNode = self.reverseListNode(head, left, right)

        # 当前位置
        i = 1

        while head != None:

            if i >= left and i <= right:
                if i == 1:
                    result = ListNode(reverseNode.val)
                    results = result
                else:
                    result.next = ListNode(reverseNode.val)
                    result = result.next
                reverseNode = reverseNode.next
            else:
                if i == 1:
                    result = ListNode(head.val)
                    results = result
                else:
                    result.next = ListNode(head.val)
                    result = result.next

            i += 1
            if head.next != None:
                head  = head.next
            else:
                break
        print(1)
        print(results)
        return results

    def reverseListNode(self, head, left, right):
        temp = head
        i = 1
        if temp == None:
            return ListNode()
        while i <= right and temp != None:
            if i == left:
                reverseNode = ListNode(temp.val)
            elif i > left :
                reverseNode = ListNode(temp.val, reverseNode)
            temp = temp.next
            i += 1
        return reverseNode

if __name__ == '__main__':
    Solution()
