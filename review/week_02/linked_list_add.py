class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


def sum_node(linedList):
    cur_sum = 0
    head = linedList.head
    while head is not None:
        cur_sum = cur_sum * 10 + head.data
        head = head.next
    return cur_sum


def get_linked_list_sum(linked_1, linked_2):
    sum_total = sum_node(linked_1) + sum_node(linked_2)
    return sum_total


linked_list_1 = Linkedlist(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = Linkedlist(3)
linked_list_2.append(4)
linked_list_2.append(5)

print(get_linked_list_sum(linked_list_1, linked_list_2))
