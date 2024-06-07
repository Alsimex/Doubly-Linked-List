#######################################
# Author:       Dayton McManus
# Name:         DLL.py
# Description:  Implementation of a Doubly Linked List, for use with a driver program
#               Includes functions push, insertAfter, remove, get, search, and to_string
#######################################

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoublyLinkedList:
    # initiates list
    def __init__(self):
        self.head = None

    # puts new node at start of list
    def push(self, data):
        newNode = Node(next=self.head, data=data)

        if self.head is not None:
            self.head.prev = newNode
        
        self.head = newNode

    # puts new node after another node of a value
    def insertAfter(self, data, prev_data):
        prev = self.search(prev_data)
        if prev is None:
            print(prev_data, "not found")
        else:
            next = prev.next

            newNode = Node(next=next, prev=prev, data=data)

            prev.next = newNode
            if next is not None:
                next.prev = newNode


    # removes node of a value, if found
    def remove(self, data):
        temp = self.search(data)
        if temp is None:
            print(data, "not found")
        else:
            prev = temp.prev
            next = temp.next

            if next is not None:
                next.prev = prev
            if prev is not None:
                prev.next = next
            if temp is self.head:
                self.head = next

    # returns node of a value, if found
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            temp = temp.next
        return temp

    # returns position of a value, if found
    # head is at position 1
    def get(self, data):
        pos = 0
        found = False
        temp = self.head
        while temp is not None:
            pos += 1
            if temp.data == data:
                found = True
                break
            temp = temp.next
        if pos == 0:
            print("DLL is empty")
        elif found:
            print(data, "found at position", pos)
        else:
            print(data, "not found")

    # prints list in full
    def to_string(self):
        if self.head is None:
            print("DLL is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
            