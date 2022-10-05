from datastructures import sll

def addTwoNumbers( l1, l2 ):
    sum = sumRunner = sll.ListNode( l1.val + l2.val )
    l1 = l1.next
    l2 = l2.next
    if(sum.val < 10 ):
        carry = 0
    else:
        carry = int(sum.val / 10)
        sum.val = sum.val % 10
    while( l1 or l2 or carry ):
        if( l1 and l2 ):
            sumRunner.next = sll.ListNode( l1.val + l2.val + carry )
            l1 = l1.next
            l2 = l2.next
        elif( l1 and not l2 ):
            sumRunner.next = sll.ListNode( l1.val + carry )
            l1 = l1.next
        elif( not l1 and l2 ):
            sumRunner.next = sll.ListNode( l2.val + carry )
            l2 = l2.next
        else:
            sumRunner.next = sll.ListNode( carry )
        
        if( sumRunner.next.val < 10 ):
            carry = 0
        else:
            carry = int(sumRunner.next.val / 10)
            sumRunner.next.val = sumRunner.next.val % 10 
        sumRunner = sumRunner.next
    return sum