from datastructures import sll

#in place solution
def mergeTwoLists( list1, list2 ):
    if not ( list1 and list2 ):
        return list1 or list2

    if list1.val <= list2.val:
        head = list1
        runner = list1
        slider = list2
    else:
        head = list2
        runner = list2
        slider = list1

    while runner.next and slider:
        if runner.next.val > slider.val:
            #insert node
            shrimp = slider.next
            slider.next = runner.next
            runner.next = slider

            #move pointers
            slider = shrimp
        
        runner = runner.next
    
    if slider:
        runner.next = slider

    return head

#return new list - less assignments as used to insert nodes during in place solution
def mergeTwoLists2( list1, list2 ):
    if not ( list1 and list2 ):
        return list1 or list2

    headly = runner = sll.ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            runner.next = list1
            list1 = list1.next
        else:
            runner.next = list2
            list2 = list2.next
        runner = runner.next
    
    runner.next = list1 or list2

    return headly.next
