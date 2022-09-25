class QueueNode:
    def __init__( self, data ):
        self.data = data
        self.next = None

class Queue:
    def __init__( self ):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty( self ):
        return not bool( self.size )

    def enqueue( self, val ):
        newNode = QueueNode( val )
        if self.isEmpty() :
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return self.size
    
    def dequeue( self ):
        if self.isEmpty():
            return None
        
        oldHead = self.head
        self.head = self.head.next
        
        self.size -= 1
        if self.size < 1:
            self.tail = None

        return oldHead
    
    def seed( self, data ):
        for val in data:
            self.enqueue(val)

    def contains( self, searchVal ):
        runner = self.head
        while( runner ):
            if searchVal == runner.data:
                return True
            runner = runner.next
        return False

    def display( self ):
        if self.isEmpty():
            print("This queue is empty")
            return
        index = 0
        runner = self.head
        print("Head "+str(index)+": "+str(runner.data))
        if runner.next:
            runner = runner.next
            index += 1
            while( runner.next ):
                print("Node "+str(index)+": "+str(runner.data))
                runner = runner.next
                index += 1
        print("Tail "+str(index)+": "+str(runner.data))