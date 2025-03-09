# Medium
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        i = 0
        curr = l1
        while curr != None:
            sum+=curr.val*(10**i)
            curr = curr.next
            i+=1
        curr = l2
        i = 0
        while curr != None:
            sum+=curr.val * (10**i)
            curr = curr.next
            i+=1
        sum = str(sum)
        temp = None
        for i in range(0,len(sum)):
            num = ListNode(int(sum[i]),temp)
            temp = num
        return temp