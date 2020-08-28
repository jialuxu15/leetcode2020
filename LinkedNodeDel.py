#Definition for singly-linked list.
class ListNode:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        def traverse(head:ListNode)->ListNode:
            cur = head
            
            content=[]

            while cur is not None:
                content.append(cur.val)
                cur=cur.next
            print(content)

    
        def LinkedNodeReverse(head:ListNode)->ListNode:

            Prev=ListNode()

 
            while head is not None:
                Ptemp=head
                head=head.next
                Ptemp.next=Prev
                Prev=Ptemp
            
            return Prev

        traverse(head)
        traverse(LinkedNodeReverse(head))

a=ListNode()
b=ListNode()
c=ListNode()
a.val=1
b.val=2
c.val=3
a.next=b
b.next=c

s=Solution()
s.removeNthFromEnd(a,3)





            
            
            
