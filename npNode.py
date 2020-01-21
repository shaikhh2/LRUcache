import string

class NpNode:
    def __init__(self, key, value):
        self.data = (key, value)
        self.next = None
        self.prev = None
        return
    
    def has_value(self, value):
        # Check if the given value is equal to the value stored in the node
        if value == self.data[1]:
            return True
        else:
             return False

    def get(self):
        return self.data

    def get_value(self):
        return self.data[1]

    def get_key(self):
        return self.data[0]

    def set(self, key, value):
        self.data = (key, value)




