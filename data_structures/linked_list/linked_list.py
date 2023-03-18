
from typing import Any


class Node:   
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None


class LinkedList:
    head: Node | None
    length: int = 0
    
    def __init__(self):
        self.head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        else:
            last_node = self.get_nth_node(self.length - 1)
            last_node.next = new_node
            self.length += 1
            
    def prepend(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def insert_to_index(self, data: Any, index: int) -> None:      
        if index > self.length:
            raise ValueError("Index out of range!")
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        nth_node = self.get_nth_node(index - 1)
        list_after = nth_node.next
        new_node.next = list_after
        nth_node.next = new_node
        
    
    def pop(self) -> None:
        node = self.get_nth_node(self.length - 1) 
        node.next = None
    
    def get_nth_node(self, index: int) -> Node | None:
        nth_node = self.head
        
        for i in range(0, index):
            nth_node = nth_node.next    
        return nth_node
    

    def print_list(self) -> None:
        node = self.head 
        print("\nPrinting list...")
        while (node is not None):
            print(node.data, end = " -> ")
            node = node.next
        print("\n")
    

myList = LinkedList()
myList.append("carlos")
myList.print_list()
myList.append("juan")
myList.print_list()
myList.append("pedro")
myList.print_list()
myList.prepend("liliana")
myList.prepend("Angie")
myList.print_list()
myList.insert_to_index("Maria", 3)
myList.print_list()
myList.pop()
myList.print_list()

