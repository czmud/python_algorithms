from datastructures import sll


def swapPairs( head ):
    if not head:
        return head
    if not head.next:
        return head
    
    headly = head
    head = head.next
    runner = head.next
    head.next = headly

    while runner:
        if not runner.next:
            headly.next = runner
            return head
        
        headly.next = runner.next

        shrimp = headly
        headly = runner
        runner = shrimp.next.next
        shrimp.next.next = headly
    
    headly.next = None
    return head


list1 = sll.SinglyLinkedList().insertAtBack(0).insertAtBack(1).insertAtBack(2).insertAtBack(3).insertAtBack(4)

list1.display()
print('---')
list1.head = swapPairs(list1.head)

list1.display()


