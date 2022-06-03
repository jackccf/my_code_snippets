#Implementation of the linked list ADT
#Filename: linkedList.py
# 

class Node:
    """
        Fields: _data is the value stored in the node.
                _next is the reference to the next node in the sequence.
    """
    def __init__(self, data, next=None) :
        self._data = data
        self._next = next

    def getData(self):
        return self._data


class SLinkedList:
    """
        Fields: _headVal is a reference to the starting node of the list.
    """

    def __init__(self, head=None):
        self._headVal = head

    def isEmpty(self):
        return self._headVal == None

    def traverse(self):
        if self._headVal is None:
            print("List does not contain any nodes.")
        else:
            currNode = self._headVal
            while currNode != None:
                print(currNode._data, end=" ")
                currNode = currNode._next
            print("")
   
    def insertMystery(self, item, after):
        newNode = Node(item)
        if self._headVal is None:
            self._headVal = newNode
        else: 
            currNode = self._headVal
            while currNode._next != None:
                if currNode._data == after:
                    newNode._next = currNode._next
                    break
                currNode = currNode._next            
            currNode._next = newNode

    #Insert a new item at the end of the list
    def append (self, item):
        newNode = Node(item)
        if self._headVal is None:
            self._headVal = newNode
        else: 
            currNode = self._headVal
            while currNode._next != None:
                currNode = currNode._next            
            currNode._next = newNode

    def pop(self):
        """Pop the last element in the list"""
        currNode = self._headVal
        prevNode = None

        while currNode:
            if not currNode._next:
                if not prevNode:
                    # We are popping the 'head' of the list 
                    self._headVal = None
                else:
                    prevNode._next = None
                    
                return currNode

            prevNode = currNode
            currNode = currNode._next

    def popFirst(self):
        """Pop the first element in the list"""
        currNode = self._headVal
        if currNode:
            self._headVal = currNode._next
        return currNode 

    def remove_by_val(self, target):
        # Traverse the list and find the node to be deleted
        currNode = self._headVal
        prevNode = None
        while currNode and currNode._data != target:
            prevNode = currNode
            currNode = currNode._next
            
        if currNode is None:
            # the value is not found
            return None

        # Unlink it from the list
        if prevNode is None:
            self._headVal = currNode._next
        elif currNode:
            prevNode._next = currNode._next
    
        # remove the reference in the deleted node    
        currNode._next = None

        #return the value deleted
        return currNode._data

if __name__ == '__main__':
    # create the linked list with a single node containing 'Anders'
    aList = SLinkedList(Node("Anders"))
    # insert nodes using insertMystery
    aList.insertMystery("Betsy", "")
    aList.insertMystery("Davy", "")
    aList.insertMystery("Martha", "")
    aList.insertMystery("Jodie", "")
    aList.insertMystery("Katie", "")    
    aList.traverse()

    # another list to illustrate the difference
    aList = SLinkedList(Node("Anders"))
    # insert nodes using insertMystery
    aList.insertMystery("Betsy", "")
    aList.insertMystery("Davy", "")
    aList.insertMystery("Martha", "Betsy")
    aList.insertMystery("Jodie", "Anders")
    aList.insertMystery("Katie", "")    
    aList.traverse()    
