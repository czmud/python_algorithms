from datastructures import sll

def reverseKGroup(head, k: int):
    if not head or k == 1:
        return head
    
    streaker = head
    for i in range(k-1):
        if streaker:
            streaker = streaker.next
    
    if not streaker:
        return head
    trailer = head
    head = streaker

    while streaker:
        streaker = streaker.next

        walker = trailer.next
        print(f'trailer: {trailer.val}')
        runner = trailer.next.next

        sprinter = streaker
        for i in range(k-1):
            if streaker:
                streaker = streaker.next
        
        if streaker:
            trailer.next = streaker
        else:
            trailer.next = sprinter

        for i in range(k-2):
            walker.next = trailer
            trailer = walker
            walker = runner
            runner = runner.next
        walker.next = trailer
        trailer = sprinter

    return head




list1 = sll.SinglyLinkedList().insertAtBack(0)

list1.head = reverseKGroup(list1.head, 2)
list1.display()
