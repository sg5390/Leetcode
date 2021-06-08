class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None
    
    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while(node.next):
                node = node.next
            node.next = new_node
        
    # def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """

        
    # def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        if self.is_empty:
            return None
