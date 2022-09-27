from datastructures import sll

def removeNthFromEnd( head, n: int):
    # check for edge case
    if not head.next:
        return None

    # determine length of list
    length = 1
    runner = head
    while runner.next:
        runner = runner.next
        length += 1

    # check to see if we are removing first position
    if length == n:
        head = head.next
        return head
    
    # else run through list until land on position to remove
    runner = head
    for i in range(length-n-1):
        runner = runner.next
    
    runner.next = runner.next.next

    return head

#considering a two runner (fast and slow) approach
def removeNthFromEnd2( head, n: int ):
    fast = slow = head
    for i in range(n):
        fast = fast.next
    if not fast:
        head = head.next
        return head
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

list1 = sll.SinglyLinkedList().insertAtBack(1).insertAtBack(2)

print(removeNthFromEnd(list1.head, 1).__dict__)