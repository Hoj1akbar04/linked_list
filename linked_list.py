class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push_list(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_list(self, before_data, new_data):
        if before_data is None:
            print("Error!")

        new_node = Node(new_data)
        new_node.next = before_data.next
        before_data.next = new_node

    def append_list(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_data = self.head
        while last_data.next:
            last_data = last_data.next
        last_data.next = new_node

# 1. push method
"""ll = LinkedList()
a = Node(23)
b = Node(67)
c = Node(12)
d = Node(4)
e = Node(10)
ll.head = b
b.next = d
d.next = e
e.next = c
c.next = a
#ll.print_linked()

ll.push_list(33)
ll.push_list(44)
ll.push_list(55)
ll.print_linked()"""

#2. insert method
"""ll = LinkedList()
a = Node(18)
b = Node(6)
c = Node(2)
d = Node(74)
e = Node(16)
ll.head = c
c.next = d
d.next = e
e.next = b
b.next = a
#ll.print_linked()

ll.insert_list(c, 66)
ll.insert_list(a, 99)
ll.insert_list(d, 100)
ll.print_linked()"""

# 3. append method
ll = LinkedList()
a = Node(21)
b = Node(11)
c = Node(37)
d = Node(5)
e = Node(39)
ll.head = d
d.next = b
b.next = e
e.next = c
c.next = a
#ll.print_linked()

ll.append_list(101)
ll.append_list(102)
ll.append_list(103)
ll.print_linked()