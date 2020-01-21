import string
from npNode import NpNode

class LRUCache:
    def __init__(self, maxsize):
        self.dict = {}
        self.head = None
        self.tail = None
        self.maxsize = maxsize

    def moveNodeToHead(self, nodeToMove):
        #check if node to move is head.
        if nodeToMove.prev:
            nodeToMove.prev.next = nodeToMove.next # remove node being accessed from the queue.
            self.head.prev = nodeToMove
            nodeToMove.next = self.head  # make the node the head of the queue
            self.head = nodeToMove 
            self.head.prev = None
        return
        
    # returns None if the key is not found. Else returns the Value
    def get(self, key):
        if key in self.dict:
            self.moveNodeToHead(self.dict[key]) # value is stored in a doubly linked node
            return self.head.get_value()
        else:
            retVal = None
        return retVal

    # adds the key value pair to the Cache. 
    def put(self, key, value):
        if not self.dict: #check if the dictionary is empty
            nodeToAdd = NpNode(key, value)
            self.head = nodeToAdd
            self.tail = nodeToAdd
        elif key in self.dict:
            #change the value of the node and move it to head.
            nodeToChange = self.dict[key]
            self.moveNodeToHead(nodeToChange)
            self.head.set(key, value)
        else:
            if (len(self.dict) == self.maxsize):
                keyToRemove = self.tail.get_key()
                self.tail = self.tail.prev
                self.tail.next = None   
                del self.dict[keyToRemove] 
            nodeToAdd = NpNode(key, value)
            self.head.prev = nodeToAdd
            nodeToAdd.next = self.head
            self.head = nodeToAdd
        self.dict[key] = self.head
        return

    def delete(self, key):
        if key in self.dict:
            nodeToRemove = self.dict[key]
            # check if nodeToRemove = head
            if not nodeToRemove.prev:
                if not nodeToRemove.next:
                    self.reset() #looks like there is only one key
                    return
                else:
                    self.head = nodeToRemove.next
                    nodeToRemove.next = None #removing connections for good measure
            elif not nodeToRemove.next: #check if the node to remove is the tail
                self.tail = self.tail.prev
                nodeToRemove.prev = None
            else: # its a middle node
                nodeToRemove.prev.next = nodeToRemove.next
            del self.dict[key]
            return
        else:
             return

    def reset(self):
        # reset all values except max size.
        self.dict = {}
        self.head = None
        self.tail = None
        return

