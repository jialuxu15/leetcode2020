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

            Prev=None

 
            while head is not None:
          
                Ptemp=head
                head=head.next
                Ptemp.next=Prev
                Prev=Ptemp
            
            return Prev
        
        def LinkedNodeDel(head:ListNode,n)->ListNode:

            cur1= head
            cur2=head
            for i in range(n):
                cur1=cur1.next
            if cur1 is None:
                head=head.next
                return head
                    
            while cur1.next is not None:
                cur1=cur1.next
                cur2=cur2.next
            
            temp=cur2.next
            cur2.next=temp.next

            return head
        traverse(head)    
        traverse(LinkedNodeDel(head,n))


a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(5)

a.next=b
b.next=c
c.next=d
d.next=e

s=Solution()
s.removeNthFromEnd(a,4)





            
            
            
