#######################################
# Author:       Dayton McManus
# Name:         Driver.py
# Description:  Driver for the DoublyLinkedList class from DLL.py
#######################################

from DLL import DoublyLinkedList

def main():
    DLL = DoublyLinkedList()

    DLL.push("World")
    DLL.push("Hello")
    DLL.push('D')
    DLL.push(3)
    
    DLL.to_string()

    DLL.get("Hello")
    DLL.remove(3)
    DLL.remove('7')
    DLL.get("Hello")

    DLL.to_string()

    DLL.insertAfter("New", "Hello")
    DLL.insertAfter(27, "World")
    DLL.insertAfter(':', 'D')
    DLL.insertAfter("Oops!", 13)
    
    DLL.to_string()
    
    DLL.push('H')
    DLL.remove(27)
    DLL.insertAfter('!', "World")

    DLL.to_string()

if __name__ == "__main__":
    main()