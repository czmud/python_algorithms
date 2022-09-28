class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__( self ):
        self.head = None
    
    def isEmpty( self ):
        if self.head:
            return False
        return True

    def insertAtFront( self, val ):
        newNode = ListNode( val ) 
        newNode.next = self.head
        self.head = newNode
        return self
    
    def insertAtBack( self, val ):
        newNode = ListNode( val ) 
        if self.isEmpty():
            self.head = newNode
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = newNode
        return self
    
    def display( self ):
        if self.isEmpty():
            print("This list is empty!")
        else:
            n = 0
            runner = self.head
            print(f'node {n} : {runner.val}')
            while runner.next:
                runner = runner.next
                n += 1
                print(f'node {n} : {runner.val}')
        return self

